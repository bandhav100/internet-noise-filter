import pandas as pd
import json
import re
from collections import Counter

# Load merged dataset
with open("data/merged_data.json", "r") as file:
    data = json.load(file)

# Extract titles
titles = []

for item in data:

    title = item.get("title")

    if title:
        titles.append(title.lower())


# Join all titles
all_text = " ".join(titles)

# Remove punctuation and numbers
all_text = re.sub(r"[^a-zA-Z\s]", " ", all_text)

# Split into words
words = all_text.split()


# Stop words
stop_words = {
    "the", "and", "for", "with",
    "from", "this", "that",
    "have", "been", "will",
    "just", "more", "than",
    "they", "them", "their",
    "your", "what", "when",
    "where", "using", "show",
    "like", "into", "about",
    "over", "under", "after",
    "before", "today", "last",
    "new", "how", "why",
    "can", "not", "all",
    "are", "was", "were",
    "its", "our", "you",
    "his", "her", "who"
}

# Remove noise words
clean_words = []

for word in words:

    if len(word) < 4:
        continue

    if word in stop_words:
        continue

    clean_words.append(word)


# Count frequencies
word_counts = Counter(clean_words)

# Top 20
top_trends = word_counts.most_common(20)

print("\nTOP 20 TRENDING KEYWORDS\n")

trend_data = {}

for word, count in top_trends:

    print(f"{word}: {count}")

    trend_data[word] = count


# Save results
with open(
    "outputs/top_trends_v2.json",
    "w"
) as file:

    json.dump(
        trend_data,
        file,
        indent=4
    )

print("\nTop trends saved!")
