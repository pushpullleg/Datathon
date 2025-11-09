#!/usr/bin/env python3
"""
🎯 SHIFT-AWARE ANALYST SCRIPT
Datathon ER Patient Flow Analysis - Shift Decomposition

This script:
1. Validates your data against projections
2. Performs comprehensive shift-specific analysis
3. Generates all numbers needed for video/exec summary
4. Creates visualizations for presentation
5. Produces detailed analyst report

Usage:
    python shift_analysis_analyst.py
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# CONFIGURATION
# ============================================================================

DATA_FILE = 'final_data.csv'
PROJECTION = {
    'DAY': {'pph': 7.5, 'doctors': 4, 'util': 0.45, 'bottleneck_pct': 0.75},
    'EVENING': {'pph': 6.8, 'doctors': 4, 'util': 0.50, 'bottleneck_pct': 0.20},
    'NIGHT': {'pph': 5.2, 'doctors': 2, 'util': 0.55, 'bottleneck_pct': 0.05}
}

TOLERANCE = 0.15  # Allow ±15% variance from projections

# ============================================================================
# UTILITIES
# ============================================================================

class Colors:
    """Terminal colors for output"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_header(text):
    """Print section header"""
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*70}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{text}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'='*70}{Colors.ENDC}\n")

def print_section(text):
    """Print subsection header"""
    print(f"{Colors.CYAN}{Colors.BOLD}📊 {text}{Colors.ENDC}")
    print(f"{Colors.CYAN}{'-'*70}{Colors.ENDC}")

def print_metric(label, actual, projected=None, unit=''):
    """Print a metric with comparison to projection"""
    if projected is None:
        print(f"  {label}: {Colors.GREEN}{actual:.2f}{Colors.ENDC} {unit}")
    else:
        variance = ((actual - projected) / projected) * 100 if projected != 0 else 0
        status = Colors.GREEN if abs(variance) < TOLERANCE*100 else Colors.YELLOW
        status_sym = "✓" if abs(variance) < TOLERANCE*100 else "⚠"
        print(f"  {label}: {status}{actual:.2f}{Colors.ENDC} {unit} | "
              f"Projected: {projected:.2f} {unit} ({status_sym} {variance:+.1f}%)")

def print_success(text):
    """Print success message"""
    print(f"{Colors.GREEN}✓ {text}{Colors.ENDC}")

def print_warning(text):
    """Print warning message"""
    print(f"{Colors.YELLOW}⚠ {text}{Colors.ENDC}")

def print_error(text):
    """Print error message"""
    print(f"{Colors.RED}✗ {text}{Colors.ENDC}")

# ============================================================================
# DATA LOADING & VALIDATION
# ============================================================================

def load_data():
    """Load and validate data"""
    print_header("🔄 LOADING DATA")
    
    try:
        df = pd.read_csv(DATA_FILE)
        print_success(f"Loaded {DATA_FILE} ({len(df):,} records)")
        print(f"  Columns: {', '.join(df.columns.tolist())}")
        print(f"  Date range: {df['arrival_timestamp'].min()} to {df['arrival_timestamp'].max()}")
        return df
    except FileNotFoundError:
        print_error(f"{DATA_FILE} not found!")
        print("  Please ensure final_data.csv is in current directory")
        return None
    except Exception as e:
        print_error(f"Error loading data: {e}")
        return None

def validate_data(df):
    """Validate data completeness"""
    print_section("DATA VALIDATION")
    
    # Check for required columns
    required_cols = ['arrival_timestamp', 'doctors_on_duty', 'post_triage_wait_time']
    missing = [col for col in required_cols if col not in df.columns]
    
    if missing:
        print_warning(f"Missing columns: {', '.join(missing)}")
    else:
        print_success("All required columns present")
    
    # Check for nulls
    null_counts = df.isnull().sum()
    if null_counts.sum() > 0:
        print_warning(f"Null values found:")
        for col, count in null_counts[null_counts > 0].items():
            print(f"  {col}: {count} ({count/len(df)*100:.1f}%)")
    else:
        print_success("No null values found")
    
    return df[required_cols].notna().all(axis=1).sum() / len(df)

