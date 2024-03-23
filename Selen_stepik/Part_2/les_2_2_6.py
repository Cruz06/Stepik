from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "https://SunInJuly.github.io/execute_script.html"
selector_value = "#input_value"
input_answer = "#answer"
check_box = "#robotCheckBox"
radio_robot = "#robotsRule"
button_submit = ".btn"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, selector_value)
    x_value = x_element.text

    y = calc(x_value)

    answer = browser.find_element(By.CSS_SELECTOR, input_answer)
    answer.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, check_box)
    checkbox.click()

    #browser.execute_script("window.scrollBy(0, 100);") # любой вариант работает
    radiobut = browser.find_element(By.CSS_SELECTOR, radio_robot)
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobut)
    radiobut.click()

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
