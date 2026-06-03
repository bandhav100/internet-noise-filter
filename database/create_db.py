import sqlite3

conn = sqlite3.connect(
    "trend_intelligence.db"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS articles (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    title TEXT,

    source TEXT

)
""")

conn.commit()

conn.close()

print(
    "Database created successfully!"
)
