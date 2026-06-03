import json
import csv
import os
from datetime import datetime

# Load latest trend scores

with open(
    "outputs/trend_scores.json",
    "r"
) as file:

    scores = json.load(file)

today = datetime.now().strftime(
    "%Y-%m-%d"
)

row = {

    "date": today,

    "AI": scores["AI"],

    "Programming": scores["Programming"],

    "Security": scores["Security"],

    "Startups": scores["Startups"]

}

file_exists = os.path.exists(
    "history/trend_history.csv"
)

with open(
    "history/trend_history.csv",
    "a",
    newline=""
) as file:

    writer = csv.DictWriter(

        file,

        fieldnames=[
            "date",
            "AI",
            "Programming",
            "Security",
            "Startups"
        ]

    )

    if not file_exists:

        writer.writeheader()

    writer.writerow(row)

print(
    "Trend history updated!"
)
