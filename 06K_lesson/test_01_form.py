from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    driver.get("http://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    WebDriverWait(driver, 50).until(
        EC.presence_of_all_elements_located((By.NAME, "company"))
    )

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "zip-code").send_keys("")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.ID, "company"))
    )

    assert "danger" in driver.find_element(By.ID, "zip-code").get_attribute(
        "class"), "Поле Zip code должно быть подсвечено красным"

    fields = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company"
    ]
    for field_id in fields:
        field = driver.find_element(By.ID, field_id)
        assert "success" in driver.find_element(By.ID, field_id).get_attribute(
            "class"), f"Поле {field_id} должно быть подсвечено зеленым"

    print("Все проверки пройдены успешно!")

finally:

    driver.quit()