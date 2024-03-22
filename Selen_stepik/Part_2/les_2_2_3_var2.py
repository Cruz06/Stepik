from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


def calc(x1, x2):
    return str(int(x1) + int(x2))


link = "https://suninjuly.github.io/selects1.html"
value1 = "#num1"
value2 = "#num2"
open_selector = "#dropdown"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    element1 = browser.find_element(By.CSS_SELECTOR, value1).text
    element2 = browser.find_element(By.CSS_SELECTOR, value2).text

    rez = calc(element1, element2)

    select = Select(browser.find_element(By.CSS_SELECTOR, open_selector))
    select.select_by_value(str(rez))

    button_submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button_submit.click()

    time.sleep(1)


finally:
    time.sleep(5)
    browser.quit()
