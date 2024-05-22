import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                secret_code TEXT,
                salary REAL,
                promotion_date DATE)''')
conn.commit()