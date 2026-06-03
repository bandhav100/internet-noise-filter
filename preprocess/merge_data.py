import json

# Load HackerNews

with open(
    "data/hackernews.json",
    "r"
) as file:

    hackernews = json.load(file)

# Load RSS

with open(
    "data/rss_news.json",
    "r"
) as file:

    rss = json.load(file)

# Load GitHub

with open(
    "data/github.json",
    "r"
) as file:

    github = json.load(file)

# Merge

merged_data = (
    hackernews
    + rss
    + github
)

# Save

with open(
    "data/merged_data.json",
    "w"
) as file:

    json.dump(
        merged_data,
        file,
        indent=4
    )

print("Merge Successful!")

print(
    "Total Records:",
    len(merged_data)
)
