import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from form_page import FormPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


@allure.title("Тест для заполнения формы")
@allure.description("Тест проверяет корректность заполнения формы")
@allure.feature("Форма заполнения")
@allure.severity("blocker")
def test_01_form(driver):
    with allure.step("Создаём объект страницы"):
        form_page = FormPage(driver)

    with allure.step("Открываем страницу"):
        form_page.open()

    with allure.step("Заполняем форму"):
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

        form_page.fill_form(field_names, values)

    with allure.step("Нажатие кнопки"):
        form_page.submit()

    form_page.wait_for_company_element()

    with allure.step("Проверка, что поле Zip code подсвечено красным"):
        assert "danger" in form_page.get_zip_code_class(), "Поле Zip code должно быть подсвечено красным"

    fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]
    for field_id in fields:
        with allure.step(f"Проверка поля {field_id} на успешное заполнение"):
            assert "success" in form_page.get_field_class(field_id), f"Поле {field_id} должно быть подсвечено зеленым"

    print("Все проверки пройдены успешно!")
