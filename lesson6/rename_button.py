from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("http://uitestingplayground.com/textinput")

input_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "newButtonName"))
)
input_field.send_keys("SkyPro")

submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
submit_button.click()

button_text = submit_button.text
print(button_text)

driver.quit()