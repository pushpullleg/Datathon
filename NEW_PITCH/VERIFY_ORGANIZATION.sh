#!/bin/bash

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║        NEW_PITCH FOLDER VERIFICATION CHECKLIST                 ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

FOLDER="/Users/mukeshravichandran/Datathon/NEW_PITCH"
cd "$FOLDER" || exit 1

echo "📁 FOLDER: $FOLDER"
echo ""

# Count files
TOTAL_FILES=$(ls -1 | wc -l)
echo "✅ File Count: $TOTAL_FILES files"

# List all files
echo ""
echo "📂 FILES PRESENT:"
ls -1 | nl

echo ""
echo "📊 STATISTICS:"
echo "   • Total lines: $(wc -l *.md *.py *.sh *.txt 2>/dev/null | tail -1 | awk '{print $1}')"
echo "   • Total size: $(du -sh . | awk '{print $1}')"

echo ""
echo "🔍 VERIFICATION:"

# Check execution files
if [ -f "shift_analysis_analyst.py" ]; then echo "   ✓ shift_analysis_analyst.py"; else echo "   ✗ shift_analysis_analyst.py MISSING"; fi
if [ -f "run_analyst.sh" ]; then echo "   ✓ run_analyst.sh"; else echo "   ✗ run_analyst.sh MISSING"; fi

# Check quick start guides
if [ -f "QUICK_REFERENCE_CARD.md" ]; then echo "   ✓ QUICK_REFERENCE_CARD.md"; else echo "   ✗ QUICK_REFERENCE_CARD.md MISSING"; fi
if [ -f "00_START_HERE_ANALYST_COMPLETE.md" ]; then echo "   ✓ 00_START_HERE_ANALYST_COMPLETE.md"; else echo "   ✗ 00_START_HERE_ANALYST_COMPLETE.md MISSING"; fi
if [ -f "INDEX.md" ]; then echo "   ✓ INDEX.md"; else echo "   ✗ INDEX.md MISSING"; fi

# Check documentation
if [ -f "ANALYST_SCRIPT_GUIDE.md" ]; then echo "   ✓ ANALYST_SCRIPT_GUIDE.md"; else echo "   ✗ ANALYST_SCRIPT_GUIDE.md MISSING"; fi
if [ -f "ENHANCED_PRE_MORNING_RUSH_ANALYSIS.md" ]; then echo "   ✓ ENHANCED_PRE_MORNING_RUSH_ANALYSIS.md (NEW!)"; else echo "   ✗ ENHANCED_PRE_MORNING_RUSH_ANALYSIS.md MISSING"; fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🚀 READY TO RUN?"
if [ -f "shift_analysis_analyst.py" ] && [ -f "QUICK_REFERENCE_CARD.md" ]; then
    echo "   ✅ YES! All files organized."
    echo ""
    echo "   Next: cd $FOLDER && python3 shift_analysis_analyst.py"
else
    echo "   ⚠️ Missing some files"
fi
echo ""
