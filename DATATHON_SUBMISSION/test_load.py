
from pptx import Presentation
import os

try:
    prs = Presentation("Meridian_ER_Presentation.pptx")
    print(f"✅ Successfully loaded presentation with {len(prs.slides)} slides")
    print("Note: For full PDF conversion on macOS, you may need to:")
    print("1. Open PowerPoint or use brew install libreoffice")
    print("2. Or use online conversion tool")
except Exception as e:
    print(f"Error: {e}")
