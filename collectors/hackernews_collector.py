import requests
import json

url = "https://hacker-news.firebaseio.com/v0/topstories.json"

response = requests.get(url)

story_ids = response.json()

print(story_ids[:30])

stories = []

LIMIT =200
for story_id in story_ids[:LIMIT]:

    story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"

    story_response = requests.get(story_url)

    story_data = story_response.json()

    story = {
    "title": story_data.get("title"),
    "author": story_data.get("by"),
    "score": story_data.get("score"),
    "url": story_data.get("url"),
    "source": "HackerNews"
}
    stories.append(story)

    print("Collected:", story["title"])

with open("data/hackernews.json", "w") as file:
    json.dump(stories, file, indent=4)

print("Data saved successfully!")
