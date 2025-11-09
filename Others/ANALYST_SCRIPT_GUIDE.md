# 🔍 ANALYST SCRIPT GUIDE
## Quick Reference for shift_analysis_analyst.py

---

## 📌 WHAT THIS SCRIPT DOES

This Python script performs comprehensive shift-aware analysis of your ER patient flow data:

1. **Loads & Validates** your `final_data.csv`
2. **Classifies visits** into shifts (Day: 7 AM-3 PM, Evening: 3 PM-11 PM, Night: 11 PM-7 AM)
3. **Detects bottlenecks** based on wait time thresholds
4. **Analyzes by shift:**
   - Doctor utilization % (are they busy enough?)
   - Throughput (patients per hour)
   - Wait times (mean, median, 75th percentile, 95th percentile)
   - Bottleneck distribution (where do problems concentrate?)
5. **Deep dives** into morning rush (7 AM-12 PM) - the critical constraint
6. **Generates visualizations** (4-panel chart comparing shifts)
7. **Creates analyst report** with all numbers ready for your video script

---

## 🚀 HOW TO RUN

### **Prerequisites**
```bash
pip install pandas numpy matplotlib seaborn
```

### **Execution**
```bash
# Make sure final_data.csv is in your current directory
python shift_analysis_analyst.py
```

### **What You'll See**
- Color-coded terminal output showing validation, calculations, and findings
- Progress indicators (✓ for match, ⚠ for variance, ✗ for errors)
- Section headers with analysis results

---

## 📊 OUTPUT FILES GENERATED

### **1. shift_analysis_visualization.png**
A 4-panel visualization showing:
- **Top Left:** Doctor utilization by shift (vs 75% target)
- **Top Right:** Bottleneck event distribution (pie chart)
- **Bottom Left:** Wait times comparison (mean vs 95th percentile)
- **Bottom Right:** Patient volume by shift

**Use for:** Presentation slides or supplementary material

### **2. shift_analysis_analyst_report.txt**
Comprehensive text report with:
- Executive summary
- Detailed shift breakdown (patients, doctors, utilization, wait times, bottlenecks)
- Morning rush deep dive
- Key points for video script (copy-paste ready!)
- Strategic recommendations

**Use for:** Video script numbers, exec summary drafting, team alignment

---

## 🎯 KEY METRICS EXTRACTED

The script validates these numbers from your data:

```
SHIFT METRICS:
├─ Day shift utilization: __% (vs projection 45%)
├─ Evening shift utilization: __% (vs projection 50%)
├─ Night shift utilization: __% (vs projection 55%)
├─ Day shift throughput: __ pph (vs projection 7.5)
├─ Evening shift throughput: __ pph (vs projection 6.8)
├─ Night shift throughput: __ pph (vs projection 5.2)
├─ Doctor counts by shift
├─ Wait times by shift (mean, median, 75th, 95th)
└─ Bottleneck distribution: __% day, __% evening, __% night

BOTTLENECK ANALYSIS:
├─ Total bottleneck events: ____
├─ Day shift: __% of total (____ events)
├─ Evening shift: __% of total (____ events)
├─ Night shift: __% of total (____ events)
└─ Morning rush (7 AM-12 PM) concentration: __% of day shift

MORNING RUSH SPECIFICS:
├─ Peak hour (worst): __:00
├─ Morning visits: ____
├─ Morning bottlenecks: ____
└─ Morning average wait: __ min
```

---

## ✅ DATA REQUIREMENTS

Your `final_data.csv` must have these columns:

| Column Name | Data Type | Example |
|---|---|---|
| `arrival_timestamp` | datetime/string | "2025-01-15 09:30:00" |
| `doctors_on_duty` | integer | 4 |
| `post_triage_wait_time` | float/integer | 42.5 |

**Optional but helpful:**
- `patient_id` - to track individual records
- `severity_level` - for stratified analysis
- `discharge_time` - for length-of-stay calculation

---

## 🔧 CUSTOMIZATION

You can modify these parameters in the script:

```python
# Line ~35: Adjust shift windows
if 7 <= hour < 15:  # Change 15 to shift your EVENING start
    return 'DAY'

# Line ~51: Adjust bottleneck threshold
wait_threshold_percentile=75  # Change 75 to use different cutoff

# Line ~26: Adjust tolerance for variance
TOLERANCE = 0.15  # ±15% variance - change to 0.10 for stricter checking

# Line ~23: Update projections if your estimates are different
PROJECTION = {
    'DAY': {'pph': 7.5, 'doctors': 4, 'util': 0.45, 'bottleneck_pct': 0.75},
    # Adjust these values ^
}
```

---

## 📋 INTERPRETING RESULTS

### **Utilization Scores**

```
🟢 GREEN (40-60%): Normal, room for growth
🟡 YELLOW (60-75%): Moderate, needs attention
🔴 RED (>75%): Overutilized, critical constraint
⚪ BLUE (>85%): Danger zone, service degradation
```

Your goal: Get all shifts to 75% utilization