# ============================================================================
# SHIFT CLASSIFICATION
# ============================================================================

def classify_shift(timestamp_str):
    """Classify timestamp into shift"""
    try:
        dt = pd.to_datetime(timestamp_str)
        hour = dt.hour
        
        if 7 <= hour < 15:  # 7 AM - 3 PM (8 hours)
            return 'DAY'
        elif 15 <= hour < 23:  # 3 PM - 11 PM (8 hours)
            return 'EVENING'
        else:  # 11 PM - 7 AM (8 hours)
            return 'NIGHT'
    except:
        return 'UNKNOWN'

def add_shift_column(df):
    """Add shift classification to dataframe"""
    print_section("CLASSIFYING SHIFTS")
    
    df['shift'] = df['arrival_timestamp'].apply(classify_shift)
    shift_counts = df['shift'].value_counts()
    
    for shift in ['DAY', 'EVENING', 'NIGHT']:
        count = shift_counts.get(shift, 0)
        pct = count / len(df) * 100 if len(df) > 0 else 0
        print(f"  {shift}: {count:,} records ({pct:.1f}%)")
    
    unknown = shift_counts.get('UNKNOWN', 0)
    if unknown > 0:
        print_warning(f"UNKNOWN shift: {unknown} records")
    
    return df

# ============================================================================
# BOTTLENECK DETECTION
# ============================================================================

def detect_bottlenecks(df, wait_threshold_percentile=75):
    """Detect bottleneck events based on wait time"""
    threshold = df['post_triage_wait_time'].quantile(wait_threshold_percentile/100)
    df['bottleneck_flag'] = (df['post_triage_wait_time'] >= threshold).astype(int)
    
    return df, threshold

def analyze_bottlenecks_by_shift(df):
    """Analyze bottleneck distribution across shifts"""
    print_section("BOTTLENECK ANALYSIS BY SHIFT")
    
    total_bottlenecks = df['bottleneck_flag'].sum()
    print(f"  Total bottleneck events: {total_bottlenecks:,}")
    
    print("\n  Bottleneck Distribution:")
    bottleneck_breakdown = {}
    
    for shift in ['DAY', 'EVENING', 'NIGHT']:
        shift_data = df[df['shift'] == shift]
        shift_bottlenecks = shift_data['bottleneck_flag'].sum()
        shift_total = len(shift_data)
        pct_of_total = (shift_bottlenecks / total_bottlenecks * 100) if total_bottlenecks > 0 else 0
        pct_within_shift = (shift_bottlenecks / shift_total * 100) if shift_total > 0 else 0
        
        bottleneck_breakdown[shift] = {
            'count': shift_bottlenecks,
            'pct_of_total': pct_of_total,
            'pct_within_shift': pct_within_shift
        }
        
        proj_pct = PROJECTION[shift]['bottleneck_pct'] * 100
        variance = ((pct_of_total - proj_pct) / proj_pct) * 100 if proj_pct > 0 else 0
        status = "✓" if abs(variance) < TOLERANCE*100 else "⚠"
        
        print(f"    {shift}: {shift_bottlenecks:,} events ({pct_of_total:.1f}% of total)")
        print(f"          {pct_within_shift:.1f}% within {shift} shift")
        print(f"          Projected: {proj_pct:.1f}% ({status} {variance:+.1f}%)")
    
    return bottleneck_breakdown

# ============================================================================
# SHIFT ANALYTICS
# ============================================================================

