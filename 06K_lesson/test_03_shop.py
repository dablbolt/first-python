import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from  time import  sleep

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield  driver
    #Закрыть браузер
    driver.quit()


def test_purchase_total(driver):
    #Открыть сайт магазина
    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()
    #Авторизоваться как пользователь standard_user
    user_name = driver.find_element(By.CSS_SELECTOR, '#user-name')
    user_name.clear()
    user_name.send_keys('standard_user')
    password = driver.find_element(By.CSS_SELECTOR, '#password')
    password.clear()
    password.send_keys('secret_sauce')
    driver.find_element(By.CSS_SELECTOR, '#login-button').click()
    #Добавить товары в корзину
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
    #Перейти в корзину
    driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()
    #Нажать Checkout
    driver.find_element(By.CSS_SELECTOR, '#checkout').click()
    #Заполнить форму данными
    first_name = driver.find_element(By.CSS_SELECTOR, '#first-name')
    first_name.clear()
    first_name.send_keys('Евгений')
    last_name = driver.find_element(By.CSS_SELECTOR, '#last-name')
    last_name.clear()
    last_name.send_keys('Геранин')
    postal_code = driver.find_element(By.CSS_SELECTOR, '#postal-code')
    postal_code.clear()
    postal_code.send_keys('454000')
    #Нажать на кнопку Continue
    driver.find_element(By.CSS_SELECTOR, '#continue').click()
    #Прочитать итоговую стоимость
    total = driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
    print(total)
    assert total == 'Total: $58.29'
    sleep(5)
    return total

    driver.quit()