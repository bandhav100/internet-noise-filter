import pandas as pd
import json

# Load history

df = pd.read_csv(
    "history/trend_history.csv"
)

# Need at least 2 rows

if len(df) < 2:

    print(
        "Not enough history data."
    )

else:

    latest = df.iloc[-1]

    previous = df.iloc[-2]

    changes = {}

    categories = [
        "AI",
        "Programming",
        "Security",
        "Startups"
    ]

    for category in categories:

        changes[category] = int(
            latest[category]
            -
            previous[category]
        )

    print(
        "\nTREND CHANGES\n"
    )

    for category, change in changes.items():

        sign = "+"

        if change < 0:
            sign = ""

        print(
            f"{category}: {sign}{change}"
        )

    with open(
        "outputs/trend_changes.json",
        "w"
    ) as file:

        json.dump(
            changes,
            file,
            indent=4
        )

    print(
        "\nTrend changes saved!"
    )
