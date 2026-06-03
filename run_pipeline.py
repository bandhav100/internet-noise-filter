import os
import sys

PYTHON = sys.executable
print("\nSTEP 1: Collecting HackerNews Data")
os.system(
    f"{PYTHON} collectors/hackernews_collector.py"
)

print("\nSTEP 2: Collecting RSS Data")
os.system(
    f"{PYTHON} collectors/rss_collectors.py"
)
print("\nSTEP 3: Collecting GitHub Trending")
os.system(
    f"{PYTHON} collectors/github_collector.py"
)

print("\nSTEP 4: Merging Data")
os.system(
    f"{PYTHON} preprocess/merge_data.py"
)

print("\nSTEP 5: Removing Duplicates")
os.system(
    f"{PYTHON} preprocess/remove_duplicates.py"
)

print("\nSTEP 6: Trend Analysis")
os.system(
    f"{PYTHON} analysis/trend_analysis.py"
)

print("\nSTEP 7: Trend Clustering")
os.system(
    f"{PYTHON} analysis/trend_clusters.py"
)
print("\nSTEP 8: Save History")
os.system(
    f"{PYTHON} analysis/save_history.py"
)

print("\nSTEP 9: Trend Changes")
os.system(
    f"{PYTHON} analysis/trend_change.py"
)
print("\nSTEP 10: Topic Modeling")
os.system(
    f"{PYTHON} analysis/topic_modeling.py"
)

print("\nSTEP 11: AI Insight Generation")
os.system(
    f"{PYTHON} analysis/insight_engine.py"
)

print("\nSTEP 12: Executive Summary")
os.system(
    f"{PYTHON} analysis/generate_summary.py"
)
print("\nSTEP 13: Report Generation")

os.system(
    f"{PYTHON} analysis/report_generator.py"
)
print("\nSTEP 14: PDF Report")

os.system(
    f"{PYTHON} analysis/pdf_report.py"
)
from datetime import datetime

timestamp = str(
    datetime.now()
)

with open(
    "outputs/last_run.txt",
    "w"
) as file:
    file.write(
        timestamp
    )

print(
    "\nLast Run:",
    timestamp
)
print("\nPIPELINE COMPLETE")
