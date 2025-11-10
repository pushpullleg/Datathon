# VIDEO PRODUCTION GUIDE
## Professional Recording Tips for Datathon Submission

---

## 🎬 PRE-RECORDING CHECKLIST (Do This BEFORE Recording)

### Technical Setup (30 min)

**Zoom Configuration:**
- [ ] Create Zoom meeting link (all 3 students join)
- [ ] Test link works for all 3 on their devices
- [ ] Enable "Record to Cloud" (automatic backup)
- [ ] Enable "Record Locally" option on main device (backup)
- [ ] Set screen share permission to main speaker
- [ ] Test screen share with PowerPoint

**Audio Setup:**
- [ ] Each person: USB microphone (Blue Yeti, Audio-Technica, etc.)
- [ ] Test audio levels: Should show -10dB to -3dB on Zoom meter (not peaking)
- [ ] Check: No loud background noise (fan, AC, traffic)
- [ ] Minimize echo: Position mics away from walls
- [ ] Backup: Record local audio on phone Voice Memos simultaneously

**PowerPoint Preparation:**
- [ ] Open Meridian_ER_Presentation.pptx
- [ ] Verify all 8 slides present and correct order
- [ ] Test screen share: Can you see slides clearly?
- [ ] Slides readable from 3 feet away? (Use Zoom 150% if needed)
- [ ] Speaker notes visible to consultant/analyst/scientist?

**Lighting:**
- [ ] Position lights FACING speakers (not behind)
- [ ] No harsh shadows on faces
- [ ] Avoid windows with bright backlight
- [ ] Webcams at eye level (not looking down/up)
- [ ] Test: Take a screenshot, check if faces well-lit

**Backgrounds:**
- [ ] Clean, professional background (bookshelf, plants, plain wall)
- [ ] Nothing distracting or unprofessional in frame
- [ ] Blur background if messy (Zoom setting: blur or virtual background)
- [ ] Test: Record 10-sec sample, review for distractions

**Technical Test (15 min):**
- [ ] All 3 join Zoom meeting
- [ ] Test microphone levels (Zoom audio settings)
- [ ] Each person speaks: "Test, one, two, three"
- [ ] Check: Is audio clear? Any feedback/echo?
- [ ] One person shares screen: Can all 3 see PowerPoint?
- [ ] Advance to Slide 2: Does it work smoothly?
- [ ] Do a 30-sec dry run: Consultant reads opening 2 sentences

---

## 🎙️ DURING RECORDING

### Studio Rules (Enforce These)

**Before You Hit Record:**
1. Everyone on Zoom 2 minutes early
2. Put phones on silent (no notifications)
3. Close all other apps (Slack, email, etc.)
4. Start local recording on phone FIRST
5. Wait for Zoom cloud recording to start (watch timer)
6. Everyone takes a deep breath

**Ground Rules While Recording:**
- **Pause Between Speakers:** 5-second silence (easier to edit)
- **Don't Restart:** If you stumble, pause 5 sec, re-read last sentence, continue
- **Advance Slides:** Only when speaker signals or says "next slide"
- **Stay Focused:** No side conversations during recordings
- **Watch Timing:** Follow script timing marks in Voiceover_Script.txt
- **Audio Priority:** If audio cuts, pause, rejoin Zoom, continue

### Recording Sequence (Follow This Order)