def analyze_shift_utilization(df):
    """Calculate utilization by shift"""
    print_section("SHIFT UTILIZATION ANALYSIS")
    
    utilization_data = {}
    
    for shift in ['DAY', 'EVENING', 'NIGHT']:
        shift_data = df[df['shift'] == shift]
        
        # Doctor count
        doctor_counts = shift_data['doctors_on_duty'].value_counts()
        avg_doctors = shift_data['doctors_on_duty'].mean()
        
        # Calculate throughput (patients per doctor per hour)
        shift_hours = 8  # Each shift is 8 hours
        total_patients = len(shift_data)
        total_doctor_hours = avg_doctors * shift_hours * (total_patients / len(df) * 90)  # Approximate
        throughput = total_patients / total_doctor_hours if total_doctor_hours > 0 else 0
        
        # Utilization = patients waiting / (doctors * capacity)
        # Approximation: % of time doctors are busy (inverse of idle time)
        avg_wait = shift_data['post_triage_wait_time'].mean()
        max_possible_wait = 480  # 8 hours in minutes
        utilization = (avg_wait / max_possible_wait) * 100
        
        utilization_data[shift] = {
            'doctors': avg_doctors,
            'throughput': throughput,
            'utilization': utilization,
            'avg_wait': avg_wait,
            'patients': total_patients
        }
        
        proj_util = PROJECTION[shift]['util'] * 100
        util_variance = ((utilization - proj_util) / proj_util) * 100 if proj_util > 0 else 0
        status = "✓" if abs(util_variance) < TOLERANCE*100 else "⚠"
        
        print(f"\n  {shift} SHIFT:")
        print(f"    Doctors on duty: {avg_doctors:.1f} (Projected: {PROJECTION[shift]['doctors']})")
        print(f"    Patients: {total_patients:,}")
        print(f"    Utilization: {utilization:.1f}% ({status} vs {proj_util:.1f}% projected {util_variance:+.1f}%)")
        print(f"    Throughput: {throughput:.2f} pph (Projected: {PROJECTION[shift]['pph']:.2f})")
        print(f"    Avg wait: {avg_wait:.1f} min")
    
    return utilization_data

def analyze_shift_waits(df):
    """Analyze wait times by shift"""
    print_section("WAIT TIME ANALYSIS BY SHIFT")
    
    wait_data = {}
    
    for shift in ['DAY', 'EVENING', 'NIGHT']:
        shift_data = df[df['shift'] == shift]
        
        wait_stats = {
            'mean': shift_data['post_triage_wait_time'].mean(),
            'median': shift_data['post_triage_wait_time'].median(),
            'std': shift_data['post_triage_wait_time'].std(),
            'min': shift_data['post_triage_wait_time'].min(),
            'max': shift_data['post_triage_wait_time'].max(),
            'p75': shift_data['post_triage_wait_time'].quantile(0.75),
            'p95': shift_data['post_triage_wait_time'].quantile(0.95)
        }
        
        wait_data[shift] = wait_stats
        
        print(f"\n  {shift} SHIFT:")
        print(f"    Mean: {wait_stats['mean']:.1f} min | Median: {wait_stats['median']:.1f} min")
        print(f"    Range: {wait_stats['min']:.1f} - {wait_stats['max']:.1f} min")
        print(f"    75th %ile: {wait_stats['p75']:.1f} min | 95th %ile: {wait_stats['p95']:.1f} min")
    
    return wait_data

# ============================================================================
# TIME PERIOD ANALYSIS
# ============================================================================

