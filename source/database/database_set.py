import sqlite3
from source import DATABASE_PATH
from source.models import User


def set_database(user: User):
    # Подключение к базе данных
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # Вставка данных первого пользователя в таблицу
    cursor.execute('''INSERT INTO users 
                    (username, password, secret_code, salary, promotion_date) 
                    VALUES (?, ?, ?, ?, ?)''',
                   (user.username,
                    user.password,
                    user.secret_code,
                    user.salary,
                    user.promotion_date))
    # Сохранение изменений
    conn.commit()

    # Закрытие соединения
    conn.close()
