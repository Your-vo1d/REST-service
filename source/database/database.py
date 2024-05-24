# source/database/create_db.py
import sqlite3

from source import DATABASE_PATH


# Функция для создания базы данных
def create_database():
    # Подключение к базе данных
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # Создание таблицы users
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    password TEXT,
                    secret_code TEXT,
                    salary REAL,
                    promotion_date DATE)''')
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