```
SEGMENT 1: Hook (0:00-0:30)
- SPEAKER: Consultant
- SLIDE: 1 (Title)
- LENGTH: Exactly 30 seconds
- ACTION: Consultant speaks with confidence, directly to camera
- PAUSE: 5 seconds

SEGMENT 2: Investigation (0:30-2:00)
- SPEAKER: Analyst
- SLIDE: 2 (Breakdown chart)
- LENGTH: Exactly 90 seconds
- ACTION: Analyst tells the detective story
- PAUSE: 5 seconds

SEGMENT 3: Revelation (2:00-3:30)
- SPEAKER: Scientist
- SLIDE: 3 (Bottleneck visualization)
- LENGTH: Exactly 90 seconds
- ACTION: Scientist reveals the surprise discovery
- PAUSE: 5 seconds

SEGMENT 4A: Business Solution (3:30-5:00)
- SPEAKER: Consultant
- SLIDE: 4 (3-tier solution)
- LENGTH: Exactly 90 seconds
- ACTION: Consultant explains Tiers 1-3 with energy
- PAUSE: 5 seconds

SEGMENT 4B: Technical Solution (5:00-6:30)
- SPEAKER: Scientist
- SLIDE: 5 (ML models)
- LENGTH: Exactly 90 seconds
- ACTION: Scientist explains 5 models clearly
- PAUSE: 5 seconds

SEGMENT 5: Contingencies (6:30-7:30)
- SPEAKER: Consultant
- SLIDE: 6 (Decision tree)
- LENGTH: Exactly 60 seconds
- ACTION: Consultant shows mature thinking
- PAUSE: 5 seconds

SEGMENT 6: Vision (7:30-9:30)
- SPEAKERS: All 3 (rotating)
- SLIDE: 7-8 (before/after, then title)
- LENGTH: Exactly 120 seconds
- ACTION: Consultant (30 sec) → Analyst (30 sec) → Scientist (30 sec) → All 3 (30 sec)
- END: Hold final title slide for 3 seconds, then "cut"

TOTAL DURATION: 9 min 30 sec (9:30) ✅
```

### Quality Checks During Recording

**After Each Segment (during 5-sec pause):**
- [ ] Audio clear? (No background noise, speech distinct?)
- [ ] Timing correct? (Did you match the script timing?)
- [ ] Confidence level high? (Or do you want to re-do it?)
- [ ] Slides correct? (Are we on the right slide?)

**Red Flags - STOP and Re-Record:**
- ❌ Speaker speaks too fast (rushed)
- ❌ Long pause/stutter (awkward silence)
- ❌ Audio cuts out (no sound)
- ❌ Feedback/echo in background
- ❌ Speaker seems unsure or reading robotically

**Good to Keep Going:**
- ✅ Natural pace, confident delivery
- ✅ Clear audio, no background noise
- ✅ Smooth speaker transitions
- ✅ Timing close to script

---

## ✂️ POST-PRODUCTION (After Recording)

### Step 1: Download Files (5 min)
```
From Zoom:
- Download video file: Meridian_ER_Datathon_Video.mp4 (or .mov)
- Download audio file (if separate): Meridian_ER_Audio.m4a
- Keep originals (don't delete until final version confirmed)

Local Backups:
- Retrieve voice memo recordings from phones
- Copy to computer
- Label: Consultant_Audio, Analyst_Audio, Scientist_Audio
```

### Step 2: Audio Cleanup (10 min - Using Audacity, Free)

```
1. OPEN AUDACITY (free download at audacityteam.org)

2. IMPORT AUDIO
   - File → Open → Select Meridian_ER_Audio.m4a
   - (Or paste audio from video using Audacity's audio extractor)

3. NOISE REDUCTION
   - Select → All (Ctrl+A)
   - Highlight 2 seconds of pure background noise (start or end)
   - Effect → Noise Reduction → Get Noise Profile
   - Select → All again
   - Effect → Noise Reduction → Apply (default settings fine)

4. VOLUME NORMALIZATION
   - Select → All
   - Effect → Normalize
   - Set to: Peak amplitude to -3.0 dB
   - Click OK

5. REMOVE SILENCE (Optional - cleans up gaps)
   - Select → All
   - Analyze → Silence Finder (if available)
   - Effect → Truncate Silence (if available)
   - Or manually delete long silences

6. EXPORT CLEANED AUDIO
   - File → Export → Export as MP3
   - Quality: 192 kbps (good quality, reasonable file size)
   - Save as: Meridian_ER_Audio_Clean.mp3
```

