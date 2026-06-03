import sqlite3

conn = sqlite3.connect(
    "trend_intelligence.db"
)

cursor = conn.cursor()

cursor.execute(
    """
    SELECT COUNT(*)
    FROM articles
    """
)

count = cursor.fetchone()[0]

print(
    "Total Records:",
    count
)

conn.close()
