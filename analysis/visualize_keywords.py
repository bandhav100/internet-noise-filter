import json
import matplotlib.pyplot as plt

with open("outputs/top_keywords.json", "r") as file:
    keywords = json.load(file)

labels = list(keywords.keys())
values = list(keywords.values())

plt.figure(figsize=(14, 7))

plt.bar(labels, values)

plt.xticks(rotation=45)

plt.title("Top 20 Trending Keywords")
plt.xlabel("Keywords")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig("outputs/top_keywords_chart.png")

plt.show()