### Step 3: Video Editing (15 min - Using iMovie or CapCut, Free)

**Using CapCut (Recommended for this project):**
```
1. IMPORT MEDIA
   - Open CapCut
   - Create new project
   - Import: Meridian_ER_Datathon_Video.mp4 (from Zoom)
   - Import: Meridian_ER_Audio_Clean.mp3 (cleaned audio)
   - Import: Meridian_ER_Presentation.pptx (or export slides as images)

2. ADD VIDEO TO TIMELINE
   - Drag video to timeline
   - Mute original audio (click audio track, mute)
   - Trim: Keep only 9:30 (remove any pre/post recording)

3. SYNC CLEANED AUDIO
   - Drag cleaned audio to audio track
   - Align start of audio with start of video (drag to sync)
   - Test: Play back, audio should match video

4. ADD TITLE SLIDE (0:00-0:05)
   - If Zoom screen share worked: Skip this
   - If not: Create title card "Emergency Room Efficiencies - From Bottleneck to Breakthrough"
   - Place at beginning, 5 seconds duration

5. ADD ENDING/CREDITS (9:25-9:30)
   - Add final title slide or black screen
   - Duration: 5 seconds
   - Add text overlay: Student names, University, Date

6. COLOR CORRECTION (Optional but Recommended)
   - Select video
   - Adjustments → Color
   - Increase saturation +10% (makes skin tones pop)
   - Increase brightness +5% (fixes Zoom default pale look)
   - Keep it subtle (don't overdo it)

7. EXPORT
   - File → Export
   - Format: MP4
   - Resolution: 1080p (1920×1080)
   - Codec: H.264
   - Bitrate: High (8000+ kbps)
   - Filename: Meridian_ER_Datathon_Video.mp4
```

**Using iMovie (Alternative):**
```
1. Open iMovie
2. Create new movie
3. Import video: Drag Meridian_ER_Datathon_Video.mp4
4. Import audio: File → Import Media → Meridian_ER_Audio_Clean.mp3
5. Delete original video audio (right-click, detach)
6. Position cleaned audio to sync with video
7. Add title: Click at beginning, add title card
8. Add credits: Click at end, add closing title
9. Export: File → Share → File → 1080p HD, H.264
```

### Step 4: Final Quality Check (5 min)

**Watch the Complete 9:30 Video:**
- [ ] Audio is clear (no background noise)?
- [ ] Audio synced with video (no lag)?
- [ ] All 3 speakers audible and understandable?
- [ ] Slides visible and readable?
- [ ] Timing: Total 7-10 minutes? (Should be 9:30, well within range)
- [ ] No awkward gaps or jumps?
- [ ] Colors look good (not washed out)?
- [ ] Title visible at start?
- [ ] Credits visible at end?

**Checklist Before Export:**
- [ ] Video length: 9:30 ✅
- [ ] Audio quality: Clear ✅
- [ ] Slides visible: Yes ✅
- [ ] Speaker transitions: Smooth ✅
- [ ] Timing: Accurate ✅
- [ ] Professional appearance: Yes ✅

---

## 🎬 BACKUP PLANS

**IF Zoom Audio Fails:**
```
PROBLEM: Zoom recording has no audio or distorted audio

SOLUTION:
1. Extract audio from local phone backup recordings
2. Splice together the 3 audio tracks (Consultant + Analyst + Scientist)
3. Sync with Zoom video using iMovie/CapCut
4. Result: Audio from phones, video from Zoom (minimal quality loss)
```

**IF Screen Share Doesn't Record Slides:**
```
PROBLEM: Video shows video of speakers, not slides

SOLUTION:
1. Export PowerPoint slides as PNG images (high resolution 1920×1080)
2. Import images into iMovie/CapCut
3. Time each slide to match voiceover segment timing
4. Result: Video of speakers + overlaid/integrated slides
```

