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

    # Заполнение формы с ожиданием
    wait_for_element(driver, By.CSS_SELECTOR, "input[name='first-name']").send_keys("Иван")
    wait_for_element(driver, By.CSS_SELECTOR, "input[name='last-name']").send_keys("Петров")
    wait_for_element(driver, By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
    wait_for_element(driver, By.CSS_SELECTOR, "input[name='e-mail']").send_keys("test@skypro.com")
    wait_for_element(driver, By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")
    wait_for_element(driver, By.CSS_SELECTOR, "input[name='zip-code']").send_keys("")  # Оставляем пустым
    wait_for_element(driver, By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
    wait_for_element(driver, By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
    wait_for_element(driver, By.CSS_SELECTOR, "input[name='job-position']").send_keys("QA")
    wait_for_element(driver, By.CSS_SELECTOR, "input[name='company']").send_keys("SkyPro")

    # Нажимаем кнопку "Submit"
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Проверка цвета поля "Zip code"
    alert_danger_color = "rgba(248, 215, 218, 1)"  # Ожидаемый цвет для ошибки
    color_zip = wait_for_element(driver, By.CSS_SELECTOR, "input[name='zip-code']").value_of_css_property("background-color")
    assert color_zip == alert_danger_color, f"Expected {alert_danger_color}, but got {color_zip}"

    # Проверка цвета остальных полей
    alert_success_color = "rgba(209, 231, 221, 1)"  # Ожидаемый цвет для успешного заполнения
    fields = [
        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "country", "job-position", "company"
    ]

    for field_name in fields:
        field = wait_for_element(driver, By.CSS_SELECTOR, f"input[name='{field_name}']")
        field_color = field.value_of_css_property("background-color")
        assert field_color == alert_success_color, f"Expected {alert_success_color} for {field_name}, but got {field_color}"

driver.quit()