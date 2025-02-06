import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


@allure.title("Тест для работы с калькулятором")
@allure.description("Тест проверяет функциональность калькулятора")
@allure.feature("Калькулятор")
@allure.severity("blocker")
def test_calculator(driver):
    with allure.step("Создаём объект страницы калькулятора"):
        calculator_page = CalculatorPage(driver)

    with allure.step("Открываем страницу калькулятора"):
        calculator_page.open()

    with allure.step("Устанавливаем задержку"):
        calculator_page.set_delay("45")

    with allure.step("Выполняем нажатия на кнопки 7 + 8 ="):
        calculator_page.click_button("7")
        calculator_page.click_button("+")
        calculator_page.click_button("8")
        calculator_page.click_button("=")

    with allure.step("Ожидаем результат"):
        calculator_page.wait_for_result("15")

    with allure.step("Проверяем результат"):
        result = calculator_page.get_result()
        assert int(result) == 15, f"Ожидалось 15, но получено {result}"

    print("Тест пройден успешно!")
