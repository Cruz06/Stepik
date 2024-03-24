from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/alert_accept.html"
button_activate = "button[type='submit']"   # name I want to go on a magical journey!
selector_value = ".nowrap#input_value"      #"#input_value"
input_answer = "answer"
button_submit = ".btn"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button_to_start = browser.find_element(By.CSS_SELECTOR, button_activate)
    button_to_start.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.CSS_SELECTOR, selector_value)
    x_value = x_element.text

    y = calc(x_value)

    answer = browser.find_element(By.ID, input_answer)
    answer.send_keys(y)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
