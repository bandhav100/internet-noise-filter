import pandas as pd
from collections import Counter

# Load processed data
df = pd.read_csv("data/processed_hackernews.csv")

# Merge all titles into one string
all_titles = " ".join(df["clean_title"].astype(str))

# Convert to lowercase
all_titles = all_titles.lower()

# Split into words
words = all_titles.split()

# Common words remove cheyyadam
stop_words = {
    "the", "and", "for", "with", "from",
    "that", "this", "into", "your", "have",
    "been", "will", "more", "than", "about",
    "what", "when", "where", "why"
}

filtered_words = [
    word for word in words
    if word not in stop_words and len(word) > 3
]

# Count frequency
word_counts = Counter(filtered_words)

# Top 20 keywords
top_words = word_counts.most_common(20)

print("\nTOP 20 TRENDING KEYWORDS\n")

for word, count in top_words:
    print(f"{word}: {count}")
