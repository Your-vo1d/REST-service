# Используем официальный образ Python с Docker Hub
FROM python:3.12-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы зависимостей в рабочую директорию
COPY pyproject.toml poetry.lock /app/

# Устанавливаем Poetry
RUN pip install poetry

# Устанавливаем зависимости
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Копируем остальной код приложения в рабочую директорию
COPY . /app

# Открываем порт, на котором работает приложение
EXPOSE 8000

# Запускаем приложение FastAPI с Uvicorn
CMD ["uvicorn", "source.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