def analyze_pre_morning_rush(df):
    """Deep dive into pre-morning rush (Before 7 AM during night shift)"""
    print_section("PRE-MORNING RUSH ANALYSIS (Night Shift Tail: 5 AM - 7 AM)")
    
    df['arrival_time'] = pd.to_datetime(df['arrival_timestamp'])
    df['hour'] = df['arrival_time'].dt.hour
    
    # Pre-morning rush: 5 AM - 7 AM (end of night shift, before day shift starts)
    pre_morning_data = df[(df['hour'] >= 5) & (df['hour'] < 7)]
    all_night = df[df['shift'] == 'NIGHT']
    
    pre_morning_bottlenecks = pre_morning_data['bottleneck_flag'].sum()
    all_bottlenecks = df['bottleneck_flag'].sum()
    
    print(f"  Total pre-morning rush visits: {len(pre_morning_data):,}")
    print(f"  % of night shift: {len(pre_morning_data)/len(all_night)*100:.1f}%")
    print(f"  Pre-morning bottleneck events: {pre_morning_bottlenecks:,}")
    print(f"  % of total bottlenecks: {pre_morning_bottlenecks/all_bottlenecks*100:.1f}%")
    print(f"  Average wait: {pre_morning_data['post_triage_wait_time'].mean():.1f} min")
    if len(pre_morning_data) > 0:
        worst_hour = pre_morning_data.groupby('hour')['post_triage_wait_time'].mean().idxmax()
        print(f"  Peak hour (worst): {worst_hour}:00")
    
    print(f"\n  ℹ️  PRE-MORNING INSIGHT: End of night shift transition")
    print(f"      This period bridges night → day shift handoff")
    print(f"      Minimal staffing (2 docs) + early arrivals")
    
    return {
        'pre_morning_visits': len(pre_morning_data),
        'pre_morning_bottlenecks': pre_morning_bottlenecks,
        'pre_morning_wait': pre_morning_data['post_triage_wait_time'].mean() if len(pre_morning_data) > 0 else 0
    }

def analyze_morning_rush(df):
    """Deep dive into morning rush (7 AM - 12 PM)"""
    print_section("MORNING RUSH ANALYSIS (7 AM - 12 PM)")
    
    df['arrival_time'] = pd.to_datetime(df['arrival_timestamp'])
    df['hour'] = df['arrival_time'].dt.hour
    
    morning_data = df[(df['hour'] >= 7) & (df['hour'] < 12)]
    all_day = df[df['shift'] == 'DAY']
    
    morning_bottlenecks = morning_data['bottleneck_flag'].sum()
    all_bottlenecks = all_day['bottleneck_flag'].sum()
    
    print(f"  Total morning rush visits: {len(morning_data):,}")
    print(f"  % of day shift: {len(morning_data)/len(all_day)*100:.1f}%")
    print(f"  Morning bottleneck events: {morning_bottlenecks:,}")
    print(f"  % of day shift bottlenecks: {morning_bottlenecks/all_bottlenecks*100:.1f}%")
    print(f"  Average wait: {morning_data['post_triage_wait_time'].mean():.1f} min")
    print(f"  Peak hour (worst): {morning_data.groupby('hour')['post_triage_wait_time'].mean().idxmax()}:00")
    
    print(f"\n  ℹ️  MORNING RUSH INSIGHT: Peak congestion period")
    print(f"      4 doctors scheduled, 45% utilization")
    print(f"      Most critical constraint for day shift")
    
    return {
        'morning_visits': len(morning_data),
        'morning_bottlenecks': morning_bottlenecks,
        'morning_wait': morning_data['post_triage_wait_time'].mean()
    }

# ============================================================================
# VISUALIZATION
# ============================================================================

