import requests
import pytest
from source import BASE_URL
from source.database.users_data import valid_user, invalid_user


# Тест для входа пользователя
def test_login():
    # Отправляем запрос на вход с правильными учетными данными
    response = requests.post(f"{BASE_URL}/login", json=valid_user)
    assert response.status_code == 200  # Обработка ответа сервиса (200)
    data = response.json()
    assert "message" in data
    assert "secret_key" in data

    # Отправляем запрос на вход с неправильным паролем
    invalid_credentials = valid_user.copy()
    invalid_credentials["password"] = "wrongpassword"
    response = requests.post(f"{BASE_URL}/login", json=invalid_credentials)
    assert response.status_code == 401
    data = response.json()
    assert "detail" in data
    assert data["detail"] == "Password does not match"

    # Отправляем запрос на вход с несуществующим пользователем
    response = requests.post(f"{BASE_URL}/login", json=invalid_user)
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert data["detail"] == "User not found"


@pytest.fixture(scope="module")
def secret_key():
    responce = requests.post(f"{BASE_URL}/login", json=valid_user)
    data = responce.json()
    return data["secret_key"]


def test_information(secret_key):
    response = requests.get(
        f"{BASE_URL}/information", params={"secret_code": secret_key}
    )
    assert response.status_code == 200
    data = response.json()
    assert "username" in data
    assert "salary" in data
    assert "promotion_date" in data

    # Выводим информацию о пользователе в терминал
    print("Имя пользователя:", data["username"])
    print("Зарплата:", data["salary"])
    print("Дата повышения:", data["promotion_date"])

    # Отправляем запрос на получение информации с неправильным секретным кодом
    response = requests.get(
        f"{BASE_URL}/information", params={"secret_code": "invalid_secret"}
    )
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert data["detail"] == "Invalid or expired secret code"
