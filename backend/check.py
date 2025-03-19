# Menu db creation code
import sqlite3

conn = sqlite3.connect("menu.db")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS menu (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL
    );
""")

# Insert default data if empty
cursor.execute("SELECT COUNT(*) FROM menu;")
if cursor.fetchone()[0] == 0:
    cursor.executemany(
        "INSERT INTO menu (name, price) VALUES (?, ?);",
        [("Burger", 5.99), ("Pizza", 8.99), ("Pasta", 7.49), ("Salad", 4.99)]
    )
    conn.commit()

print("Database and table initialized successfully!")

conn.close()
