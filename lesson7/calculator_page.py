from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self._driver = driver

class CalculatorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def open(self):
        # Открываем страницу калькулятора
        self._driver.get(self.url)

    def set_delay(self, delay):
        # Устанавливаем задержку
        delay_input = self._driver.find_element(By.CSS_SELECTOR, "input#delay")
        delay_input.clear()  # Очищаем поле задержки
        delay_input.send_keys(delay)  # Вводим значение задержки

    def click_button(self, button_text):
        # Нажимаем на кнопку калькулятора
        button = self._driver.find_element(By.XPATH, f"//span[text()='{button_text}']")
        button.click()

    def get_result(self):
        # Получаем результат вычисления
        return self._driver.find_element(By.CSS_SELECTOR, ".screen").text

    def wait_for_result(self, expected_result):
        # Ожидаем, пока результат появится на экране
        WebDriverWait(self._driver, 50).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), expected_result)
        )