from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # открывает хром
driver.maximize_window()  # делать окно в макс размере

driver.get("https://the-internet.herokuapp.com/add_remove_elements/") # заходим на сайт

# пять раз кликаем на кнопку "Add Element"
add_element_button_locator = "button"  # локатор кнопки "Add Element"
for _ in range(5):
    add_element_button = driver.find_element(By.CSS_SELECTOR, add_element_button_locator)
    add_element_button.click()  # клик по кнопке

# собираем со страницы список кнопок "Delete"
delete_buttons_locator = "button.added-manually"  # локатор кнопок "Delete"
delete_buttons = driver.find_elements(By.CSS_SELECTOR, delete_buttons_locator)

# выводим на экран размер списка
print("Количество кнопок 'Delete':", len(delete_buttons))

sleep(5)
