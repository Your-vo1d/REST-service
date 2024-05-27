import sqlite3

from users_data import valid_user

from source import DATABASE_PATH
from source.models import User


# Функция добавление работника в базу данных
def set_database(user: User):
    try:
        # Подключение к базе данных
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()

        # Проверка существования таблицы users
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='users';"
        )
        if cursor.fetchone() is None:
            raise Exception("Таблица 'users' не существует в базе данных.")

        # Вставка данных первого пользователя в таблицу
        cursor.execute(
            """INSERT INTO users 
                        (username, password, secret_code, salary, promotion_date) 
                        VALUES (?, ?, ?, ?, ?)""",
            (
                user.username,
                user.password,
                user.secret_code,
                user.salary,
                user.promotion_date,
            ),
        )
        # Сохранение изменений
        conn.commit()
    # Обработка исключений
    except sqlite3.Error as e:
        print(f"Ошибка при работе с базой данных: {e}")
    except Exception as e:
        print(f"Общая ошибка: {e}")
    finally:
        # Закрытие соединения
        if conn:
            conn.close()


if __name__ == "__main__":
    valid_user = User(**valid_user)
    set_database(valid_user)
