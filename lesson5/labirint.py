from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # открывает хром
driver.maximize_window()  # делать окно в макс размере

# зайти на лабиринт
driver.get("https://www.labirint.ru/")

# найти книги по слову Python
search_locator = "#search-field"  # локатор поисковой строки

search_input = driver.find_element(By.CSS_SELECTOR,search_locator)  # поиск элемента на веб-странице, соответствующий указанному CSS-селектору

search_input.send_keys("Python", Keys.RETURN)  # в поисковой строке пишет название python и имитирует нажатие ентер

# собрать все карточки товаров
book_locator = "div.product-card"  # локатор карточек с названием python

books = driver.find_elements(By.CSS_SELECTOR, book_locator)  # ищем все продукты по локатору

# вывести в консоль инфо: автор + название + цена
for book in books:
    title = book.find_element(By.CSS_SELECTOR, 'a.product-card__name').text

    try:  # если в какой-то книге нет автора, то...
        author = book.find_element(By.CSS_SELECTOR,'div.product-card__author').text  # ищем всех авторов и выводим текстом
    except:
        author = "Автор не найден"

    try:  # если в какой-то книге нет цены, то...
        price = book.find_element(By.CSS_SELECTOR, 'div.product-card__price-val-old').text
    except:
        price = "Цена не найдена"  # выводим, что цена не найдена

    print(author + "\t" + title + "\t" + price)

sleep(5)