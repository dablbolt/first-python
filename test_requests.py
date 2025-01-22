import requests

base_url = "https://x-clients-be.onrender.com"

def test_simple_req():
    resp = requests.get(base_url + '/company')
    
    # Проверка успешного ответа
    assert resp.status_code == 200
    
    response_body = resp.json()  # Вызов метода json()
    first_company = response_body[0]  # Предполагается, что это список
    assert resp.headers["Content-Type"] == "application/json; charset=utf-8"
    assert first_company["name"] == "Барбершоп 'ЦирюльникЪ'"

def test_auth():
    creds = {
        "username": "bloom",
        "password": "fire-fairy"
    }
    resp = requests.post(base_url + '/auth/login', json=creds)
    
    # Проверка успешного ответа
    assert resp.status_code == 201  # Обычно для успешной аутентификации ожидается 200
    token = resp.json()["userToken"]  # Вызов метода json()

def test_create_company():
    creds = {
        "username": "bloom",
        "password": "fire-fairy"
    }
    company = {
        "name": "python",
        "discription": "requests"
    }

    # Авторизация
    resp = requests.post(base_url + '/auth/login', json=creds)
    assert resp.status_code == 201  # Проверка успешной аутентификации
    token = resp.json()["userToken"]  # Вызов метода json()

    # Создание
    my_headers = {
        "x-client-token": token
    }
    
    resp = requests.post(base_url + '/company', json=company, headers=my_headers)
    assert resp.status_code == 201  # Проверка успешного создания компании