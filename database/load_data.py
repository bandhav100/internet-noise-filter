import sqlite3
import json

conn = sqlite3.connect(
    "trend_intelligence.db"
)

cursor = conn.cursor()

with open(
    "data/merged_data.json",
    "r"
) as file:

    data = json.load(file)

for item in data:

    title = item.get(
        "title",
        ""
    )

    source = item.get(
        "source",
        "Unknown"
    )

    cursor.execute(
        """
        INSERT INTO articles
        (
            title,
            source
        )
        VALUES
        (?, ?)
        """,
        (
            title,
            source
        )
    )

conn.commit()

conn.close()

print(
    "Data inserted successfully!"
)
