import pytest
import requests

BASE_URL = "https://ru.yougile.com"
API_KEY = "IK+4L2F9ClYmiRzgfwLJfCddAdTnd-qen+xowzRbb4BcHtWF3HTikxWSHTMy-i50"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# Данные для авторизации
AUTH_DATA = {
    "login": "dablbolt@mail.ru",
    "password": "1021997m",
    "companyId": "7031ab99-d0ed-4f36-9ecf-643e0e025ac0"
}

# Фикстура для получения ID проекта
@pytest.fixture
def project_id():
    # Создаем проект 
    payload = {"title": "Новый проект для домашки24"}
    response = requests.post(f"{BASE_URL}/api-v2/projects", headers=HEADERS, json=payload)
    assert response.status_code == 201
    return response.json()["id"]

# Тесты для [POST] /api-v2/projects
def test_create_project_positive():
    payload = {"title": "Новый проект для домашки24"}
    response = requests.post(f"{BASE_URL}/api-v2/projects", headers=HEADERS, json=payload)
    assert response.status_code == 201
    assert "id" in response.json()

def test_create_project_negative():
    # Отправляем пустой запрос
    payload = {}
    response = requests.post(f"{BASE_URL}/api-v2/projects", headers=HEADERS, json=payload)
    assert response.status_code == 400

# Тесты для [GET] /api-v2/projects
def test_get_projects_list_positive():
    response = requests.get(f"{BASE_URL}/api-v2/projects", headers=HEADERS)
    assert response.status_code == 200
    assert "content" in response.json()

def test_get_projects_list_negative():
    # Используем неверный метод (POST вместо GET)
    response = requests.post(f"{BASE_URL}/api-v2/projects", headers=HEADERS)
    assert response.status_code == 400  # Method Not Allowed

# Тесты для [GET] /api-v2/projects/{id}
def test_get_project_by_id_positive(project_id):
    response = requests.get(f"{BASE_URL}/api-v2/projects/{project_id}", headers=HEADERS)
    assert response.status_code == 200
    assert response.json()["id"] == project_id

def test_get_project_by_id_negative():
    # Используем несуществующий ID
    non_existent_id = "несуществующий_id"
    response = requests.get(f"{BASE_URL}/api-v2/projects/{non_existent_id}", headers=HEADERS)
    assert response.status_code == 404

# Тесты для [PUT] /api-v2/projects/{id}
def test_add_user_to_project_positive(project_id):
    payload = {
        "users": {
            "138c8f2d-ed6a-4115-a340-e339c8440152": "admin"
        }
    }
    response = requests.put(f"{BASE_URL}/api-v2/projects/{project_id}", headers=HEADERS, json=payload)
    assert response.status_code == 200
    assert "id" in response.json()

def test_add_user_to_project_negative(project_id):
    # Отправляем пустой запрос
    payload = {}
    response = requests.put(f"{BASE_URL}/api-v2/projects/{project_id}", headers=HEADERS, json=payload)
    assert response.status_code == 200

# Тест для получения ключа API (негативный, так как лимит исчерпан)
def test_get_api_key_negative():
    response = requests.post(f"{BASE_URL}/api-v2/auth/keys", json=AUTH_DATA)
    assert response.status_code == 403  # Forbidden