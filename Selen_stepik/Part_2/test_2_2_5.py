import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_225():
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    # на кнопку кликнуть нельзя, т.к. она перекрыта футером. Надо ее вытащить оттуда.
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # другой способ скрола
    browser.execute_script("window.scrollBy(0, 100);")
    button.click()

    time.sleep(3)
