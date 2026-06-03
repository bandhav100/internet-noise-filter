import pandas as pd
import matplotlib.pyplot as plt

# Load processed dataset
df = pd.read_csv("data/processed_hackernews.csv")

# Define trend clusters
trend_clusters = {
    "AI": [
        "ai", "gpt", "openai",
        "llm", "agents", "learning"
    ],

    "Programming": [
        "python", "java",
        "javascript", "developer"
    ],

    "Startups": [
        "startup", "funding",
        "business", "company"
    ],

    "Security": [
        "security", "cyber",
        "privacy", "attack"
    ]
}

# Store scores
trend_scores = {}

titles = df["clean_title"].astype(str)

# Count cluster occurrences
for cluster_name, keywords in trend_clusters.items():

    score = 0

    for title in titles:

        for keyword in keywords:

            if keyword in title:
                score += 1

    trend_scores[cluster_name] = score

# Prepare chart data
labels = list(trend_scores.keys())
values = list(trend_scores.values())

# Create bar chart
plt.figure(figsize=(8,5))

plt.bar(labels, values)

# Labels and title
plt.title("Internet Trend Analysis")
plt.xlabel("Trend Categories")
plt.ylabel("Trend Scores")

# Save chart
plt.savefig("outputs/trend_chart.png")

# Show chart
plt.show()
