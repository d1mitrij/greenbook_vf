"""WELLBY and QALY unit valuations (HM Treasury Wellbeing Guidance 2021; OECD 2025)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import pipeline

if __name__ == "__main__":
    print(pipeline.run_table("wellby_valuations"))
