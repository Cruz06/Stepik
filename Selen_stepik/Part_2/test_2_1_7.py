from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
selector_trunk = "#treasure"
input_answer = "#answer"

def test_217():
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        x_element = browser.find_element(By.CSS_SELECTOR, selector_trunk)
        x_value = x_element.get_attribute("valuex")

        y = calc(x_value)

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
