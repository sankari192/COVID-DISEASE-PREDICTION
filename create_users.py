import sqlite3
import os

# Step 1: Create only the 'db' folder (not the file)
db_folder = os.path.join("db")
os.makedirs(db_folder, exist_ok=True)

# Step 2: Point to the database FILE inside the folder
db_path = os.path.join(db_folder, 'users.db')

# Step 3: Now connect to database file (this will create it if it doesn't exist)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# Optional: Add default user
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", "12345"))

conn.commit()
conn.close()

print("✅ User table created and default user inserted.")
