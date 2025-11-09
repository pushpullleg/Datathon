#!/bin/bash
# 🚀 QUICK START: Shift Analysis Analyst Script
# Run this to execute full analysis in <5 minutes

echo "🎯 DATATHON SHIFT ANALYSIS - QUICK START"
echo "========================================"
echo ""

# Check if final_data.csv exists
if [ ! -f "final_data.csv" ]; then
    echo "❌ ERROR: final_data.csv not found in current directory"
    echo "   Please ensure final_data.csv is in: $(pwd)"
    exit 1
fi

echo "✓ Found final_data.csv"
echo ""

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ ERROR: Python 3 not found"
    echo "   Install Python from https://www.python.org/downloads/"
    exit 1
fi

echo "✓ Python 3 found"
echo ""

# Install required packages
echo "📦 Installing required packages..."
pip install -q pandas numpy matplotlib seaborn 2>/dev/null
if [ $? -eq 0 ]; then
    echo "✓ Packages installed"
else
    echo "⚠ Could not auto-install packages"
    echo "   Run: pip install pandas numpy matplotlib seaborn"
    echo "   Then try again: python3 shift_analysis_analyst.py"
fi

echo ""
echo "🔄 Running analysis..."
echo "========================================"
echo ""

# Run the analysis
python3 shift_analysis_analyst.py

# Check if analysis succeeded
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ ANALYSIS COMPLETE!"
    echo "========================================"
    echo ""
    echo "📊 Files generated:"
    echo "   1. shift_analysis_visualization.png (4-panel chart)"
    echo "   2. shift_analysis_analyst_report.txt (detailed findings)"
    echo ""
    echo "📋 Next steps:"
    echo "   1. Open shift_analysis_analyst_report.txt"
    echo "   2. Copy key numbers for video script"
    echo "   3. Update team on actual findings"
    echo "   4. Record practice take with new numbers"
    echo ""
    echo "🎬 Key numbers to extract and use:"
    echo "   • Day shift bottleneck concentration: [see report]"
    echo "   • Day shift utilization: [see report]"
    echo "   • Morning rush bottleneck events: [see report]"
    echo ""
    echo "Good luck! 🚀"
else
    echo ""
    echo "❌ Analysis failed"
    echo "   Check error messages above"
    echo "   Try: python3 shift_analysis_analyst.py"
fi
