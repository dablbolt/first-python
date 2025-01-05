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

    # Проверка цвета поля "zip-code" для ошибки
    zip_code = wait_for_element(driver, By.NAME, "zip-code")
    alert_danger_color = 'rgba(248, 215, 218, 1)'  # Цвет фона для ошибки
    zip_color = zip_code.value_of_css_property('background-color')
    assert zip_color == alert_danger_color

    # Проверка цвета остальных полей для успеха
    alert_success_color = 'rgba(209, 231, 221, 1)'  # Цвет фона для успеха
    buttons = [wait_for_element(driver, By.NAME, name) for name in field_names if name != "zip-code"]

    for button in buttons:
        button_color = button.value_of_css_property('background-color')
        assert button_color == alert_success_color
