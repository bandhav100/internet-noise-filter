import requests
from bs4 import BeautifulSoup
import json

url = "https://github.com/trending"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(
    url,
    headers=headers
)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

repos = soup.select("article.Box-row")

data = []

for repo in repos:

    title = repo.h2.text.strip()

    data.append({
        "title": title,
        "source": "GitHub"
    })

with open(
    "data/github.json",
    "w"
) as file:

    json.dump(
        data,
        file,
        indent=4
    )

print(
    f"Collected {len(data)} repositories"
)
