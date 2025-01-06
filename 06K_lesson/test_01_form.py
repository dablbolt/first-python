import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def wait_for_element(driver, by, value):
    return WebDriverWait(driver, 10).until(EC.visibility_of_element_located((by, value)))

def test_01_form(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение формы
    field_names = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "zip-code", "city", "country",
        "job-position", "company"
    ]

    values = [
        "Иван", "Петров", "Ленина, 55-3", "test@skypro.com",
        "+7985899998787", "", "Москва", "Россия",
        "QA", "SkyPro"
    ]

    for name, value in zip(field_names, values):
        wait_for_element(driver, By.NAME, name).send_keys(value)

    # Нажимаем кнопку "Submit"
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.ID, "company"))
    )

    assert "danger" in driver.find_element(By.ID, "zip-code").get_attribute(
        "class"), "Поле Zip code должно быть подсвечено красным"

    fields = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company"
    ]
    for field_id in fields:
        field = driver.find_element(By.ID, field_id)
        assert "success" in driver.find_element(By.ID, field_id).get_attribute(
            "class"), f"Поле {field_id} должно быть подсвечено зеленым"

    print("Все проверки пройдены успешно!")

    driver.quit()
