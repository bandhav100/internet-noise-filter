import requests
import json

url = "https://www.reddit.com/r/artificial/hot.json?limit=50"

headers = {
    "User-Agent": "TrendIntelligenceBot/1.0"
}

response = requests.get(
    url,
    headers=headers
)

print("Status Code:", response.status_code)

data = response.json()

posts = []

for post in data["data"]["children"]:

    post_data = post["data"]

    posts.append({

        "title": post_data.get("title"),

        "author": post_data.get("author"),

        "score": post_data.get("score"),

        "source": "reddit"

    })

with open(
    "data/reddit.json",
    "w"
) as file:

    json.dump(
        posts,
        file,
        indent=4
    )

print("Reddit data saved!")
print("Total posts:", len(posts))
