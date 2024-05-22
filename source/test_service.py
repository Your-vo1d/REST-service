import requests

# URL
base_url = "http://127.0.0.1:8000"

valid_user = {
    "username": "testuser",
    "password": "testpassword",
    "secret_code": "0fbd35e9405c601d4dcc8e12d0a1651d",
    "salary": 0,
    "promotion_date": ""
}

invalid_user = {
    "username": "invaliduser",
    "password": "wrongpassword",
    "secret_code": "wrongsecret",
    "salary": 60000.0,
    "promotion_date": "2022-12-31"
}

# Тест для входа пользователя
def test_login():
    # Отправляем запрос на вход с правильными учетными данными
    response = requests.post(f"{base_url}/login", json=valid_user)
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "secret_key" in data

    # Отправляем запрос на вход с неправильным паролем
    invalid_credentials = valid_user.copy()
    invalid_credentials["password"] = "wrongpassword"
    response = requests.post(f"{base_url}/login", json=invalid_credentials)
    assert response.status_code == 401
    data = response.json()
    assert "detail" in data
    assert data["detail"] == "Password does not match"

    # Отправляем запрос на вход с несуществующим пользователем
    response = requests.post(f"{base_url}/login", json=invalid_user)
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert data["detail"] == "User not found"

if __name__ == "__main__":
    test_login()
