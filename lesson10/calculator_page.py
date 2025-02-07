from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class BasePage:
    def __init__(self, driver: webdriver):
        self.driver = driver  # Тип: webdriver

class CalculatorPage(BasePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)  # Вызов конструктора родительского класса
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def open(self) -> None:
        """Открывает страницу калькулятора."""
        self.driver.get(self.url)

    def set_delay(self, delay: str) -> None:
        """Устанавливает задержку.

        Параметры:
        delay: Задержка в виде строки.
        Возвращает:
        None
        """
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "input#delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_button(self, button_text: str) -> None:
        """Нажимает на кнопку калькулятора.

        Параметры:
        button_text: Текст кнопки.
        Возвращает:
        None
        """
        button = self.driver.find_element(By.XPATH, f"//span[text()='{button_text}']")
        button.click()

    def get_result(self) -> str:
        """Получает результат вычисления.

        Возвращает:
        str: Результат вычисления как строка.
        """
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text

    def wait_for_result(self, expected_result: str) -> None:
        """Ожидает, пока результат появится на экране.

        Параметры:
        expected_result: Строка с ожидаемым результатом.
        Возвращает:
        None
        """
        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), expected_result)
        )
