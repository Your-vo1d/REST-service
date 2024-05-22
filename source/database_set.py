import sqlite3

# Данные первого пользователя
existing_user = {
    "username": "testuser",
    "password": "testpassword",
    "secret_code": "0fbd35e9405c601d4dcc8e12d0a1651d",
    "salary": 60000,
    "promotion_date": "2023-03-21"
}

# Подключение к базе данных
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Вставка данных первого пользователя в таблицу
cursor.execute('''INSERT INTO users 
                  (username, password, secret_code, salary, promotion_date) 
                  VALUES (?, ?, ?, ?, ?)''',
               (existing_user["username"],
                   existing_user["password"],
                   existing_user["secret_code"],
                   existing_user["salary"],
                   existing_user["promotion_date"]))
# Сохранение изменений
conn.commit()

# Закрытие соединения
conn.close()
