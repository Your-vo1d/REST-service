from fastapi import FastAPI, HTTPException
from database import cursor, conn
from model import User
import secrets
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio

app = FastAPI()



# Функция для обновления секретных кодов
async def update_secret_codes():
    while True:
        cursor.execute("SELECT username FROM users")
        users = cursor.fetchall()
        for user in users:
            new_secret_code = secrets.token_hex(16)
            cursor.execute(
                "UPDATE users SET secret_code = ? WHERE username = ?", (
                    new_secret_code, user[0])
            )
        conn.commit()
        await asyncio.sleep(3600)  # Ожидание 1 час перед следующим обновлением


@app.post("/login")
async def login(user: User):
    cursor.execute("SELECT * FROM users WHERE username=?", (user.username,))
    db_user = cursor.fetchone()
    if db_user:
        db_password = db_user[2]
        if user.password == db_password:
            return {"message": "User exists and password matches", "secret_key": db_user[3]}
        else:
            raise HTTPException(
                status_code=401, detail="Password does not match")
    else:
        raise HTTPException(status_code=404, detail="User not found")


# Создаем и запускаем планировщик
scheduler = AsyncIOScheduler()
scheduler.add_job(update_secret_codes, "interval", hours=1)
scheduler.start()

# Запускаем цикл обновления секретных кодов при старте приложения
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(update_secret_codes())
