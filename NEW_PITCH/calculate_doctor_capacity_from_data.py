"""
Calculate Doctor Capacity from Actual Data
===========================================
This script derives the doctor capacity empirically from the case study data
instead of assuming 2.5 patients/hour industry standard.
"""

import pandas as pd
import numpy as np

def calculate_doctor_capacity_from_data():
    """
    Calculate actual doctor capacity based on observed data during 
    low-utilization periods (evening shift) where capacity is not constrained.
    """
    
    print("="*80)
    print("CALCULATING DOCTOR CAPACITY FROM ACTUAL DATA")
    print("="*80)
    print()
    
    # Load data
    print("Loading data...")
    visits = pd.read_csv('../Meridian_City_Hospital_Data/Hospital_Visits.csv')
    staffing = pd.read_csv('../Meridian_City_Hospital_Data/Hospital_Staffing_EAST_LOCATION.csv')
    
    # Filter for EAST location only
    visits = visits[visits['Hospital ID'] == 'MC_ER_EAST'].copy()
    
    # Parse dates and times
    visits['Arrival Time'] = pd.to_datetime(visits['Arrival Time'], format='mixed', errors='coerce')
    visits['Doctor Seen'] = pd.to_datetime(visits['Doctor Seen'], format='mixed', errors='coerce')
    visits['Exit Time'] = pd.to_datetime(visits['Exit Time'], format='mixed', errors='coerce')
    
    # Calculate doctor service time (Doctor Seen to Exit)
    visits['doctor_service_time_min'] = (visits['Exit Time'] - visits['Doctor Seen']).dt.total_seconds() / 60
    
    # Add shift classification
    visits['hour'] = visits['Arrival Time'].dt.hour
    visits['shift'] = visits['hour'].apply(lambda h: 
        'DAY' if 7 <= h < 15 else 
        'EVENING' if 15 <= h < 23 else 
        'NIGHT'
    )
    
    # Add date for merging with staffing
    visits['date'] = visits['Arrival Time'].dt.date
    staffing['Date'] = pd.to_datetime(staffing['Date'])
    staffing['date'] = staffing['Date'].dt.date
    staffing['Shift'] = staffing['Shift'].str.upper()
    
    # Merge with staffing data
    merged = visits.merge(
        staffing[['date', 'Shift', 'Doctors On Duty']], 
        left_on=['date', 'shift'], 
        right_on=['date', 'Shift'],
        how='left'
    )
    
    print(f"Total visits analyzed: {len(merged):,}")
    print()
    
    # =======================================================================================
    # METHOD 1: Calculate capacity from EVENING SHIFT (unconstrained capacity)
    # =======================================================================================
    print("METHOD 1: EVENING SHIFT CAPACITY (Unconstrained)")
    print("-" * 80)
    print("Logic: Evening shift has low utilization (47%), so it represents actual")
    print("       doctor capacity without queue/wait constraints.")
    print()
    
    evening_data = merged[merged['shift'] == 'EVENING'].copy()
    
    # Get statistics
    total_evening_patients = len(evening_data)
    days_in_dataset = 90  # Q1 2025
    shift_hours = 8
    total_shift_hours = days_in_dataset * shift_hours
    
    avg_doctors_evening = evening_data['Doctors On Duty'].mean()
    patients_per_hour_evening = total_evening_patients / total_shift_hours
    
    # Calculate capacity per doctor
    capacity_per_doctor_evening = patients_per_hour_evening / avg_doctors_evening
    
    print(f"  Evening shift patients (Q1 2025):     {total_evening_patients:,}")
    print(f"  Days in dataset:                       {days_in_dataset}")
    print(f"  Shift hours per day:                   {shift_hours}")
    print(f"  Total shift-hours:                     {total_shift_hours:,}")
    print(f"  Average doctors on duty (evening):     {avg_doctors_evening:.2f}")
    print()
    print(f"  Patients per hour (evening):           {patients_per_hour_evening:.2f}")
    print(f"  Doctor capacity (evening):             {capacity_per_doctor_evening:.2f} patients/doctor/hour")
    print()
    print(f"  ✅ MEASURED DOCTOR CAPACITY: {capacity_per_doctor_evening:.2f} patients/hour/doctor")
    print()
    
    # =======================================================================================
    # METHOD 2: Calculate from average service time
    # =======================================================================================
    print("METHOD 2: SERVICE TIME CALCULATION")
    print("-" * 80)
    print("Logic: Calculate based on average time a doctor spends with each patient")
    print()
    
    # Filter valid service times (remove outliers)
    valid_service = merged[
        (merged['doctor_service_time_min'] > 0) & 
        (merged['doctor_service_time_min'] < 300)  # Less than 5 hours
    ]
    
    avg_service_time = valid_service['doctor_service_time_min'].median()  # Use median to avoid outliers
    capacity_from_service = 60 / avg_service_time
    
    print(f"  Median doctor service time:            {avg_service_time:.1f} minutes")
    print(f"  Calculated capacity:                   60 / {avg_service_time:.1f} = {capacity_from_service:.2f} patients/hour/doctor")
    print()
    print(f"  ✅ SERVICE-BASED CAPACITY: {capacity_from_service:.2f} patients/hour/doctor")
    print()
    
    # =======================================================================================
    # METHOD 3: Calculate from NIGHT SHIFT (moderate utilization ~80%)
    # =======================================================================================
    print("METHOD 3: NIGHT SHIFT CAPACITY (Moderate utilization)")
    print("-" * 80)
    print("Logic: Night shift at 80% utilization represents sustainable capacity")
    print()
    
    night_data = merged[merged['shift'] == 'NIGHT'].copy()
    
    total_night_patients = len(night_data)
    avg_doctors_night = night_data['Doctors On Duty'].mean()
    patients_per_hour_night = total_night_patients / total_shift_hours
    
    # Since night is at ~80% utilization, actual capacity is higher
    observed_capacity_night = patients_per_hour_night / avg_doctors_night
    actual_capacity_night = observed_capacity_night / 0.80  # Adjust for 80% utilization
    
    print(f"  Night shift patients (Q1 2025):        {total_night_patients:,}")
    print(f"  Average doctors on duty (night):       {avg_doctors_night:.2f}")
    print(f"  Patients per hour (night):             {patients_per_hour_night:.2f}")
    print(f"  Observed throughput per doctor:        {observed_capacity_night:.2f}")
    print(f"  Adjusted for 80% utilization:          {observed_capacity_night:.2f} / 0.80 = {actual_capacity_night:.2f}")
    print()
    print(f"  ✅ NIGHT-ADJUSTED CAPACITY: {actual_capacity_night:.2f} patients/hour/doctor")
    print()
    
    # =======================================================================================
    # FINAL RECOMMENDATION
    # =======================================================================================
    print("="*80)
    print("FINAL RECOMMENDATION")
    print("="*80)
    print()
    
    # Average the methods
    final_capacity = np.mean([capacity_per_doctor_evening, capacity_from_service, actual_capacity_night])
    
    print(f"  Method 1 (Evening shift):              {capacity_per_doctor_evening:.2f} patients/hour/doctor")
    print(f"  Method 2 (Service time):               {capacity_from_service:.2f} patients/hour/doctor")
    print(f"  Method 3 (Night adjusted):             {actual_capacity_night:.2f} patients/hour/doctor")
    print()
    print(f"  AVERAGE:                               {final_capacity:.2f} patients/hour/doctor")
    print()
    print(f"  📊 RECOMMENDED DOCTOR CAPACITY: {final_capacity:.2f} patients/hour (empirically derived)")
    print(f"  📌 Compare to industry standard: 2.5 patients/hour")
    print()
    
    if abs(final_capacity - 2.5) < 0.3:
        print("  ✅ Our data VALIDATES the industry standard of ~2.5 patients/hour!")
    elif final_capacity < 2.5:
        print(f"  ⚠️  Our hospital appears less efficient ({final_capacity:.2f} vs 2.5 industry standard)")
    else:
        print(f"  ✅ Our hospital is more efficient than average ({final_capacity:.2f} vs 2.5)")
    
    print()
    
    # =======================================================================================
    # RECALCULATE DAY SHIFT UTILIZATION WITH ACTUAL DATA
    # =======================================================================================
    print("="*80)
    print("DAY SHIFT UTILIZATION (Using Measured Capacity)")
    print("="*80)
    print()
    
    day_data = merged[merged['shift'] == 'DAY'].copy()
    total_day_patients = len(day_data)
    avg_doctors_day = day_data['Doctors On Duty'].mean()
    patients_per_hour_day = total_day_patients / total_shift_hours
    
    # Using the measured capacity
    day_shift_capacity = avg_doctors_day * final_capacity
    day_shift_utilization = (patients_per_hour_day / day_shift_capacity) * 100
    
    print(f"  Day shift patients (Q1 2025):          {total_day_patients:,}")
    print(f"  Average doctors on duty (day):         {avg_doctors_day:.2f}")
    print(f"  Patients per hour (demand):            {patients_per_hour_day:.2f}")
    print()
    print(f"  Doctor capacity (measured):            {final_capacity:.2f} patients/hour/doctor")
    print(f"  Total capacity:                        {avg_doctors_day:.2f} × {final_capacity:.2f} = {day_shift_capacity:.2f} patients/hour")
    print()
    print(f"  UTILIZATION:                           ({patients_per_hour_day:.2f} / {day_shift_capacity:.2f}) × 100")
    print(f"                                         = {day_shift_utilization:.1f}%")
    print()
    
    if day_shift_utilization > 100:
        print(f"  🔴 OVERLOADED: Day shift is operating at {day_shift_utilization:.1f}% capacity")
        print(f"     This is UNSUSTAINABLE and requires additional staffing.")
    elif day_shift_utilization > 85:
        print(f"  🟡 HIGH: Day shift is operating at {day_shift_utilization:.1f}% capacity")
        print(f"     Approaching maximum sustainable level.")
    else:
        print(f"  🟢 HEALTHY: Day shift is operating at {day_shift_utilization:.1f}% capacity")
    
    print()
    print("="*80)
    
    return {
        'evening_capacity': capacity_per_doctor_evening,
        'service_capacity': capacity_from_service,
        'night_capacity': actual_capacity_night,
        'final_capacity': final_capacity,
        'day_utilization': day_shift_utilization,
        'day_demand': patients_per_hour_day,
        'day_capacity': day_shift_capacity,
        'day_doctors': avg_doctors_day
    }


if __name__ == "__main__":
    results = calculate_doctor_capacity_from_data()
