import json

with open(
    "outputs/trend_scores.json",
    "r"
) as file:

    trend_scores = json.load(file)

with open(
    "outputs/topic_models.json",
    "r"
) as file:

    topics = json.load(file)

total_score = sum(
    trend_scores.values()
)

ai_score = trend_scores.get(
    "AI",
    0
)

ai_percentage = round(
    (ai_score / total_score) * 100,
    1
)

top_topics = list(
    topics.keys()
)

brief = []

brief.append(
    "EXECUTIVE MARKET BRIEF\n"
)

brief.append(
    f"AI continues to dominate technology discourse, "
    f"representing approximately {ai_percentage}% "
    f"of tracked trend signals.\n"
)

if "nvidia" in top_topics:

    brief.append(
        "NVIDIA remains a major ecosystem driver, "
        "reflecting continued demand for AI compute infrastructure.\n"
    )

if "openai" in top_topics:

    brief.append(
        "OpenAI continues to influence discussion volumes "
        "through model releases and agent-based workflows.\n"
    )

if "github" in top_topics:

    brief.append(
        "GitHub activity suggests increasing developer interest "
        "in AI tooling and automation frameworks.\n"
    )

brief.append(
    f"Leading topics this cycle include: "
    f"{', '.join(top_topics[:8])}."
)

with open(
    "outputs/executive_brief.txt",
    "w"
) as file:

    file.write(
        "\n".join(brief)
    )

print(
    "\n".join(brief)
)
