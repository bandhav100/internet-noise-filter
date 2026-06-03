import requests
import json

# Fetch top story IDs
url = "https://hacker-news.firebaseio.com/v0/topstories.json"

response = requests.get(url)

story_ids = response.json()

print("Fetching story data...\n")

stories = []

# Fetch story details
for story_id in story_ids[:10]:

    story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"

    story_response = requests.get(story_url)

    story_data = story_response.json()

    # Create structured story object
    story = {
        "title": story_data.get("title"),
        "author": story_data.get("by"),
        "score": story_data.get("score"),
        "url": story_data.get("url")
    }

    stories.append(story)

    print("Collected:", story["title"])

# Save data to JSON file
with open("data/hackernews.json", "w") as file:
    json.dump(stories, file, indent=4)

print("\nData saved successfully!")