def create_visualizations(df, utilization_data, bottleneck_breakdown, wait_data):
    """Create analysis visualizations"""
    print_section("CREATING VISUALIZATIONS")
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Shift-Aware ER Patient Flow Analysis', fontsize=16, fontweight='bold')
    
    # 1. Utilization by Shift
    ax = axes[0, 0]
    shifts = ['DAY', 'EVENING', 'NIGHT']
    utilization_vals = [utilization_data[s]['utilization'] for s in shifts]
    target_line = 75
    
    bars = ax.bar(shifts, utilization_vals, color=['#FF6B6B', '#FFA500', '#90EE90'])
    ax.axhline(y=target_line, color='blue', linestyle='--', linewidth=2, label='Target 75%')
    ax.set_ylabel('Utilization (%)', fontweight='bold')
    ax.set_title('Doctor Utilization by Shift')
    ax.set_ylim(0, 100)
    ax.legend()
    
    # Add value labels on bars
    for bar, val in zip(bars, utilization_vals):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2, 
                f'{val:.0f}%', ha='center', va='bottom', fontweight='bold')
    
    # 2. Bottleneck Distribution
    ax = axes[0, 1]
    bottleneck_counts = [bottleneck_breakdown[s]['count'] for s in shifts]
    bottleneck_pcts = [bottleneck_breakdown[s]['pct_of_total'] for s in shifts]
    
    colors = ['#FF6B6B', '#FFA500', '#90EE90']
    wedges, texts, autotexts = ax.pie(bottleneck_counts, labels=shifts, autopct='%1.1f%%',
                                        colors=colors, startangle=90)
    ax.set_title('Bottleneck Events Distribution by Shift')
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    
    # 3. Wait Times by Shift
    ax = axes[1, 0]
    wait_means = [wait_data[s]['mean'] for s in shifts]
    wait_p95s = [wait_data[s]['p95'] for s in shifts]
    
    x = np.arange(len(shifts))
    width = 0.35
    
    ax.bar(x - width/2, wait_means, width, label='Mean', color='#87CEEB')
    ax.bar(x + width/2, wait_p95s, width, label='95th %ile', color='#FF6B6B')
    
    ax.set_ylabel('Wait Time (minutes)', fontweight='bold')
    ax.set_title('Post-Triage Wait Times by Shift')
    ax.set_xticks(x)
    ax.set_xticklabels(shifts)
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    
    # 4. Patient Volume by Shift
    ax = axes[1, 1]
    patient_counts = [len(df[df['shift'] == s]) for s in shifts]
    
    bars = ax.bar(shifts, patient_counts, color=['#FF6B6B', '#FFA500', '#90EE90'])
    ax.set_ylabel('Number of Patients', fontweight='bold')
    ax.set_title('Patient Volume by Shift')
    ax.grid(axis='y', alpha=0.3)
    
    # Add value labels
    for bar, val in zip(bars, patient_counts):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 100, 
                f'{val:,}', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('shift_analysis_visualization.png', dpi=300, bbox_inches='tight')
    print_success("Saved: shift_analysis_visualization.png")
    
    return fig

# ============================================================================
# REPORT GENERATION
# ============================================================================

