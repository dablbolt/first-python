from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class BasePage:
    def __init__(self, driver: webdriver):
        self._driver = driver  # Тип: webdriver

class FormPage(BasePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def open(self) -> None:
        """Открывает страницу формы."""
        self._driver.get(self.url)  # Тип возвращаемого значения: None

    def fill_form(self, field_names: list, values: list) -> None:
        """Заполняет форму.

        Параметры:
        field_names: Список строк с именами полей.
        values: Список строк с значениями для полей.
        """
        for name, value in zip(field_names, values):
            self.wait_for_element(By.NAME, name).send_keys(value)

    def submit(self) -> None:
        """Нажимает кнопку 'Submit'."""
        self._driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    def wait_for_element(self, by: By, value: str) -> webdriver:
        """Ожидает, пока элемент станет видимым на странице.

        Параметры:
        by: Метод поиска элемента.
        value: Строка с значением для поиска.
        Возвращает:
        webdriver: Элемент, который стал видимым.
        """
        return WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((by, value)))

    def wait_for_company_element(self) -> None:
        """Ожидает появления элемента с ID 'company'."""
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_all_elements_located((By.ID, "company"))
        )

    def get_zip_code_class(self) -> str:
        """Получает класс элемента с ID 'zip-code'.

        Возвращает:
        str: Класс элемента.
        """
        return self._driver.find_element(By.ID, "zip-code").get_attribute("class")

    def get_field_class(self, field_id: str) -> str:
        """Получает класс элемента по его ID.

        Параметры:
        field_id: Строка с ID элемента.
        Возвращает:
        str: Класс элемента.
        """
        return self._driver.find_element(By.ID, field_id).get_attribute("class")
