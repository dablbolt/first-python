from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Инициализация драйвера Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # открывает хром
driver.maximize_window()  # делает окно в максимальном размере

# Переход на сайт
driver.get("http://uitestingplayground.com/classattr")  # заходим на сайт

# Кликаем на синюю кнопку с классом 'btn-primary'
blue_button_locator = ".btn-primary"  # локатор синей кнопки
blue_button = driver.find_element(By.CSS_SELECTOR, blue_button_locator)
blue_button.click()  # клик по кнопке

# Запускаем скрипт три раза подряд
print("Скрипт выполнен. Запускаем его еще два раза.")

sleep(5)