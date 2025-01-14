from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self._driver = driver

class FormPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def open(self):
        self._driver.get(self.url)  # Открываем страницу формы

    def fill_form(self, field_names, values):
        # Заполняем форму, перебирая имена полей и соответствующие значения
        for name, value in zip(field_names, values):
            self.wait_for_element(By.NAME, name).send_keys(value)  # Находим элемент по имени и вводим значение

    def submit(self):
        # Нажимаем кнопку "Submit"
        self._driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    def wait_for_element(self, by, value):
        # Ожидаем, пока элемент станет видимым на странице
        return WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((by, value)))

    def wait_for_company_element(self):
        # Ожидаем появления элемента с ID "company"
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_all_elements_located((By.ID, "company"))
        )

    def get_zip_code_class(self):
        # Получаем класс элемента с ID "zip-code"
        return self._driver.find_element(By.ID, "zip-code").get_attribute("class")

    def get_field_class(self, field_id):
        # Получаем класс элемента по его ID
        return self._driver.find_element(By.ID, field_id).get_attribute("class")
