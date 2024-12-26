from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/login")

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "username"))
).send_keys("tomsmith")
sleep(1)

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "password"))
).send_keys("SuperSecretPassword!")
sleep(1)

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
).click()

sleep(5)