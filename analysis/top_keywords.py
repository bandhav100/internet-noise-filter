import pandas as pd
import json
from collections import Counter

df = pd.read_csv("data/processed_hackernews.csv")

all_titles = " ".join(df["clean_title"].astype(str))

words = all_titles.split()

stop_words = {
    "the", "and", "for", "with",
    "this", "that", "from",
    "into", "have", "been"
}

filtered_words = [
    word for word in words
    if word not in stop_words and len(word) > 3
]

word_counts = Counter(filtered_words)

top_words = word_counts.most_common(20)

keyword_data = {}

for word, count in top_words:
    keyword_data[word] = count

with open("outputs/top_keywords.json", "w") as file:
    json.dump(keyword_data, file, indent=4)

print("Top keywords saved!")
