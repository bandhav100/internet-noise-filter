import feedparser
import json

feed_url = "https://techcrunch.com/feed/"

feed = feedparser.parse(feed_url)

articles = []

for entry in feed.entries[:20]:

    articles.append({
        "title": entry.title,
        "link": entry.link,
        "source": "TechCrunch"
    })

with open(
    "data/rss_news.json",
    "w"
) as file:

    json.dump(
        articles,
        file,
        indent=4
    )

print("RSS data saved!")
print("Articles:", len(articles))
