import sqlite3

conn = sqlite3.connect(
    "trend_intelligence.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT source, COUNT(*)
FROM articles
GROUP BY source
""")

for row in cursor.fetchall():
    print(row)

conn.close()
