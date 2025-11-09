# Executive Summary vs. Presentation Strategy
## Why They're Different, Why They Complement, Why There's NO Repetition

**Date:** November 9, 2025  
**Context:** Datathon submission (video + exec summary + Alteryx workflow)

---

## 📊 QUICK COMPARISON TABLE

| Aspect | Executive Summary | Presentation (Video) |
|--------|-------------------|----------------------|
| **Length** | 200-300 words | 7-10 minutes (~3,000-4,000 words spoken) |
| **Format** | Static text (.docx) | Dynamic video (slides + voiceover) |
| **Audience** | Hospital executives reading on their own | Judges watching + listening |
| **Reading Speed** | ~2 minutes to read | ~9 minutes to watch |
| **Depth** | Summary only (headline findings) | Detailed journey (investigation, discovery, proof) |
| **Goal** | "Should we greenlight this?" | "Are these brilliant problem-solvers?" |
| **Tone** | Formal, business, bottom-line | Engaging, investigative, cinematic |
| **Visual Elements** | None (text only) | Charts, graphs, decision trees, data viz |
| **Contingencies** | IF/THEN brief mentions | IF/THEN fully explained with reasoning |
| **Technical Detail** | Minimal | Moderate (ML models, system theory, root cause algorithm) |
| **Call-to-Action** | "Approve funding / Next steps" | "This team is exceptional / Hire them" |

---

## 🎯 STRATEGIC PURPOSE OF EACH

### **EXECUTIVE SUMMARY = Decision-Maker's Cheat Sheet**

**Who reads it?**
- Hospital CFO (2 minutes available)
- Hospital COO (skimming for ROI)
- Meridian management team (deciding whether to fund)

