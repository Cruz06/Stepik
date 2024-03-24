from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import re

link = "http://suninjuly.github.io/redirect_accept.html"
button_redirect = "button"
selector_value = ".nowrap#input_value"      #"#input_value"
input_answer = "answer"
button_submit = ".btn"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button_link = browser.find_element(By.CSS_SELECTOR, button_redirect)
    button_link.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.CSS_SELECTOR, selector_value)
    x_value = x_element.text

    y = calc(x_value)

    answer = browser.find_element(By.ID, input_answer)
    answer.send_keys(y)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    # take answer
    alert = browser.switch_to.alert
    alert_text = alert.text
    text = re.findall("(?:Congrats, you've passed the task! Copy this code as the answer to Stepik quiz:\s)(.*)", alert_text)
    print(*text)

finally:
    time.sleep(5)
    browser.quit()
