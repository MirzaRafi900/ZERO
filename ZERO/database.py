import sqlite3

def init_db():

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS memory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        memory TEXT NOT NULL
    )
    """)

# Temporary Test

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    print(cursor.fetchall())


    conn.commit()

    conn.close()

if __name__ == "__main__":
    init_db()