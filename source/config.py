# source/config.py

import os
import sys


# Определение базовой директории проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Определение директории для данных
DATA_DIR = os.path.join(BASE_DIR, 'source', 'data')

# Создание директории для данных, если она не существует
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Путь к базе данных
DATABASE_PATH = os.path.join(DATA_DIR, 'users.db')
