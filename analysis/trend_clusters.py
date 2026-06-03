import json

# Load merged data

with open("data/merged_data.json", "r") as file:
    data = json.load(file)

# Trend categories

trend_clusters = {

    "AI": [
        "ai",
        "openai",
        "claude",
        "llm",
        "gemini",
        "agent",
        "agents",
        "anthropic",
        "copilot"
    ],

    "Programming": [
        "python",
        "java",
        "rust",
        "javascript",
        "coding",
        "developer",
        "programming",
        "code",
        "github"
    ],

    "Security": [
        "security",
        "cyber",
        "exploit",
        "privacy",
        "attack",
        "vulnerability",
        "zero-day",
        "zero",
        "hack"
    ],

    "Startups": [
        "startup",
        "funding",
        "business",
        "company",
        "founder",
        "founders"
    ]
}

trend_scores = {}

# Extract titles

titles = []

for item in data:

    title = item.get("title")

    if title:
        titles.append(title.lower())

# Calculate scores

for cluster_name, keywords in trend_clusters.items():

    score = 0

    for title in titles:

        for keyword in keywords:

            if keyword in title:

                score += 1

    trend_scores[cluster_name] = score

# Print results

print("\nTREND CLUSTER ANALYSIS\n")

for cluster, score in trend_scores.items():

    print(f"{cluster}: {score}")

# Save JSON

with open(
    "outputs/trend_scores.json",
    "w"
) as file:

    json.dump(
        trend_scores,
        file,
        indent=4
    )

print("\nTrend scores saved!")
