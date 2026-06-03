import json

from sklearn.feature_extraction.text import (
    TfidfVectorizer,
    ENGLISH_STOP_WORDS
)

with open(
    "data/merged_data.json",
    "r"
) as file:

    data = json.load(file)

titles = []

for item in data:

    title = item.get(
        "title",
        ""
    )

    if title:

        titles.append(title)

custom_stopwords = list(

    ENGLISH_STOP_WORDS.union(

        {

            "hn",
            "show",
            "ask",
            "new",
            "using",

            "2023",
            "2024",
            "2025",
            "2026",
            "2004",

            "one",
            "two",
            "three",
            "first",
            "second",

            "made",
            "make",
            "like",
            "get",
            "build",
            "building",
            "used",
            "use",

            "year",
            "years",
            "public",
            "free",
            "video",
            "access",
            "hits",
            "zero",
            "open",
            "based",
            "language",
            "services",
            "engineering",
            "need",
            "shows",
            "takes",
            "engine",
            "chip",
            "laptop",
            "system",
            "tool",
            "tools",
            "platform",
            "software", 
            "project",

            "2016",
            "2017",
            "2018",
            "2019",
            "2020",
            "2021",
            "2022",
            "american",
            "says",
            "scratch",
            "bit",
            "app",
            "workflows",
            "hiring"

        }

    )
)

vectorizer = TfidfVectorizer(
    stop_words=custom_stopwords,
    max_features=100,
    min_df=2,
    ngram_range=(1, 2)
)

X = vectorizer.fit_transform(
    titles
)

keywords = vectorizer.get_feature_names_out()

scores = X.sum(
    axis=0
).A1

results = list(
    zip(
        keywords,
        scores
    )
)

results.sort(
    key=lambda x: x[1],
    reverse=True
)

print(
    "\nTOP NLP TOPICS\n"
)

for word, score in results[:20]:

    print(
        f"{word}: {round(score, 2)}"
    )

top_topics = {}

for word, score in results[:20]:

    top_topics[word] = round(
        float(score),
        2
    )

with open(
    "outputs/topic_models.json",
    "w"
) as file:

    json.dump(
        top_topics,
        file,
        indent=4
    )

print(
    "\nTopics saved successfully!"
)
