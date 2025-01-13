import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage  # Импортируем класс страницы калькулятора


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_calculator(driver):
    calculator_page = CalculatorPage(driver)

    # Открываем страницу калькулятора
    calculator_page.open()

    # Устанавливаем задержку
    calculator_page.set_delay("45")

    # Выполняем нажатия на кнопки 7 + 8 =
    calculator_page.click_button("7")
    calculator_page.click_button("+")
    calculator_page.click_button("8")
    calculator_page.click_button("=")

    # Ожидаем результат
    calculator_page.wait_for_result("15")

    # Проверка результата
    result = calculator_page.get_result()
    assert int(result) == 15, f"Ожидалось 15, но получено {result}"

    print("Тест пройден успешно!")