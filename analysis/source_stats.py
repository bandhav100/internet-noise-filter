import json

with open("data/merged_data.json", "r") as file:
    data = json.load(file)

sources = {}

for item in data:

    source = item.get("source", "HackerNews")

    sources[source] = sources.get(source, 0) + 1

with open("outputs/source_stats.json", "w") as file:
    json.dump(sources, file, indent=4)

print(sources)
