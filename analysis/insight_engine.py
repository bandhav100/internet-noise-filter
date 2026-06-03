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

with open(
    "outputs/topic_models.json",
    "r"
) as file:

    topics = json.load(file)

insights = []

# Top Trend

top_trend = max(
    trend_scores,
    key=trend_scores.get
)

insights.append(
    f"{top_trend} remains the dominant technology trend across all monitored sources."
)

# Fastest Growing

top_gainer = max(
    trend_changes,
    key=trend_changes.get
)

if trend_changes[top_gainer] > 0:

    insights.append(
        f"{top_gainer} is the fastest growing trend in the latest analysis cycle."
    )

# AI Ecosystem

ai_terms = [
    "ai",
    "openai",
    "anthropic",
    "agent",
    "github"
]

found = []

for topic in topics:

    if topic.lower() in ai_terms:

        found.append(topic)

if found:

    insights.append(
        "AI discussions are being driven by "
        + ", ".join(found[:5])
        + "."
    )

# Industry Signals

if "nvidia" in topics:

    insights.append(
        "NVIDIA continues to play a major role in technology discussions."
    )

if "spacex" in topics:

    insights.append(
        "SpaceX remains a highly visible innovation topic."
    )

# Save

with open(
    "outputs/insights.json",
    "w"
) as file:

    json.dump(
        insights,
        file,
        indent=4
    )

print("\nAI INSIGHTS\n")

for insight in insights:

    print(
        "-",
        insight
    )
