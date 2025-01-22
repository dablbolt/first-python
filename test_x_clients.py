import requests

base_url = "https://x-clients-be.onrender.com"

def get_company_list(params_to_add=None):
    resp = requests.get(base_url + '/company', params=params_to_add)
    return resp.json()  # Вызов метода json()

def get_token(user='bloom', password='fire-fairy'):
    creds = {
        "username": user,
        "password": password
    }
    resp = requests.post(base_url + '/auth/login', json=creds)
    return resp.json()["userToken"]  # Вызов метода json() и обращение к токену

def create_company(name, description=''):
    company = {
        "name": name,
        "discription": discription
    } 

    my_headers = {}
    my_headers = {"x-client-token": get_token()} 
    return resp.json{}


def test_get_companies():
    body = get_company_list()
    assert len(body) > 0 
    # assert resp.status_code == 200  

def test_get_active_companies():
    # Получение списка компаний
    full_list = get_company_list()

    # Получение списка всех активных компаний
    filtered_list = get_company_list(params_to_add={'active': 'true'})

    # Проверить, что список 1 > списка 2
    assert len(full_list) > len(filtered_list)

def test_add_new():
    # получить количество компаний
    body = get_company_list()
    len_before = len(body)

    # создать новую компанию
    company = {
        "name": "python",
        "discription": "requests"
    }    

    my_headers = {}
    my_headers = {
        "x-client-token": get_token()  
    }
    
    resp = requests.post(base_url + '/company', json=company, headers=my_headers)

    # получить количество компаний
    body = get_company_list()
    len_after = len(body)

    # проверить, что + 1
    assert len_after - len_before == 1