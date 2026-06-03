import json

# -------------------------
# Trend Categories
# -------------------------

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
        "hack"
    ],

    "Startups": [
        "startup",
        "funding",
        "business",
        "company",
        "founder"
    ]
}

# -------------------------
# Function
# -------------------------

def calculate_scores(data):

    scores = {}

    titles = []

    for item in data:

        title = item.get("title")

        if title:
            titles.append(title.lower())

    for cluster_name, keywords in trend_clusters.items():

        score = 0

        for title in titles:

            for keyword in keywords:

                if keyword in title:
                    score += 1

        scores[cluster_name] = score

    return scores


# -------------------------
# Load HackerNews
# -------------------------

with open(
    "data/hackernews.json",
    "r"
) as file:

    hackernews_data = json.load(file)


# -------------------------
# Load RSS
# -------------------------

with open(
    "data/rss_news.json",
    "r"
) as file:

    rss_data = json.load(file)

with open(
    "data/github.json",
    "r"
) as file:

    github_data = json.load(file)
# -------------------------
# Calculate
# -------------------------

hackernews_scores = calculate_scores(
    hackernews_data
)

rss_scores = calculate_scores(
    rss_data
)
github_scores = calculate_scores(
    github_data
)

comparison = {

    "HackerNews": hackernews_scores,

    "TechCrunch": rss_scores,

    "GitHub"    :github_scores
}


# -------------------------
# Save
# -------------------------

with open(
    "outputs/source_comparison.json",
    "w"
) as file:

    json.dump(
        comparison,
        file,
        indent=4
    )


# -------------------------
# Print Results
# -------------------------

print("\nSOURCE COMPARISON\n")

for source, scores in comparison.items():

    print(f"\n{source}")

    for category, score in scores.items():

        print(
            f"{category}: {score}"
        )

print(
    "\nComparison saved successfully!"
)
