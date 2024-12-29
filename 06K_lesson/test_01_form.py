import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Фикстура для инициализации драйвера
@pytest.fixture
def driver():
    # Инициализация драйвера Chrome
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver  # Возвращаем драйвер для использования в тестах
    driver.quit()  # Закрываем драйвер после завершения теста


def test_01_form(driver):
    # Открываем страницу с формой
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение формы
    driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").send_keys("")  # Оставляем пустым
    driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys("SkyPro")

    # Нажимаем кнопку "Submit"
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Проверка цвета поля "Zip code"
    alert_danger_color = "rgba(248, 215, 218, 1)"  # Ожидаемый цвет для ошибки
    color_zip = driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").value_of_css_property("background-color")
    assert color_zip == alert_danger_color, f"Expected {alert_danger_color}, but got {color_zip}"

    # Проверка цвета остальных полей
    alert_success_color = "rgba(209, 231, 221, 1)"  # Ожидаемый цвет для успешного заполнения
    fields = [
        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "country", "job-position", "company"
    ]

    for field_name in fields:
        field = driver.find_element(By.CSS_SELECTOR, f"input[name='{field_name}']")
        field_color = field.value_of_css_property("background-color")
        assert field_color == alert_success_color, f"Expected {alert_success_color} for {field_name}, but got {field_color}"