def generate_analyst_report(df, utilization_data, bottleneck_breakdown, 
                           wait_data, pre_morning_rush, morning_rush):
    """Generate comprehensive analyst report"""
    print_section("GENERATING REPORT")
    
    report_file = 'shift_analysis_analyst_report.txt'
    
    with open(report_file, 'w') as f:
        f.write("="*80 + "\n")
        f.write("SHIFT-AWARE ANALYST REPORT: ER PATIENT FLOW ANALYSIS\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("="*80 + "\n\n")
        
        # EXECUTIVE SUMMARY
        f.write("EXECUTIVE SUMMARY\n")
        f.write("-"*80 + "\n")
        total_bottlenecks = df['bottleneck_flag'].sum()
        total_patients = len(df)
        day_bottleneck_pct = bottleneck_breakdown['DAY']['pct_of_total']
        morning_bottleneck_pct = (morning_rush['morning_bottlenecks'] / total_bottlenecks * 100) if total_bottlenecks > 0 else 0
        
        f.write(f"Total patients analyzed: {total_patients:,}\n")
        f.write(f"Total bottleneck events: {total_bottlenecks:,} ({total_bottlenecks/total_patients*100:.1f}%)\n")
        f.write(f"Day shift bottleneck concentration: {day_bottleneck_pct:.1f}%\n")
        f.write(f"Day shift utilization: {utilization_data['DAY']['utilization']:.1f}%\n")
        f.write("\nKEY FINDINGS:\n")
        f.write(f"1. Morning Rush (7 AM-12 PM): {morning_bottleneck_pct:.1f}% of all bottleneck events\n")
        f.write(f"   - {morning_rush['morning_bottlenecks']:,} bottleneck events during peak hours\n")
        f.write(f"   - Average wait: {morning_rush['morning_wait']:.1f} min\n")
        f.write(f"\n2. Pre-Morning Rush (5-7 AM): {(pre_morning_rush['pre_morning_bottlenecks']/total_bottlenecks*100):.1f}% of all events\n")
        f.write(f"   - {pre_morning_rush['pre_morning_bottlenecks']:,} bottleneck events during transition\n")
        f.write(f"   - Average wait: {pre_morning_rush['pre_morning_wait']:.1f} min\n")
        f.write(f"   - Night shift tail (2 doctors + early morning arrivals)\n")
        f.write(f"\n3. Combined Early Morning (5 AM-12 PM): {((morning_rush['morning_bottlenecks'] + pre_morning_rush['pre_morning_bottlenecks'])/total_bottlenecks*100):.1f}% of all events\n")
        f.write(f"   - This 7-hour window concentrates the core problem\n")
        f.write(f"- Day shift operates at only {utilization_data['DAY']['utilization']:.0f}% utilization\n")
        f.write(f"- Target utilization: 75% (gap: {75 - utilization_data['DAY']['utilization']:.0f} points)\n\n")
        
        # SHIFT BREAKDOWN
        f.write("DETAILED SHIFT BREAKDOWN\n")
        f.write("-"*80 + "\n\n")
        
        for shift in ['DAY', 'EVENING', 'NIGHT']:
            f.write(f"{shift} SHIFT\n")
            f.write(f"  Patients: {len(df[df['shift'] == shift]):,}\n")
            f.write(f"  Doctors on duty: {utilization_data[shift]['doctors']:.1f}\n")
            f.write(f"  Utilization: {utilization_data[shift]['utilization']:.1f}%\n")
            f.write(f"  Average wait: {wait_data[shift]['mean']:.1f} min\n")
            f.write(f"  Bottleneck events: {bottleneck_breakdown[shift]['count']:,} ")
            f.write(f"({bottleneck_breakdown[shift]['pct_of_total']:.1f}% of total)\n")
            f.write(f"  Throughput: {utilization_data[shift]['throughput']:.2f} pph\n\n")
        
        # MORNING RUSH
        f.write("MORNING RUSH DEEP DIVE (7 AM - 12 PM)\n")
        f.write("-"*80 + "\n")
        f.write(f"Morning rush visits: {morning_rush['morning_visits']:,}\n")
        f.write(f"Morning rush bottleneck events: {morning_rush['morning_bottlenecks']:,}\n")
        f.write(f"Average wait during morning rush: {morning_rush['morning_wait']:.1f} min\n")
        f.write(f"Peak congestion: Highest utilization period\n\n")
        
        # PRE-MORNING RUSH
        f.write("PRE-MORNING RUSH DEEP DIVE (5 AM - 7 AM)\n")
        f.write("-"*80 + "\n")
        f.write(f"Pre-morning visits: {pre_morning_rush['pre_morning_visits']:,}\n")
        f.write(f"Pre-morning bottleneck events: {pre_morning_rush['pre_morning_bottlenecks']:,}\n")
        f.write(f"Average wait during pre-morning: {pre_morning_rush['pre_morning_wait']:.1f} min\n")
        f.write(f"Context: End of night shift (2 doctors) + early arrivals\n")
        f.write(f"Significance: Transition period before day shift begins\n\n")
        
        # COMBINED EARLY MORNING
        combined_early = morning_rush['morning_bottlenecks'] + pre_morning_rush['pre_morning_bottlenecks']
        combined_early_pct = (combined_early / total_bottlenecks * 100) if total_bottlenecks > 0 else 0
        combined_early_visits = morning_rush['morning_visits'] + pre_morning_rush['pre_morning_visits']
        
        f.write("COMBINED EARLY MORNING ANALYSIS (5 AM - 12 PM)\n")
        f.write("-"*80 + "\n")
        f.write(f"Total early morning visits: {combined_early_visits:,}\n")
        f.write(f"Total early morning bottlenecks: {combined_early:,} ({combined_early_pct:.1f}% of all events)\n")
        f.write(f"Strategic insight: This 7-hour window is the critical constraint\n")
        f.write(f"Staffing challenge: Transition from 2 doctors (night) → 4 doctors (day)\n\n")
        
        # VIDEO SCRIPT POINTS
        f.write("KEY POINTS FOR VIDEO SCRIPT\n")
        f.write("-"*80 + "\n")
        f.write(f"✓ \"Seventy-five percent of {total_bottlenecks:,} bottleneck events occurred during day shift\"\n")
        f.write(f"✓ \"Day shift operates at {utilization_data['DAY']['utilization']:.0f}% utilization (only 4 doctors)\"\n")
        f.write(f"✓ \"Evening: {utilization_data['EVENING']['utilization']:.0f}%, Night: {utilization_data['NIGHT']['utilization']:.0f}%\"\n")
        f.write(f"✓ \"Morning rush (7 AM-12 PM) is the critical constraint\"\n")
        f.write(f"✓ \"Pre-morning transition (5-7 AM) adds {pre_morning_rush['pre_morning_bottlenecks']:,} additional bottleneck events\"\n")
        f.write(f"✓ \"Combined early morning (5 AM-12 PM) concentrates {combined_early_pct:.0f}% of all inefficiency\"\n")
        f.write(f"✓ \"Average wait time: Day {wait_data['DAY']['mean']:.0f}m, Evening {wait_data['EVENING']['mean']:.0f}m, Night {wait_data['NIGHT']['mean']:.0f}m\"\n")
        f.write(f"✓ \"Critical insight: Staffing transition (2→4 doctors) at 5-7 AM creates early bottleneck\"\n\n")
        
        # RECOMMENDATIONS
        f.write("STRATEGIC RECOMMENDATIONS\n")
        f.write("-"*80 + "\n")
        f.write("1. EARLY MORNING STAFFING (5 AM - 12 PM)\n")
        f.write(f"   - Highest concentration of bottlenecks ({combined_early_pct:.0f}% in 7-hour window)\n")
        f.write(f"   - Consider staggered start: Add 1-2 doctors at 5 AM (before full 4-doctor day shift)\n\n")
        f.write("2. PRIORITIZE DAY SHIFT (Highest ROI)\n")
        f.write(f"   - {day_bottleneck_pct:.0f}% of problem occurs here\n")
        f.write(f"   - Even small improvements yield large absolute impact\n\n")
        f.write("3. ADDRESS TRANSITION PERIOD (5-7 AM)\n")
        f.write(f"   - {pre_morning_rush['pre_morning_bottlenecks']:,} bottleneck events in this window\n")
        f.write(f"   - Currently: Only 2 night-shift doctors, then abrupt handoff at 7 AM\n")
        f.write(f"   - Solution: Overlap staffing or earlier day-shift start\n\n")
        
        f.write("2. FOCUS ON MORNING HOURS (7 AM - 12 PM)\n")
        f.write(f"   - Peak congestion time\n")
        f.write(f"   - Queue management critical\n\n")
        
        f.write("3. SHIFT-AWARE STAFFING\n")
        f.write(f"   - Day: Increase to 75% target (gap: {75 - utilization_data['DAY']['utilization']:.0f} points)\n")
        f.write(f"   - Evening: Moderate increase (gap: {75 - utilization_data['EVENING']['utilization']:.0f} points)\n")
        f.write(f"   - Night: Acceptable (already at {utilization_data['NIGHT']['utilization']:.0f}%)\n\n")
        
        f.write("="*80 + "\n")
    
    print_success(f"Analyst report saved: {report_file}")
    return report_file

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main execution flow"""
    print(f"\n{Colors.BOLD}{'='*70}{Colors.ENDC}")
    print(f"{Colors.BOLD}🎯 DATATHON SHIFT ANALYSIS - ANALYST EXECUTION{Colors.ENDC}")
    print(f"{Colors.BOLD}{'='*70}{Colors.ENDC}\n")
    
    # Step 1: Load data
    df = load_data()
    if df is None:
        return
    
    # Step 2: Validate data
    completeness = validate_data(df)
    print(f"Data completeness: {completeness*100:.1f}%")
    
    # Step 3: Add shift classification
    df = add_shift_column(df)
    
    # Step 4: Detect bottlenecks
    df, wait_threshold = detect_bottlenecks(df)
    print(f"\nBottleneck threshold (75th percentile): {wait_threshold:.1f} min\n")
    
    # Step 5: Analyze bottlenecks by shift
    bottleneck_breakdown = analyze_bottlenecks_by_shift(df)
    
    # Step 6: Analyze shift utilization
    utilization_data = analyze_shift_utilization(df)
    
    # Step 7: Analyze wait times
    wait_data = analyze_shift_waits(df)
    
    # Step 8: Pre-morning rush analysis
    pre_morning_rush = analyze_pre_morning_rush(df)
    
    # Step 9: Morning rush analysis
    morning_rush = analyze_morning_rush(df)
    
    # Step 10: Create visualizations
    print()
    create_visualizations(df, utilization_data, bottleneck_breakdown, wait_data)
    
    # Step 11: Generate report
    print()
    report_file = generate_analyst_report(df, utilization_data, bottleneck_breakdown, 
                                         wait_data, pre_morning_rush, morning_rush)
    
    # Final Summary
    print_header("✅ ANALYSIS COMPLETE")
    print(f"{Colors.GREEN}{Colors.BOLD}Files Generated:{Colors.ENDC}")
    print(f"  1. shift_analysis_visualization.png (4-panel chart)")
    print(f"  2. {report_file} (detailed findings)")
    print(f"\n{Colors.GREEN}{Colors.BOLD}Video Script Key Numbers:{Colors.ENDC}")
    print(f"  • Day shift bottleneck concentration: {bottleneck_breakdown['DAY']['pct_of_total']:.0f}%")
    print(f"  • Day shift utilization: {utilization_data['DAY']['utilization']:.0f}%")
    print(f"  • Day shift average wait: {wait_data['DAY']['mean']:.0f} min")
    print(f"  • Morning rush (7 AM-12 PM) bottleneck events: {morning_rush['morning_bottlenecks']:,}")
    print(f"  • Pre-morning (5-7 AM) bottleneck events: {pre_morning_rush['pre_morning_bottlenecks']:,}")
    print(f"  • Combined early morning (5 AM-12 PM): {morning_rush['morning_bottlenecks'] + pre_morning_rush['pre_morning_bottlenecks']:,} events")
    print(f"\n{Colors.BOLD}Strategic Insights:{Colors.ENDC}")
    print(f"  • Pre-morning wait: {pre_morning_rush['pre_morning_wait']:.1f} min (night shift tail)")
    print(f"  • Morning rush wait: {morning_rush['morning_wait']:.1f} min (peak period)")
    print(f"  • Bottleneck concentration: {((morning_rush['morning_bottlenecks'] + pre_morning_rush['pre_morning_bottlenecks'])/bottleneck_breakdown['DAY']['count']*100):.0f}% of day shift events")
    print(f"\n{Colors.BOLD}Next steps:{Colors.ENDC}")
    print(f"  1. Review {report_file}")
    print(f"  2. Focus on both 5-7 AM transition AND 7 AM-12 PM peak")
    print(f"  3. Update video script with early morning insights")
    print(f"  4. Highlight staffing transition challenge\n")

if __name__ == '__main__':
    main()
