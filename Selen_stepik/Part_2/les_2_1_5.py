from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/math.html"
selector_value = "#input_value.nowrap"
input_answer = "#answer.form-control"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, selector_value)
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, input_answer)
    answer.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    radiobut = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobut.click()

    button_submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button_submit.click()

    time.sleep(1)


finally:
    time.sleep(5)
    browser.quit()
