import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def test_calculator():
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay = driver.find_element(By.CSS_SELECTOR, 'input#delay')
    delay.send_keys('45')

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # Ожидаем, пока результат появится на экране
    WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    # результат
    result = driver.find_element(By.CSS_SELECTOR, ".screen").text

    # Проверка результата
    assert result == "15", f"Expected result to be '15', but got '{result}'"


driver.quit()