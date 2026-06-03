import json

with open(
    "outputs/trend_scores.json",
    "r"
) as file:

    trend_scores = json.load(file)

with open(
    "outputs/trend_changes.json",
    "r"
) as file:

    trend_changes = json.load(file)

top_trend = max(
    trend_scores,
    key=trend_scores.get
)

summary = []

summary.append(
    f"{top_trend} remains the dominant technology trend with {trend_scores[top_trend]} mentions."
)

for category, change in trend_changes.items():

    if change > 0:

        summary.append(
            f"{category} discussions increased by {change} points."
        )

    elif change < 0:

        summary.append(
            f"{category} discussions decreased by {abs(change)} points."
        )

summary_text = "\n".join(summary)

with open(
    "outputs/executive_summary.txt",
    "w"
) as file:

    file.write(
        summary_text
    )

print(
    "Executive summary generated!"
)
