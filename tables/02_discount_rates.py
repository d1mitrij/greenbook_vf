"""Social Time Preference Rates and health discount rates (HM Treasury Green Book 2026)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import pipeline

if __name__ == "__main__":
    print(pipeline.run_table("discount_rates"))
