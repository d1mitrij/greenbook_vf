"""Society-wide annual health/wellbeing benefits from cultural engagement (Frontier/DCMS 2024)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import pipeline

if __name__ == "__main__":
    print(pipeline.run_table("culture_health_societal"))