### **Bottleneck Distribution**

```
Expected (from projections):
├─ Day: 75% (problem area)
├─ Evening: 20% (moderate)
└─ Night: 5% (acceptable)

If your data shows different %:
→ Use ACTUAL % in video (real data > projections)
→ Adjust solution prioritization accordingly
```

### **Wait Time Patterns**

```
If morning rush (7 AM-12 PM) is significantly worse:
→ Confirms critical constraint hypothesis
→ Supports "morning rush is the bottleneck" messaging

If wait times are similar across hours:
→ Problem may be systemic (not just morning)
→ May need to adjust analysis strategy
```

---

## 🎬 USING NUMBERS IN VIDEO SCRIPT

The report generates these copy-paste ready lines:

**For SCIENTIST segment (Revelation):**
```
"Seventy-five percent of {TOTAL_BOTTLENECKS} bottleneck events 
occurred during day shift morning rush, seven to noon.

Day shift has {DAY_UTIL}% utilization. Evening: {EVE_UTIL}%. 
Night: {NIGHT_UTIL}%.

The morning rush is our critical constraint."
```

**For CONSULTANT segment (Solution):**
```
"We prioritized day shift first because {DAY_PCT}% of inefficiency 
occurs during morning hours. This shift-aware approach ensures we 
solve the highest-impact problem immediately."
```

**For EXEC SUMMARY:**
```
"Root cause: Day shift morning rush (7 AM-12 PM) operates at {DAY_UTIL}% 
utilization, creating {DAY_BOTTLENECK_COUNT} bottleneck events 
({DAY_PCT}% of total). Average wait extends to {DAY_WAIT} minutes."
```

---

## ⚠️ TROUBLESHOOTING

### **"Script errors when loading final_data.csv"**
- Check file is in same directory as script
- Verify column names match exactly (case-sensitive)
- Try: `python3 shift_analysis_analyst.py`

### **"All values showing 0% utilization"**
- Your wait time data may be in different format (hours vs minutes?)
- Check if `post_triage_wait_time` column exists
- Try: `df.info()` to see data types

### **"Bottleneck % don't add up to 100%"**
- Normal! Shows % of bottleneck events per shift
- Confirms our assumption: ~75% in day, ~20% in evening, ~5% in night

### **"Numbers don't match our projections"**
- Use YOUR actual numbers (more credible to judges)
- Document the variance in your final report
- Example: "Our analysis shows 68% (vs projected 75%)"

---

## 📊 EXAMPLE OUTPUT

When you run the script, you'll see something like:

```
✓ Loaded final_data.csv (15,000 records)

📊 DATA VALIDATION
✓ All required columns present
✓ No null values found

📊 CLASSIFYING SHIFTS
  DAY: 5,012 records (33.4%)
  EVENING: 5,123 records (34.2%)
  NIGHT: 4,865 records (32.4%)

📊 BOTTLENECK ANALYSIS BY SHIFT
  Total bottleneck events: 2,179
  
  Bottleneck Distribution:
    DAY: 1,634 events (74.9% of total)
    EVENING: 437 events (20.0% of total)
    NIGHT: 108 events (5.0% of total)

📊 SHIFT UTILIZATION ANALYSIS
  DAY SHIFT:
    Doctors on duty: 4.0
    Patients: 5,012
    Utilization: 44.8% (vs 45.0% projected +0.2%)
    Throughput: 7.48 pph (vs 7.5 projected -0.3%)
    Avg wait: 48.2 min
    ...
```

---

## 🎯 NEXT STEPS AFTER RUNNING

1. **Review the .txt report** - save key numbers
2. **Check visualization.png** - look for obvious patterns
3. **Compare vs projections** - are we close? (±15% tolerance)
4. **Extract key talking points** - copy them into video script
5. **Brief your team** - share numbers, make sure everyone uses same figures
6. **Update presentation** - use actual data not estimates
7. **Practice recording** - read with new shift-aware numbers

---

## 💡 PRO TIPS

- **Run the script early** - gives you time to address data issues
- **Save outputs** - keep the PNG and TXT for reference during recording
- **Share report with team** - everyone should use same numbers
- **Document assumptions** - if you had to make adjustments, note them
- **Cross-reference** - verify numbers make sense (e.g., utilization % vs wait times)

---

## 📞 QUICK REFERENCE NUMBERS

After running, write down these for quick access:

```
MY ACTUAL NUMBERS:

Day shift utilization: ____%
Evening shift utilization: ____%
Night shift utilization: ____%

Day shift bottleneck %: ____%
Evening shift bottleneck %: ____%
Night shift bottleneck %: ____%

Total bottleneck events: _____
Day shift bottleneck events: _____

Morning rush (7 AM-12 PM) bottlenecks: _____
Morning rush average wait: _____ min

Day shift average wait: _____ min
Evening shift average wait: _____ min
Night shift average wait: _____ min
```

Keep these handy while recording! ✅

---

**You're ready. Run the script. Generate the numbers. Win the competition.** 🚀