**IF Someone's Audio Gets Cut Off:**
```
PROBLEM: One speaker's segment has missing audio

SOLUTION:
1. Have that speaker re-record their segment solo
2. Export as clean MP3 (just their audio)
3. In iMovie/CapCut, replace that segment's audio
4. Sync with video timing
5. Result: Seamless (viewers won't notice)
```

**IF You Exceed 10 Minutes:**
```
PROBLEM: Total video length exceeds 10 min limit

SOLUTION:
1. Trim non-essential pauses (use CapCut silence detection)
2. Reduce Segment 5 (Contingencies) from 60 to 45 seconds
3. Re-time edits to stay under 10 min
4. Result: 9:00-9:15 min, still complete story
```

---

## 📊 TROUBLESHOOTING

| Problem | Cause | Solution |
|---------|-------|----------|
| Audio is too quiet | Mic levels too low | Re-record with mic closer to mouth |
| Audio is distorted | Mic levels too high (peaking) | Lower mic input level 20% in Zoom |
| Background noise | Room is loud | Record in quieter room, close doors |
| Feedback/echo | Microphone facing speaker | Reposition mic away from Zoom audio |
| Video looks washed out | Zoom default color grading | Increase saturation +10% in editing |
| Slides not visible | Screen share didn't record | Export slides as PNG, overlay in editor |
| Speakers talking over each other | Not following speaker transitions | Use 5-sec silence cue between speakers |
| Timing off by 5-10 seconds | Speaker read too fast/slow | Re-record that segment, match script timing |
| File size too large | High bitrate, long video | Re-export at lower bitrate (6000 kbps) |
| Audio cuts out midway | Zoom recording failed | Use local phone audio backup |

---

## 📝 FINAL CHECKLIST BEFORE SUBMISSION

**Day Before Recording:**
- [ ] All 3 team members available and confirmed
- [ ] Script printed (one copy per person, highlighted their sections)
- [ ] PowerPoint downloaded and tested
- [ ] Zoom link created and tested
- [ ] Microphones acquired and tested
- [ ] Audio levels verified (-5dB sweet spot)
- [ ] Recording space ready (lighting, background, quiet)
- [ ] Everyone is confident and excited

**Morning of Recording:**
- [ ] No one is sick (reschedule if needed)
- [ ] Tech check: Zoom, microphones, screen share
- [ ] Backup plan reviewed (everyone knows Plan B)
- [ ] Dry run: Quick 30-second test recording
- [ ] Everyone takes a moment to center/breathe

**After Recording:**
- [ ] Verify Zoom recording downloaded (check file size)
- [ ] Check local backup recordings exist on phones
- [ ] Quick quality check: Audio clear, timing ~9:30?
- [ ] Proceed to audio cleanup

**After Editing:**
- [ ] Final video downloaded and saved in multiple places
- [ ] Quality check: Watch entire 9:30 video start-to-finish
- [ ] PowerPoint presentation ready (saved .pptx)
- [ ] Executive summary ready (saved .txt, 300 words)
- [ ] Alteryx workflow documentation ready (.md file)
- [ ] README prepared with all instructions
- [ ] All files organized in DATATHON_SUBMISSION folder

**Submission Day:**
- [ ] Verify submission platform and deadline
- [ ] Check file format requirements (MP4? AVI? WebM?)
- [ ] Verify file naming conventions (no spaces, clear labels)
- [ ] Upload video, PowerPoint, executive summary, workflow docs
- [ ] Wait for confirmation that files received
- [ ] Save confirmation number and receipt
- [ ] Take a screenshot of successful submission

---

## 💪 YOU'VE GOT THIS

**Remember:**
- ✅ You have an excellent story to tell
- ✅ Your data is compelling and real
- ✅ Your analysis is consultant-level thinking
- ✅ Your preparation is thorough
- ✅ Your team is ready

**The judges are going to be impressed.**

**Now go record an awesome video!** 🚀

---

*Production Guide for Meridian ER Datathon Submission*  
*November 9, 2025*
