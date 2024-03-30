from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
browser = webdriver.Firefox()
browser.get("https://stepik.org/lesson/25969/step/8")
