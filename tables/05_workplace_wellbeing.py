"""Workplace wellbeing cost parameters and benchmarks (HM Treasury / PHE Tool 2011)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import pipeline

if __name__ == "__main__":
    print(pipeline.run_table("workplace_wellbeing"))