**What they need to know (in order):**
1. **What's the problem?** (Cost: $890K lost quarterly)
2. **Why does it exist?** (Root cause: Process, not staffing)
3. **What's the fix?** (3-tier solution, 5 ML models)
4. **What does it cost & earn?** ($550K → $15.3M, 3.3-week payback)
5. **What are the risks?** (IF wait doesn't improve 10% by Week 4 → pivot)
6. **What do you need from me?** (Approve $550K, 12-week timeline)

**What they DON'T want:**
- How you discovered it
- Why other hypotheses failed
- Detailed machine learning
- Investigation journey
- Technical proofs

**Use case:** Hospital exec scans it while on the phone with the board. They need to decide in 5 minutes: Yes or No?

---

### **PRESENTATION (VIDEO) = Proof of Competence**

**Who watches it?**
- Datathon judges (want to see team quality)
- Alteryx executive (evaluating talent)
- Consulting firm representatives (considering hiring)
- University decision-makers (rewarding excellence)

**What they need to see (in order):**
1. **Do they understand the problem deeply?** (Yes, 39 min wait + 107 min cycle time breakdown)
2. **Did they investigate rigorously?** (Yes, tested 7 hypotheses, only 1 worked)
3. **Are they honest about failure?** (Yes, "we tried X, it was wrong")
4. **Can they tell a compelling story?** (Yes, Mystery → Investigation → Revelation → Solution)
5. **Do they understand system dynamics?** (Yes, System Theory, Theory of Constraints)
6. **Can they build production solutions?** (Yes, 5 ML models with <500ms latency)
7. **Can they think like consultants?** (Yes, IF/THEN contingency planning)
8. **Are they impressive people?** (Should judge this from the video)

**What they DON'T care about:**
- Specific dollar amounts (too businessy for academic judges)
- Approval workflows (not relevant to judges)
- Implementation timelines (judges care about analysis, not execution)

**Use case:** Alteryx Ace watches it and thinks: "These three are smart. I want to work with them."

---

## 🎨 CONTENT MAPPING (What Goes Where)

### **INFORMATION FLOW DIAGRAM**

```
┌─────────────────────────────────────────────────────────────────┐
│                    TOTAL FINDINGS / DATA                        │
│  (Bottleneck analysis, root cause, ML models, staff util, etc)  │
└────────────┬──────────────────────────────────────────┬─────────┘
             │                                          │
        FILTER 1:                               FILTER 2:
      Business Focus                            Story Focus
      (What matters to                        (What impresses
       hospital execs)                          judges)
             │                                          │
             ▼                                          ▼
    ┌─────────────────┐                    ┌──────────────────┐
    │ EXEC SUMMARY    │                    │   PRESENTATION   │
    │ (200 words)     │                    │   (9 min video)  │
    └────────┬────────┘                    └────────┬─────────┘
             │                                      │
        CONTENT INSIDE:                      CONTENT INSIDE:
        ✓ Problem statement                 ✓ Investigation story
        ✓ Root cause (brief)                ✓ Hypothesis testing
        ✓ Solution (high-level)             ✓ System theory proof
        ✓ ROI & payback                     ✓ ML model details
        ✓ IF/THEN risks                     ✓ Technical credibility
        ✗ Investigation journey             ✗ Specific ROI numbers
        ✗ Why hypothesis failed             ✗ Implementation steps
        ✗ System theory details             ✗ Hospital-specific process
        ✗ ML model names/types              ✗ Approval workflows
        ✗ Technical proofs                  ✗ Budget justification
```

---

## 🚫 WHAT DOES NOT REPEAT (Avoiding Duplication)

### **Executive Summary DOES NOT Cover:**
- ❌ "We tested 7 hypotheses and 6 failed" → That's ONLY in the video
- ❌ "System Theory shows the bottleneck is..." → That's ONLY in the video
- ❌ "Model 1 is Random Forest, Model 2 is LightGBM" → That's ONLY in the video
- ❌ "Here's why we investigate this way" → That's ONLY in the video
- ❌ Detailed timeline breakdown (39 min wait, 107 min doctor cycle) → That's ONLY in the video

### **Presentation (Video) DOES NOT Cover:**
- ❌ "Payback period is 3.3 weeks" → That's ONLY in the exec summary
- ❌ "Total investment $550K" → That's ONLY in the exec summary
- ❌ "If wait time doesn't improve 10% by Week 4, pivot to staffing" → Video mentions IF/THEN but not specific % triggers
- ❌ "This costs the hospital $890,000 quarterly" → That's ONLY in the exec summary
- ❌ Week-by-week implementation timeline (Weeks 1-4, 5-8, 9-12) → Brief in video, detailed in summary

---

## 💡 STRATEGIC COMPLEMENTARITY

### **How They Support Each Other:**

**Scenario 1: Hospital Exec Path**
```
Step 1: Exec scans Executive Summary (2 min)
        → Learns: Problem, ROI, timeline, risks
        → Decision: "Approve the $550K investment"
        
Step 2: Exec says to team: "Show me the details"
        → They watch the Presentation video (9 min)
        → Learns: HOW the analysis was done
        → Reaction: "These consultants did rigorous work"
        
Result: Executive becomes INFORMED ADVOCATE within hospital
        ("I saw their video, they really know what they're doing")
```

**Scenario 2: Judge Path**
```
Step 1: Judge watches Presentation video (9 min)
        → Assesses: Team quality, analytical rigor, storytelling
        → Reaction: "This team is impressive"
        
Step 2: Judge reads Executive Summary (2 min)
        → Learns: Business impact of the work
        → Reaction: "Not only brilliant, but business-smart"
        
Result: Judge votes to award the team
        (Story + business acumen = rare combination)
```

---

## 📝 CONTENT BREAKDOWN: What Lives WHERE

### **ONLY in Executive Summary (200 words)**
```
1. PROBLEM STATEMENT (Business framing)
   "Costs the hospital $890,000 quarterly in lost revenue"
   
2. ROOT CAUSE (Brief version, no investigation story)
   "Process inefficiency: 2,179 bottleneck events, 50% vs 75-80% utilization"
   
3. SOLUTION (High-level only, not detailed)
   "3-tier approach, 5 ML models, 12-week timeline"
   
4. FINANCIAL IMPACT (Critical for exec decision)
   "Investment: $550K
    Year 1 benefit: $15.3M
    Payback: 3.3 weeks
    ROI: 2,662%"
   
5. CONTINGENCIES (Risk management for exec)
   "IF models improve wait <10% by Week 4 → Pivot to staffing analysis"
   
6. CALL TO ACTION (What you're asking for)
   "Recommend: Approve $550K, 12-week pilot timeline, weekly KPI gates"
```

### **ONLY in Presentation (9 min video)**
```
1. INVESTIGATION STORY (Why it's interesting)
   "We thought it was staffing → We tested that hypothesis → Data proved us wrong"
   
2. HYPOTHESIS TESTING (Shows rigor)
   "We checked seasonality → no pattern
    We checked special situations → no pattern
    We checked upstream/downstream → no pattern
    Finally: System Theory revealed the true constraint"
   
3. SYSTEM THEORY PROOF (Academic credibility)
   "Theory of Constraints: Bottleneck is the flow TO the resource,
    not the resource itself. This is textbook. Here's how it applies."
   
4. ML MODEL DETAILS (Technical credibility)
   "Model 1: Random Forest complexity predictor
    Model 2: LightGBM intelligent dispatcher
    Model 3: Quantile regression LOS forecaster
    Model 4: Prophet + XGBoost workload forecaster
    Model 5: Neural network risk detector"
   
5. REAL DATA EVIDENCE (Proof points)
   "15,000 patient visits analyzed
    2,179 bottleneck events documented
    Utilization rate calculations shown
    Actual vs predicted wait times graphed"
   
6. INVESTIGATIVE NARRATIVE (Storytelling)
   "Here's how we discovered it... here's what surprised us...
    here's why it matters... here's how to fix it"
```

### **MENTIONED IN BOTH (Different depth)**
```
Concept: 39-minute post-triage wait

EXEC SUMMARY VERSION:
"Post-triage wait consumes 23% of total ED time (39 minutes)"
(Just the fact, no breakdown)

PRESENTATION VERSION:
"39 minutes of post-triage wait
 107 minutes of doctor cycle time
 Together: 85% of total ED time
 Timeline chart showing the breakdown
 Patient journey visualization
 Comparison to industry benchmarks"
(Full story, visual proof, context)

---

Concept: Root cause is process, not staffing

EXEC SUMMARY VERSION:
"Root cause analysis reveals process inefficiency, not resource shortage.
Physician utilization rate is only 50% during bottlenecks (industry target: 75-80%).
Recommendation: Deploy process optimization before hiring."
(Conclusion only)

PRESENTATION VERSION:
"We discovered 2,179 moments where doctors were idle AND patients waited
at the EXACT same time. This is System Theory: bottleneck is flow, not resource.
Here's the diagram. Here's the calculation. Here's why this proves it.
Here's what we checked first and why those hypotheses failed."
(Full investigation, proof, alternative approaches)

---

Concept: 5 ML models solve the bottleneck

EXEC SUMMARY VERSION:
"5 machine learning models optimize patient routing and physician workload"
(Mention, move on)

PRESENTATION VERSION:
"Model 1: Random Forest classifier predicts patient complexity at triage
 → Feeds to Model 2: Intelligent dispatcher
   Model 2: LightGBM gradient boosting routes next patient to optimal doctor
   → Improves from 2-5 min manual dispatch to 30 sec
   Model 3: Quantile regression forecasts visit duration (25%, 50%, 90% percentile)
   Model 4: Prophet + XGBoost predicts bottlenecks 2 hours ahead
   → Alert on-call at $200 cost to avoid $22K loss (73:1 ROI)
   Model 5: Neural network detects high-risk patients
   → Early intervention saves $2.5M annually
   
All on real data. All <500ms latency. All explainable with SHAP/LIME."
(Complete architecture, impact per model, technical rigor)
```

---

## 🎯 STRATEGY SUMMARY

### **EXECUTIVE SUMMARY Strategy:**
**Goal:** Get hospital CFO to approve $550K funding in 2 minutes  
**Approach:** Problem → Root Cause → Solution → Impact → Ask  
**Tone:** Formal, data-driven, bottom-line focused  
**Content:** Only what an executive needs to make a GO/NO-GO decision  
**Repetition Risk:** ⚠️ AVOIDED by excluding investigation narrative

### **PRESENTATION (Video) Strategy:**
**Goal:** Prove you're brilliant problem-solvers who think rigorously  
**Approach:** Mystery → Investigation → Revelation → Solution → Impact  
**Tone:** Engaging, investigative, cinematic  
**Content:** Journey + proof + technical credibility + storytelling  
**Repetition Risk:** ⚠️ AVOIDED by excluding budget/ROI specifics

---

## ✅ HOW TO WRITE THEM WITHOUT REPETITION

### **Step 1: Write Executive Summary FIRST**
- Condense your findings into problem → cause → solution → impact
- Use numbers, ROI, business language
- 200-300 words, executive-digestible

### **Step 2: Write Presentation Script SECOND**
- DO NOT copy/paste from exec summary
- Focus on: How did you discover this? What surprised you? How do you prove it?
- Build narrative tension: Hypothesis → Test → Result
- Use the exec summary as a "fact-check" (ensure numbers align)
- But EXPAND into investigation, hypotheses, technical details

### **Step 3: Verify NO Repetition**
- Read exec summary aloud (should take 2 min)
- Read presentation script aloud (should take 9 min)
- Do they sound repetitive? NO → You're doing it right
- Do they cover the same ground? NO → They're complementary

---

## 📋 CONTENT OWNERSHIP CHECKLIST

| Content | Exec Summary | Presentation | Both? |
|---------|--------------|--------------|-------|
| Problem definition | ✅ | ✅ | ✅ Same statement |
| Root cause | ✅ Brief | ✅ Deep | ⚠️ Different depth |
| 7 hypotheses tested | ❌ | ✅ | Only video |
| System Theory explanation | ❌ | ✅ | Only video |
| 5 ML models | ✅ Mention | ✅ Details | ⚠️ Different depth |
| 39 min wait / 107 min cycle | ❌ | ✅ | Only video |
| 2,179 bottleneck events | ❌ | ✅ | Only video |
| 50% vs 75-80% utilization | ✅ Brief | ✅ Full | ⚠️ Different depth |
| $550K investment | ✅ | ❌ | Only summary |
| $15.3M benefit | ✅ | ❌ | Only summary |
| 3.3-week payback | ✅ | ❌ | Only summary |
| IF/THEN contingencies | ✅ Mention | ✅ Explain | ⚠️ Different depth |
| Investigation journey | ❌ | ✅ | Only video |
| Hypothesis failures | ❌ | ✅ | Only video |
| Technical ML details | ❌ | ✅ | Only video |

---

## 🎬 FINAL ANSWER: WHY THIS STRATEGY?

### **Why NOT repeat?**

**Repetition kills engagement:**
- Judges: "We've heard this already. Next."
- Executives: "Waste of time. I already read the summary."

**Repetition wastes limited time:**
- You have 9 minutes of video. Don't spend 3 repeating the exec summary.
- You have 300 words. Don't spend 100 on things video covers.

**Repetition undermines strategy:**
- Exec summary = Fast decision-making
- Video = Slow confidence-building
- If they're the same, why watch the video?

### **Why this complementarity?**

**Exec summary** enables: "Let's fund this"  
**Video** explains: "Here's why we deserve your funding"

**Different audiences, different needs:**
- CFO needs business case (exec summary provides this in 2 min)
- Judges need proof of competence (video provides this in 9 min)
- When exec watches video AFTER reading summary, they realize: "These people are thorough"

**Natural flow:**
- Exec reads summary → Decides to invest → Wants to understand how (watches video)
- Judge watches video → Impressed → Wants to see business case (reads summary)

---

## 🎯 YOUR SPECIFIC ASSIGNMENT

### **When writing Executive Summary:**
- [ ] Do NOT tell the investigation story
- [ ] DO state the problem and root cause (conclusion only)
- [ ] DO include financial impact ($550K, $15.3M, payback)
- [ ] DO mention 5 models exist (don't name them)
- [ ] DO include IF/THEN contingencies (1-2 sentences each)
- [ ] DO write in formal, business tone
- [ ] Target: 200-300 words, 2 min read

### **When writing Presentation Script:**
- [ ] DO tell the investigation story ("We tried X → it failed")
- [ ] DO explain System Theory and why it applies
- [ ] DO name all 5 models and what they do
- [ ] DO show real numbers (39 min, 107 min, 2,179 events, 50% utilization)
- [ ] DO explain IF/THEN with reasoning (not just bullet points)
- [ ] DO NOT mention specific $ amounts (not for judges)
- [ ] DO NOT mention approval workflows or "next steps" beyond the 12-week pilot
- [ ] DO write in engaging, investigative tone
- [ ] Target: 7-10 min (~3,000-4,000 words), 9 min delivery

---

## ✨ FINAL TAKEAWAY

| Aspect | Executive Summary | Presentation |
|--------|-------------------|--------------|
| **Audience** | Hospital CFO | Datathon Judges |
| **Speed** | 2 minutes | 9 minutes |
| **Goal** | Approve funding | Hire us / Award us |
| **Story** | What & Why | How & Why (deeply) |
| **Tone** | Formal | Engaging |
| **Content** | Business case | Investigative journey + technical proof |
| **Unique Content** | ROI, payback, budget | Hypothesis testing, System Theory, ML details |
| **Overlap** | Problem + root cause (brief) | Problem + root cause (detailed) |
| **Repetition Risk** | ✅ ZERO if you follow the strategy |

---

**Bottom Line:**  
Write them as **two completely different documents serving two completely different purposes for two completely different audiences.**  
The *only* overlap is the problem statement and root cause (conclusions)—everything else is unique to each format.

This is how professionals do it. This is what judges expect. This is why you'll stand out. ✨

