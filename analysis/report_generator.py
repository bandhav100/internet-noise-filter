import json
from datetime import date

with open("outputs/trend_scores.json", "r") as file:
    trend_scores = json.load(file)

with open("outputs/trend_changes.json", "r") as file:
    trend_changes = json.load(file)

with open("outputs/topic_models.json", "r") as file:
    topics = json.load(file)

with open("outputs/insights.json", "r") as file:
    insights = json.load(file)

today = date.today()

report = []

report.append(
    "TREND INTELLIGENCE REPORT"
)

report.append(
    f"\nDate: {today}\n"
)

report.append(
    "\nTREND SCORES\n"
)

for trend, score in trend_scores.items():

    report.append(
        f"{trend}: {score}"
    )

report.append(
    "\nTREND CHANGES\n"
)

for trend, change in trend_changes.items():

    report.append(
        f"{trend}: {change}"
    )

report.append(
    "\nTOP TOPICS\n"
)

for topic in list(topics.keys())[:10]:

    report.append(topic)

report.append(
    "\nAI GENERATED INSIGHTS\n"
)

for insight in insights:

    report.append(
        f"- {insight}"
    )

with open(
    "outputs/report.txt",
    "w"
) as file:

    file.write(
        "\n".join(report)
    )

print(
    "Report generated successfully!"
)
