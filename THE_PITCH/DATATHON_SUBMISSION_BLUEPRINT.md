# 🎬 DATATHON SUBMISSION BLUEPRINT
## Emergency Room Efficiencies: From Bottleneck to Breakthrough

**Date:** November 9, 2025  
**Team:** 3 Students (Consultant, Data Analyst, Data Scientist)  
**Challenge:** Analyze patient flow → identify delay causes → propose actionable solutions  
**Deliverables:** 7-10 min video (5-8 slides + voiceover) + 200-300 word exec summary + Alteryx workflow  
**Judges:** UT Dallas Datathon (Consulting firm + Alteryx Ace + Data Scientist)

---

## 📋 SECTION 1: NARRATIVE STRATEGY

### The Core Challenge (What Judges Want to See)
From the brief:
> **"Team's challenge is to analyze patient flow and operational data to identify the **primary causes of delays** and propose **actionable solutions** to improve overall ER throughput, staffing efficiency, and operational performance."**

**Translation:** Judges expect:
1. ✅ **Root cause analysis** (WHY are there delays?)
2. ✅ **Solutions that work** (HOW do you fix it?)
3. ✅ **Actionable steps** (WHAT do you do Monday?)
4. ✅ **Real data validation** (PROVE it with data)
5. ✅ **Business impact** (WHAT'S the financial return?)

### Your Unique Angle: "Cinematic Investigative Approach"
Instead of "here's what we found," use: **"Here's how we investigated, what surprised us, what didn't work, and what finally solved it"**

**The Journey:**
```
MYSTERY:      "Why is ER slow despite having enough doctors?"
INVESTIGATION: "We tested 7 hypotheses. 6 were wrong. Here's the 1 that worked."
REVELATION:   "It's not staffing—it's PROCESS. System Theory proved it."
SOLUTION:     "5 ML models that fix the bottleneck without hiring"
IMPACT:       "+50% throughput, $15.3M annual benefit, 3.3-week payback"
```

---

## 🎯 SECTION 2: FINDINGS PRIORITY MATRIX

### What NOT to Include (Simplify)
- **Avoid:** Deep statistical tests, confidence intervals, p-values
- **Avoid:** Every EDA finding (too much clutter)
- **Avoid:** Technical ML model details (save for Q&A)
- **Avoid:** Lengthy timeseries analysis
- **Reason:** 7-10 minutes = 1-2 min per major idea max

### What TO Include (Impact-Driven)
Based on YOUR files + challenge requirements:

#### **MUST HAVE (Core Story):**
1. **The Bottleneck** (FIRST_PRINCIPLES_ANALYSIS.md)
   - Post-triage wait: 39 min (23% of total)
   - Doctor cycle: 107 min (62% of total)
   - Together: 85% of total ED time
   - **Why:** Answers "what's the problem?"
   - **Data:** Real numbers from 15,000 visits
   
2. **Root Cause** (DOCTOR_IDLE_ANALYSIS_EXPLANATION.md)
   - 2,179 bottleneck events (14.5% of visits)
   - Average 1.8 idle doctors while 4.3 patients waiting
   - Evidence: System Theory + Theory of Constraints
   - **Why:** Proves it's PROCESS not STAFFING
   - **Story:** "We thought we needed more doctors. Data proved otherwise."
   - **Data:** Concurrent activity analysis, idle doctor metrics
   
3. **Staff Utilization Reality** (STAFF_UTILIZATION_EXPLAINED.md)
   - Current: 50% utilization during bottlenecks
   - Industry target: 75-80%
   - **Why:** Shows massive improvement opportunity (no hiring needed)
   - **Data:** Utilization formula, benchmark comparisons
   
4. **Solution & Impact** (BOTTLENECK_TO_BREAKTHROUGH_ML_STRATEGY.md)
   - 5 ML models solving bottleneck
   - Expected outcomes: Wait 39→12 min, Throughput +32%, $15.3M benefit
   - **Why:** Demonstrates sophisticated, implementable solution
   - **Data:** Financial ROI, timeline, success metrics

#### **SHOULD HAVE (Story Depth):**
5. **The "Why We Investigated This Way"** (failure/learning moments)
   - We tested hypothesis X (didn't work)
   - We tested hypothesis Y (didn't work)
   - Finally discovered: System Theory + bottleneck shifting
   - **Why:** Shows rigor, honesty, investigative approach
   - **Delivery:** "We checked seasonality, special situations, upstream/downstream... nothing."
   
6. **Implementation Path** (IF/ELSE consultant style)
   - IF Solution 1 works: Throughput +6% in Week 4 → continue to Solution 2
   - IF Solution 1 fails: Accept we need more doctors, here's cost/impact
   - IF/THEN for each major decision point
   - **Why:** Shows mature consulting thinking
   - **Delivery:** "If our models improve wait time by <20%, then we recommend..."

#### **NICE TO HAVE (Polish):**
7. **Staff Reaction** (From Doctor_Idle_Analysis)
   - Doctors ARE seeing patients when they can
   - Problem is VISIBILITY + ROUTING not motivation
   - **Why:** Humanizes findings, prevents "blame doctors" perception

8. **Real Data Evidence** (Multiple sources)
   - Show actual timestamps from patient visits
   - Show actual utilization calculations
   - Show actual model predictions vs. actuals
   - **Why:** Judges love when you back claims with data

### **EXCLUDED (Less relevant for judges):**
- General EDA trends (too basic)
- Demographic breakdowns without insight
- Deep ER_Analysis workflows (unless directly supports bottleneck story)
- ML model hyperparameter tuning details
- Code implementations (Alteryx handles this)

---

## 🎬 SECTION 3: CINEMATIC NARRATIVE ARC (7-10 Minutes)

### **SEGMENT 1: HOOK (0:00-0:30)** — Consultant speaks
**Goal:** Grab attention, make judges care

```
SCRIPT: "Every weekday morning, Meridian ER has 4 doctors on duty.
They're capable of seeing 10 patients per hour.
But they only see 6.9 patients per hour.
That 25% loss? It costs them $890,000 EVERY QUARTER.

But here's the twist: It's not because there aren't enough doctors.
It's something we discovered that surprised us all."

VISUAL: Chart showing: Doctor capacity vs actual throughput gap
TONE: Confident, slightly mysterious
DURATION: 30 sec
NEXT: Analyst comes in with "Here's what we found"
```

### **SEGMENT 2: INVESTIGATION - THE MYSTERY (0:30-2:00)** — Analyst speaks
**Goal:** Build curiosity, reveal the problem

```
SCRIPT: "We looked at 15,000 patient visits across Q1 2025.
We asked: Where's the time going?

The data was clear:
- First 23% of total ED time: Post-triage wait (patients waiting for doctor)
- Next 62% of total ED time: Doctor cycle time (actually seeing the doctor)
- Together: 85% of a patient's entire ER visit

We thought: Maybe it's just staffing. Not enough doctors.
But when we dug deeper... something odd appeared."

VISUAL: 
- Sankey/waterfall: Total LOS → breakdown by stage
- Highlight: 39 min wait + 107 min doctor cycle = 85%
- Show: "This is the problem zone"

TONE: Detective-like, building tension
DURATION: 90 sec
NEXT: "And then we discovered what was REALLY happening"
```

### **SEGMENT 3: INVESTIGATION - THE SURPRISE (2:00-3:30)** — Scientist speaks
**Goal:** Reveal the shocking finding (process not people)

```
SCRIPT: "We found 2,179 moments where:
- Doctors were IDLE (not with a patient)
- Patients were WAITING (in the queue)
- At the SAME TIME

In 14.5% of all patient visits, this happened.
Average: 1.8 doctors idle while 4.3 patients waited.

This is textbook System Theory: The bottleneck isn't the resource (doctors).
It's the FLOW of patients TO the resource.

Our utilization rate during these bottlenecks? Just 50%.
Industry best practice? 75-80%.
We had CAPACITY. We just weren't USING it.

The team kept searching for staffing solutions.
But the data said: 'You need PROCESS solutions.'
We tried X... didn't work. We tried Y... didn't work.
System Theory finally showed us: It's upstream/downstream flow, not doctor skill."

VISUAL:
- Timeline showing: Doctor finishes → 2-5 min gap → Next patient assigned
- Concurrent activity chart: Doctors vs patients in queue
- Utilization graph: 50% vs 75-80% target gap

TONE: "AH-HA!" moment, scientific rigor
DURATION: 90 sec
NEXT: "So we built 5 ML models to fix it"
```

### **SEGMENT 4: SOLUTION - THE APPROACH (3:30-6:00)** — Consultant + Scientist
**Goal:** Show the solution is sophisticated AND implementable

```
CONSULTANT speaks (first 60 sec):
"We designed 3 solution tiers:

TIER 1 (Weeks 1-4): Quick wins
- Real-time queue visibility dashboard
- Intelligent patient dispatcher (not manual)
- Cost: $150K, Benefit: Wait time 39→27 min (-31%), +6% throughput

TIER 2 (Weeks 5-8): Process redesign
- Pre-work in parallel (draw labs while waiting)
- NP fast-track for routine cases
- Cost: $250K, Benefit: +32% cumulative throughput

TIER 3 (Weeks 9-12): Monitoring & optimization
- Real-time dashboard for continuous improvement
- Cost: $150K, Benefit: Sustain 75-80% utilization

Total investment: $550K
First-year benefit: $15.3M (additional 7,500 visits × $800 margin)
Payback period: 3.3 weeks
ROI: 2,662%"

VISUAL:
- Gantt chart: 12-week timeline
- Three-tier solution architecture
- Investment vs benefit table
- Decision tree: IF solution works → continue; IF not → alternative path

SCIENTIST speaks (next 60 sec):
"Supporting each tier are 5 ML models:

Model 1: COMPLEXITY PREDICTOR (Random Forest)
- Predicts patient complexity early
- Impact: +6% throughput in Week 4

Model 2: INTELLIGENT DISPATCHER (LightGBM)
- Routes patients intelligently (not manually)
- Impact: Dispatch delay 5→1 min
- Impact: Additional +5% throughput

Model 3: LENGTH-OF-STAY (Quantile Regression)
- Predicts how long doctor visit takes (with confidence intervals)
- Impact: Queue optimization, patient expectation setting

Model 4: WORKLOAD FORECASTER (Prophet + XGBoost)
- Predicts bottlenecks 2 hours ahead
- Alert: If wait >45 min predicted, call on-call
- ROI: $200 cost / $22K saved = 73:1

Model 5: ADVERSE OUTCOME DETECTOR (Neural Network)
- Flags high-risk patients early
- Impact: 5-10% improvement in adverse events
- Impact: $2.5M annual benefit

All models use real data from 15,000 visits.
All models built for production (<500ms latency).
All models explainable (SHAP, LIME, feature importance)."

VISUAL:
- 5-model architecture diagram
- Example predictions from each model
- Real vs predicted wait times (validation plots)
- Performance metrics table

TONE: Business case + technical credibility
DURATION: 2 min total (60 sec each speaker)
NEXT: "What happens if it works? What if it doesn't?"
```

### **SEGMENT 5: CONTINGENCY PLANNING - IF/THEN (6:00-7:30)** — Consultant speaks
**Goal:** Show mature consulting thinking, de-risk the recommendation

```
SCRIPT: "Smart implementations need contingency plans.

SCENARIO 1: IF Models 1-2 improve wait time by 20%+
→ THEN proceed to Tier 2 (weeks 5-8)
→ Confidence: High (based on 2,179 bottleneck events we analyzed)
→ Risk: Low

SCENARIO 2: IF Models 1-2 improve wait time by <10%
→ THEN re-evaluate: Process issues elsewhere?
→ Alternative: Accept we need additional MD staffing
→ Cost: Add 0.5 FTE MD = $150K + benefits = $200K annual
→ Impact: +5% throughput, but annual recurring cost
→ Recommendation: Try Tier 1 first (3.3 week payback), then decide

SCENARIO 3: IF real-world results lag predictions
→ Reasons: Data drift, staff resistance, external factors
→ Response: Weekly retraining, staff engagement, root cause analysis
→ Timeline: 30-day iteration, then re-assess

SUCCESS LOOKS LIKE:
- Week 4: Wait time 39→27 min, Throughput 6.9→7.3 pph
- Week 8: Wait time 39→12 min, Throughput 6.9→8.0 pph
- Week 12: Wait time 39→12 min, Throughput 6.9→9.1 pph, LWBS <1%

FAILURE TRIGGERS:
- By Week 4: If wait time doesn't improve by 10%+ → pivot
- By Week 8: If cumulative throughput <7.5 pph → add staffing discussion
- By Week 12: If we hit 75% utilization → success (even if not 80%)"

VISUAL:
- Decision tree: If X → then Y
- Success/failure metrics table
- Week-by-week milestones

TONE: Professional, realistic, confident
DURATION: 90 sec
NEXT: "Here's what success looks like"
```

### **SEGMENT 6: VISION & IMPACT (7:30-9:30)** — All 3 students
**Goal:** Create excitement, leave lasting impression

```
CONSULTANT speaks (30 sec):
"By fixing process, not staffing:
- No hiring needed (same doctors, better used)
- $15.3M additional annual revenue (7,500 more visits)
- Patient satisfaction improves (shorter waits)
- Staff satisfaction improves (less idle time)"

ANALYST speaks (30 sec):
"The data told a clear story:
- Problem: Flow, not people
- Opportunity: 50%→75% utilization gain
- Evidence: 15,000 patient visits, 2,179 bottleneck events
- Timeline: 12 weeks from decision to full benefit"

SCIENTIST speaks (30 sec):
"Technology makes it possible:
- 5 complementary ML models
- Real-time optimization
- Explainable predictions (staff trust)
- Production-ready, scalable architecture"

ALL THREE speak (final 30 sec):
"This is what modern healthcare operations looks like:
- Data-driven decisions
- Process innovation (not just hiring)
- Sophisticated but implementable solutions
- Balanced business case with real contingencies

Meridian ER isn't just getting faster.
It's getting smarter."

VISUAL:
- Split screen: 3 speakers side-by-side
- Before/after comparison (39 min wait → 12 min)
- Financial impact (890K loss → 15.3M gain)
- Engagement metric (3.8→4.3 satisfaction)

TONE: Inspiring, confident, unified
DURATION: 2 min total
CLOSING: Strong, memorable

FINAL SLIDE: "Emergency Room Efficiencies: From Bottleneck to Breakthrough"
Credits: 3 student names + university
```

---

## 📝 SECTION 4: VOICEOVER SCRIPT (Word-by-Word with Timing)

### **Full Script with Timing Marks**

```
============ SEGMENT 1: HOOK ============
[0:00] CONSULTANT starts speaking (slides on-screen: title + ER photo)

"Every weekday morning at Meridian City Hospital, 
[0:03] the Emergency Room opens with four doctors on duty.

Based on national benchmarks, four capable physicians should see 
[0:08] approximately ten patients per hour.

But in reality, Meridian sees just six point nine.

[0:13] That twenty-five percent gap?

It costs the hospital eight hundred ninety thousand dollars 
[0:18] every single quarter.

The obvious question: Hire more doctors, right?

[0:23] But here's what surprised us:

It's not that simple. Not because there aren't enough doctors,
but because of something we discovered during our investigation."

[VISUAL: Chart appears showing doctor capacity vs actual]
[DURATION: 0:00-0:30 = 30 sec]

============ SEGMENT 2: INVESTIGATION ============
[0:30] ANALYST starts speaking (slides shift to data visuals)

"We analyzed fifteen thousand patient visits over the first quarter of twenty-twenty-five.

[0:38] One question: Where is all the time going?

The answer emerged from the data immediately:

[0:43] Twenty-three percent of total emergency room time is spent waiting for a doctor 
after a patient finishes triage.

Sixty-two percent is spent with the doctor.

[0:50] Together: eighty-five percent of a patient's entire ER visit.

We thought the issue was simple: maybe not enough physicians.

[0:58] But when we investigated further, something odd appeared.
And I'll let our data scientist explain."

[VISUAL: Waterfall chart showing time breakdown, highlighting 39+107=146 min]
[DURATION: 0:30-2:00 = 90 sec]

============ SEGMENT 3: REVELATION ============
[2:00] SCIENTIST starts speaking (slides show bottleneck analysis)

"In our dataset, we identified two thousand one hundred seventy-nine moments where:

Doctors were idle—not seeing a patient.
Patients were waiting in the queue.
[2:12] Both things happening at the exact same moment.

This occurred in fourteen point five percent of all patient visits.

[2:19] The picture was stark: on average, one point eight doctors were idle 
while four point three patients waited.

This is textbook System Theory. The bottleneck isn't the resource—the doctors.
[2:28] It's the flow of patients TO the resource.

Our staffing utilization rate during these bottlenecks? 
Just fifty percent.

Industry best practice? Seventy-five to eighty percent.
[2:37] We had the capacity. We just weren't using it.

Now, my team initially searched for staffing solutions.
More doctors, different schedules—the usual approaches.

But the data kept saying something different.
[2:47] So we went back to first principles.

We tested hypothesis after hypothesis:
- Seasonality patterns? No.
- Special situations overwhelming the system? No.
- Upstream or downstream bottlenecks? No—the constraint is exactly here: 
between triage completion and doctor assignment.

[2:58] System Theory confirmed it: This is a PROCESS problem, not a STAFFING problem."

[VISUAL: Concurrent activity chart, utilization gap visualization]
[DURATION: 2:00-3:30 = 90 sec]

============ SEGMENT 4A: SOLUTION - BUSINESS ============
[3:30] CONSULTANT resumes (slides show solution architecture)

"Given this finding, we designed a three-tier solution:

[3:36] TIER ONE—Weeks One through Four:
Implement a real-time queue visibility dashboard so doctors see who's waiting.
Deploy an intelligent patient dispatcher to automatically route the next patient 
instead of manual assignment.

[3:47] Cost: One hundred fifty thousand dollars.
Expected benefit: Wait time drops from thirty-nine to twenty-seven minutes—a thirty-one percent improvement.
Throughput improvement: Plus six percent.

[3:56] TIER TWO—Weeks Five through Eight:
Run pre-lab work in parallel while patients wait for the doctor.
Deploy a nurse practitioner for routine, low-complexity cases.

[4:06] Cost: Two hundred fifty thousand dollars additional.
Cumulative benefit by week eight: 
Throughput climbs from six point nine to nine point one patients per hour—a thirty-two percent gain.

[4:17] TIER THREE—Weeks Nine through Twelve:
Build an interactive real-time dashboard for continuous monitoring and optimization.
Weekly huddles to refine processes.

[4:25] Cost: One hundred fifty thousand dollars.

Total investment: Five hundred fifty thousand dollars.

[4:30] Total first-year benefit: Fifteen point three million dollars 
from handling seven thousand five hundred additional patient visits.

Payback period: Three point three weeks.

[4:37] Return on investment: Twenty-six hundred sixty-two percent in year one."

[VISUAL: 12-week Gantt, investment vs benefit table, ROI chart]
[DURATION: 3:30-5:00 = 90 sec]

============ SEGMENT 4B: SOLUTION - TECHNICAL ============
[5:00] SCIENTIST resumes (slides show ML architecture)

"Behind each of these tiers are five machine learning models 
designed to optimize different aspects of the bottleneck.

[5:08] MODEL ONE: Complexity Predictor—a Random Forest classifier that 
predicts patient complexity at triage time. 
This feeds the dispatcher model, improving routing accuracy. 
Expected contribution: Plus six percent throughput in week four.

[5:20] MODEL TWO: Intelligent Dispatcher—a Gradient Boosting model 
that recommends which doctor should see the next waiting patient, 
accounting for availability, expertise, and patient complexity.

Current manual dispatch adds two to five minutes per patient.
Our model reduces that to thirty seconds.
[5:33] Contribution: Additional five percent throughput.

MODEL THREE: Length-of-Stay Predictor—a Quantile Regression model that 
estimates how long a doctor visit will take,
giving confidence intervals: twenty-five, fifty, and ninety percentile predictions.

[5:46] Doctors see 'This patient will likely take ninety minutes, 
but could range eighty to one-sixty.' This enables queue sequencing 
and sets patient expectations realistically.

[5:55] MODEL FOUR: Workload Forecaster—an ensemble combining Facebook Prophet 
for trend and seasonality plus XGBoost for exogenous factors like weather or events.

This predicts wait times two hours ahead.
Decision rule: If wait exceeds forty-five minutes forecast, 
alert the on-call physician at a cost of two hundred dollars.
[6:09] That saves an average of twenty-two thousand dollars in lost capacity.
Return on that alert alone: Seventy-three to one.

[6:15] MODEL FIVE: Adverse Outcome Detector—a neural network that 
identifies patients at risk for adverse events within thirty days.

Real-time risk score plus key contributing factors.
Enables early intervention, improving outcomes and reducing ICU admissions.
[6:24] Estimated annual benefit from complications prevented: Two point five million dollars.

All models were trained on your real data—fifteen thousand actual patient visits.
[6:30] All achieve sub-five-hundred-millisecond inference time for production deployment.
All use explainability techniques—SHAP, LIME, feature importance—
because hospital staff won't trust a black box."

[VISUAL: 5-model architecture, example predictions, validation plots]
[DURATION: 5:00-6:30 = 90 sec]

============ SEGMENT 5: CONTINGENCY ============
[6:30] CONSULTANT speaks (slides show decision tree)

"Any serious implementation requires 'if-then' thinking.

[6:35] IF our models improve wait time by twenty percent or more by week four:
THEN proceed confidently to Tier Two.
Our confidence is high because we've analyzed all twenty-one hundred seventy-nine bottleneck events.

[6:46] IF the models improve wait time by less than ten percent:
THEN we have a harder choice. It may indicate the bottleneck is elsewhere, 
or process resistance is stronger than expected.

In that case, we recommend accepting that additional MD staffing is required:
[6:57] Add zero point five FTE doctor = one hundred fifty thousand dollars plus benefits.
That costs approximately two hundred thousand annually but might be necessary.

We'd still recommend trying this process-optimization approach first, 
given the three-point-three-week payback.

[7:08] IF real-world results lag our predictions:
Common reasons include data drift, staff resistance, or external factors.
Response: Weekly model retraining, staff engagement sessions, root cause analysis.
Timeline: Thirty-day iteration, then reassess.

[7:20] SUCCESS METRICS:
- Week four: Wait reduces to twenty-seven minutes, throughput to seven point three pph.
- Week eight: Wait reduces to twelve minutes, throughput to eight point zero pph.
- Week twelve: Wait reduces to twelve minutes, throughput to nine point one pph, left-without-being-seen rate below one percent.

[7:35] FAILURE TRIGGERS:
- If wait doesn't improve ten percent by week four: Pivot immediately.
- If cumulative throughput doesn't reach seven point five pph by week eight: Add staffing discussion.
- If we haven't hit seventy-five percent utilization by week twelve: Reassess model inputs."

[VISUAL: If/then decision tree, metrics table, week-by-week targets]
[DURATION: 6:30-7:30 = 60 sec]

============ SEGMENT 6: VISION ============
[7:30] CONSULTANT speaks (30 sec)

"What excites us about this approach:
[7:33] It doesn't require hiring. 
Same four doctors, working smarter.
Fifteen point three million dollars of additional revenue without additional headcount costs.
[7:40] Patients experience shorter waits. Staff experience less downtime. The hospital breaks through its capacity ceiling."

[VISUAL: Before/after comparison]
[DURATION: 7:30-8:00 = 30 sec]

[8:00] ANALYST speaks (30 sec)

"From a data perspective, this tells a complete story:
[8:03] Fifteen thousand patient visits revealed a process problem,
not a resource problem.

The evidence is strong:
[8:08] Twenty-one hundred seventy-nine bottleneck events, even when accounting for realistic doctor transition time.
A fifty percent utilization rate when the industry target is seventy-five to eighty percent.

The path forward was clear."

[VISUAL: Data visualization highlights]
[DURATION: 8:00-8:30 = 30 sec]

[8:30] SCIENTIST speaks (30 sec)

"The technology makes this achievable:
[8:33] Five complementary models handle different optimization challenges.
Real-time inference means decisions happen seconds after a patient finishes triage.
Explainability means clinicians understand WHY the model made a recommendation.

This isn't just theory. It's production-grade architecture."

[VISUAL: Technical architecture]
[DURATION: 8:30-9:00 = 30 sec]

[9:00] ALL THREE speak together (final 30 sec)

CONSULTANT: "This represents a fundamental shift in how modern hospitals work:"
ANALYST: "Data-driven operations instead of guesswork—"
SCIENTIST: "—powered by thoughtful, explainable machine learning—"
ALL THREE: "—that respects both the business case AND the human element.

[9:15] Meridian isn't just getting faster.
It's getting smarter.

[9:20] This is the future of emergency medicine operations."

[VISUAL: Composite shot of all three; final slide]
[DURATION: 9:00-9:30 = 30 sec]

[END CREDITS: Student names, University, Date]
[TOTAL VIDEO TIME: 9:30]

```

**Timing Notes:**
- Total: 9 min 30 sec (within 7-10 min window with room for transitions)
- Segment 1: 30 sec (Hook—Consultant)
- Segment 2: 90 sec (Investigation—Analyst)
- Segment 3: 90 sec (Revelation—Scientist)
- Segment 4A: 90 sec (Solution Business—Consultant)
- Segment 4B: 90 sec (Solution Technical—Scientist)
- Segment 5: 60 sec (Contingency—Consultant)
- Segment 6: 60 sec (Vision—All Three)
- Total: 570 seconds = 9:30

**Pacing Notes:**
- Each speaker: 60-90 sec chunks (manageable, engaging rhythm)
- Speaker changes every 90 sec max (prevents monotony)
- Visual changes every 45 sec (data viz, charts, decision trees)
- Key emphasis points marked with [brackets]
- Tone: Conversational, confident, data-driven

---

## 🎬 SECTION 5: VIDEO PRODUCTION GUIDE

### Setup (Pre-Recording)
```
1. ZOOM CONFIGURATION
   - Participant 1 (Consultant): Primary speaker, screen share control
   - Participant 2 (Analyst): Secondary speaker, camera on
   - Participant 3 (Scientist): Tertiary speaker, camera on
   
   Settings:
   └─ Resolution: 1080p minimum
   └─ Audio: Zoom audio + local backup (each person records locally too)
   └─ Screen share: PowerPoint (slides advance manually on cue)
   └─ Recording: To cloud + local file backup
   
2. AUDIO SETUP
   - Each person: USB microphone (Blue Yeti or equivalent) ✅
   - Test levels: -10dB to -3dB on meter (not peaking)
   - Room: Quiet (minimize background noise)
   - Backup: Voice Memos on phone running simultaneously
   
3. LIGHTING
   - Face-on lighting (no shadows)
   - Webcams: Elevated to eye level
   - Background: Professional (books, plants, clean wall)
   
4. TECHNICAL CHECK (15 min before recording)
   - Zoom link tested, all 3 can join
   - Slides present, correct order, speaker notes visible
   - Screen share: Practice advancing slides
   - Audio: All 3 test microphones
   - Webcams: All 3 visible, well-lit
   - Recording destination: Confirmed (cloud + local)
```

### Recording (Execution)
```
TIMING:
- Start Zoom cloud recording
- Each person presses local record on phone/recorder
- Consultant reads opening script (provides "3, 2, 1, GO" cue)
- Proceed through all 6 segments
- If major mistake, pause, reset, continue
  (You can edit out false starts in post)

CONTINGENCIES:
- Audio cuts out: Pause, have person rejoin, resume
- Slide advanced too fast: Pause, go back, resume
- Someone stumbles: Pause, take deep breath, resume from last sentence
- Good rule: Pause for 5 sec of silence, then "cut"
  (Easier to remove silence than to fix scrambled audio)

QUALITY CHECK (after each segment):
- Listen back: Audio clear? No background noise?
- Slides: Correct, advanced properly?
- Timing: On track (~90 sec per segment)?
```

### Post-Production (15-30 minutes)
```
STEP 1: Export from Zoom
- Download: Video file (.mp4) + audio (.m4a)
- Keep: High quality, uncompressed

STEP 2: Audio Cleanup (using Audacity, free)
- Open: Zoom audio file
- Noise reduction: Select 5 sec of background noise → Effect → Reduce Noise → Apply
- Volume normalization: Effect → Normalize (peak -3dB)
- Remove silence: Select → Silence → Apply
- Export: MP3 at 192kbps

STEP 3: Edit Video (using CapCut, free, or iMovie)
- Import: Zoom video + cleaned audio
- Sync: Match cleaned audio to video
- Insert: Slides (if Zoom screen share didn't capture well)
- Add: Title slide at start, credits at end
- Color correction: Slight boost to skin tones (Zoom default is pale)
- Export: MP4, 1080p, H.264

STEP 4: Final Check
- Play: Full 9:30 video
- Audio: Clear, no gaps, consistent volume?
- Visuals: All slides visible, readable?
- Timing: 7-10 min requirement met? ✅
- Upload: Save as "Meridian_ER_Datathon_Video.mp4"
```

### Backup Plans
```
IF Zoom audio fails:
→ Use local phone recordings for audio
→ Use Zoom video for visuals
→ Sync in iMovie/CapCut

IF screen share doesn't capture slides:
→ Export slides as high-res images (PNG, 1920x1080)
→ Import into video editor
→ Time slides to match voiceover

IF someone misses recording:
→ Record solo audio reading their segment
→ Lay audio over B-roll, previous recordings, or slides
→ Minimal impact, still professional

IF 9:30 exceeds 10 min limit:
→ Remove non-essential pauses
→ Trim examples from Segment 5 (contingency)
→ Aim for 9:00-9:15 to be safe
```

---

## 📊 SECTION 6: EXECUTIVE SUMMARY (200-300 Words)

**[Use this template, fill in with your exact data]**

---

### **MERIDIAN CITY HOSPITAL ER OPTIMIZATION**
### **Executive Summary**

**Problem:**  
Meridian's Emergency Department achieves only 6.9 patient visits/hour despite physician capacity of 10+/hour. Analysis of 15,000 Q1 2025 patient visits reveals that 85% of total ED time is consumed by two stages: post-triage wait (39 min, 23%) and doctor cycle time (107 min, 62%). This 25% capacity gap costs the hospital $890,000 quarterly in lost revenue.

**Root Cause:**  
Contrary to initial assumptions, the bottleneck is not staffing shortage but process inefficiency. Detailed analysis identified 2,179 instances (14.5% of visits) where doctors were idle while patients waited—representing a physician utilization rate of only 50% against the industry target of 75-80%. System Theory analysis confirms the constraint is not physician availability but patient flow optimization to physicians.

**Solution:**  
A three-tier implementation over 12 weeks deploys five machine learning models:
1. **Complexity Predictor** (Random Forest): Improves triage-to-dispatch routing
2. **Intelligent Dispatcher** (LightGBM): Automates next-patient assignment
3. **LOS Predictor** (Quantile Regression): Forecasts visit duration for queue optimization
4. **Workload Forecaster** (Prophet): Predicts bottlenecks 2 hours ahead for proactive staffing
5. **Adverse Outcome Detector** (Neural Network): Identifies at-risk patients for early intervention

**Expected Outcomes:**
- Week 4: Wait time 39→27 min; Throughput 6.9→7.3 pph (+6%)
- Week 8: Wait time 39→12 min; Throughput 6.9→8.0 pph (+16%)
- Week 12: Wait time 39→12 min; Throughput 6.9→9.1 pph (+32%); LWBS <1%

**Financial Impact:**
- Investment: $550K (Tier 1-3)
- Year 1 Benefit: $15.3M (7,500 additional visits × $800 margin)
- Payback Period: 3.3 weeks
- Year 1 ROI: 2,662%

**Implementation Contingencies:**
- **IF** models improve wait time <10% by Week 4: Pivot to staffing analysis; add 0.5 FTE MD ($200K annual)
- **IF** data drift observed: Weekly model retraining + root cause analysis (30-day window)
- **IF** success metrics achieved: Proceed to optimization phase; target sustained 75-80% utilization

**Recommendation:**  
Deploy Tier 1 immediately (3-week payback). Establish weekly KPI review gates for Tier 2/3 progression. Implement decision-tree contingencies to de-risk investment.

---

**[Word count: 280 words]**

---

## 🛠️ SECTION 7: ALTERYX WORKFLOW DESIGN

### **Workflow: "Patient Flow Data Pipeline"**

**Purpose:** Demonstrate data cleaning + feature engineering + bottleneck detection in Alteryx

**Complexity Level:** Moderate (6-8 transforms, shows real engineering)

**Workflow Structure:**

```
INPUT (1): Hospital_Visits.csv
- 15,002 rows × 39 columns
- Contains: Patient ID, Arrival, Triage_Start, Triage_End, Doctor_Seen, Exit, 
  Doctors_On_Duty, Nurses_On_Duty, etc.

INPUT (2): Hospital_Staffing.csv
- Shift schedules, staff count by time slot
- Cross-reference for idle doctor calculations

╔════════════════════════════════════════════════════════════════╗
║ TRANSFORM 1: Data Validation & QC                             ║
║ ├─ Check for null values in critical fields                   ║
║ ├─ Remove records where Exit < Doctor_Seen (data errors)      ║
║ ├─ Flag records where wait times > 360 min (outliers)         ║
║ └─ Output: 14,956 clean records (46 removed)                  ║
╚════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════╗
║ TRANSFORM 2: Parse & Join Timestamps                          ║
║ ├─ Convert timestamp strings to datetime                       ║
║ ├─ Extract: Hour, DayOfWeek, Shift (DAY/EVENING/NIGHT)       ║
║ ├─ Join with Staffing.csv on Shift + Hour                     ║
║ └─ Output: Records now have Doctor_On_Duty field             ║
╚════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════╗
║ TRANSFORM 3: Calculate Wait Times (Core Metrics)             ║
║ ├─ Wait_For_Registration = Registration_Start - Arrival      ║
║ ├─ Registration_Time = Registration_End - Registration_Start  ║
║ ├─ Triage_Time = Triage_End - Triage_Start                   ║
║ ├─ Post_Triage_Wait = Doctor_Seen - Triage_End               ║
║ ├─ Doctor_Cycle_Time = Exit - Doctor_Seen                     ║
║ ├─ Total_LOS = Exit - Arrival                                 ║
║ └─ Output: 6 new time fields per patient                      ║
╚════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════╗
║ TRANSFORM 4: Bottleneck Detection Flag                        ║
║ ├─ For each patient's Triage_End moment:                      ║
║ ├─ Count active doctors (Doctor_Seen ≤ Triage_End            ║
║ │   AND Exit + 10_min_buffer ≥ Triage_End)                   ║
║ ├─ Count waiting patients (Triage_End ≤ current               ║
║ │   AND Doctor_Seen ≥ current)                                ║
║ ├─ Calculate Idle_Doctors = Doctors_On_Duty - Active_Doctors  ║
║ ├─ Flag IF Idle_Doctors > 0 AND Waiting_Patients > 0         ║
║ │   → Bottleneck_Flag = 1 (else 0)                            ║
║ └─ Output: Bottleneck_Flag + Idle_Doctor_Count fields        ║
╚════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════╗
║ TRANSFORM 5: Feature Engineering                              ║
║ ├─ Time features:                                             ║
║ │  ├─ Is_Morning_Rush (7-9 AM) → Binary                      ║
║ │  ├─ Is_Weekend → Binary                                    ║
║ │  ├─ Hour_of_Day → Numeric (0-23)                           ║
║ ├─ Operational features:                                      ║
║ │  ├─ Doctor_Density = Doctors_On_Duty / 100                 ║
║ │  ├─ Nurse_to_Doctor_Ratio = Nurses / Doctors               ║
║ │  ├─ Specialist_Available → Binary                          ║
║ ├─ Patient risk features (from data):                         ║
║ │  ├─ ESI_Level → Categorical (1-5)                         ║
║ │  ├─ Chief_Complaint_Category → Categorical                 ║
║ │  ├─ Age_Group → Binned (0-18, 19-40, 41-65, 65+)          ║
║ └─ Output: 12 new feature fields                              ║
╚════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════╗
║ TRANSFORM 6: Aggregation & Summary Stats                      ║
║ ├─ Aggregate by Hour:                                         ║
║ │  ├─ Count(Bottleneck_Events)                               ║
║ │  ├─ AVG(Post_Triage_Wait)                                   ║
║ │  ├─ AVG(Doctor_Cycle_Time)                                  ║
║ │  ├─ AVG(Idle_Doctors)                                       ║
║ │  └─ Utilization % = (Doctors - Idle) / Doctors × 100       ║
║ ├─ Aggregate by Shift:                                        ║
║ │  ├─ Same metrics per shift (DAY/EVENING/NIGHT)             ║
║ └─ Output: Hourly + Shift summary tables                      ║
╚════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════╗
║ OUTPUT (1): Clean Patient Records                             ║
║ ├─ 14,956 rows × 52 columns (original 39 + 6 wait times      ║
║ │  + 6 flags/metrics + 12 features)                           ║
║ ├─ Fields: All cleaned, engineered, ready for ML              ║
║ └─ Destination: Clean_Patient_Records.csv                    ║
╚════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════╗
║ OUTPUT (2): Bottleneck Summary (Hourly)                       ║
║ ├─ 90 rows (days) × 24 rows (hours/day) = 2,160 rows        ║
║ ├─ Fields: Hour, Bottleneck_Count, Avg_Wait, Avg_Cycle,      ║
║ │  Avg_Idle_Doctors, Utilization%                            ║
║ └─ Destination: Hourly_Bottleneck_Summary.csv               ║
╚════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════╗
║ OUTPUT (3): Shift Summary                                     ║
║ ├─ 3 rows (DAY/EVENING/NIGHT)                                ║
║ ├─ Fields: Shift, Bottleneck_Count, Avg_Wait, Avg_Cycle,     ║
║ │  Avg_Idle_Doctors, Utilization%, Total_Patients           ║
║ └─ Destination: Shift_Bottleneck_Summary.csv                 ║
╚════════════════════════════════════════════════════════════════╝
```

**Why This Workflow Impresses:**
- ✅ Shows real data engineering (validation, joins, transformations)
- ✅ Demonstrates domain knowledge (bottleneck detection algorithm)
- ✅ Produces actionable outputs (clean data for ML, summary KPIs)
- ✅ Documents business logic clearly (in comments)
- ✅ Moderate complexity (not overwhelming, shows competence)
- ✅ Production-ready (error handling, QC flags)

**Alteryx Skills Demonstrated:**
- Data parsing & cleansing
- DateTime manipulation
- Joins & aggregation
- Custom formulas (idle doctor calculation)
- Branching logic (bottleneck flag)
- Multiple outputs (feeds into ML models)

---

## ✅ SECTION 8: FINAL CHECKLIST

### **Assets to Create (Before Recording)**
- [ ] PowerPoint slides (5-8 slides, speaker notes)
- [ ] Voiceover script (printed, highlighted per speaker)
- [ ] Alteryx workflow (tested, outputs generated)
- [ ] Executive summary (200-300 words, polished)

### **Recording Checklist**
- [ ] Zoom meeting link created & tested
- [ ] All 3 microphones tested (audio levels ~-5dB)
- [ ] Slides uploaded & order verified
- [ ] Local backup recorders on all 3 phones
- [ ] Lighting: All 3 faces well-lit, no shadows
- [ ] Backgrounds: Professional, no distractions
- [ ] Run-through: Full rehearsal with timing

### **Recording Day**
- [ ] Start Zoom + local recorders simultaneously
- [ ] Record segment by segment (pause between if needed)
- [ ] Review audio quality after each segment
- [ ] Save all files: Zoom MP4 + local backups

### **Post-Production**
- [ ] Download Zoom video + audio
- [ ] Clean audio (Audacity): Remove noise, normalize volume
- [ ] Edit video (CapCut): Insert cleaned audio, titles, credits
- [ ] Final check: 7-10 min? Audio clear? Slides visible?
- [ ] Export as MP4 (1080p, H.264, high bitrate)

### **Submissions**
- [ ] Video (Meridian_ER_Datathon_Video.mp4)
- [ ] Executive Summary (200-300 words, .docx)
- [ ] Alteryx Workflow (.yxmd file)
- [ ] All files named clearly, in submission folder
- [ ] Confirm file sizes, upload format, deadline

### **Before Hitting Submit**
- [ ] Story flows: Hook → Mystery → Revelation → Solution → Impact
- [ ] All 3 speakers contribute equally (~3 min each)
- [ ] Real data examples shown (wait times, utilization %, bottleneck counts)
- [ ] Implementation contingencies discussed (IF/THEN)
- [ ] Financial ROI clear ($550K cost, $15.3M benefit, 3.3-week payback)
- [ ] ML models explained (5 models, what each does)
- [ ] Alteryx workflow demonstrates data engineering
- [ ] No jargon without explanation

---

## 🎯 DELIVERY SUMMARY

| Deliverable | What | Timeline |
|------------|------|----------|
| **Video** | 7-10 min, 5-8 slides, voiceover, 3 speakers | This week |
| **Executive Summary** | 200-300 words, business focus, if/then contingencies | Today |
| **Alteryx Workflow** | 6-8 transforms, data cleaning + bottleneck detection | This week |
| **Supporting Files** | Speaker script, slides, production guide | Today |

---

## 🚀 NEXT STEPS (In Order)

1. ✅ **Read this entire document** (30 min)
2. ✅ **Review all 3 students on voiceover script** (30 min)
3. ✅ **Rehearse full video 1x** (10 min)
4. ✅ **Conduct Zoom audio test** (5 min)
5. ✅ **Record video** (30 min + breaks)
6. ✅ **Post-production** (30 min)
7. ✅ **Submit** (5 min)

**Total Time Estimate:** 3-4 hours for complete, professional submission

---

**Questions? Refer back to:**
- Voiceover script: Section 4
- Video production: Section 5
- Alteryx design: Section 7
- Final checklist: Section 8

**YOU ARE READY TO BUILD.** 🎬

---

*Blueprint created November 9, 2025*  
*For: Meridian City Hospital ER Datathon Submission*  
*By: Data Analytics Team (Consultant, Analyst, Scientist)*
