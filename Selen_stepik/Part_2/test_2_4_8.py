from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
changing_price = "#price"
button_book = "#book"
selector_value = "#input_value"
input_answer = "#answer"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def test_248():
    browser = webdriver.Chrome()

    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, changing_price), "$100"))
    WebDriverWait(browser, 12).until(EC.element_to_be_clickable((By.CSS_SELECTOR, button_book))).click()

    x_element = browser.find_element(By.CSS_SELECTOR, selector_value).text

    y = calc(x_element)

    button = browser.find_element(By.CSS_SELECTOR, input_answer)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "#solve").click()

    #take result
    alert = browser.switch_to.alert
    alert_text = alert.text
    text_from_alert = alert_text.split(': ')[-1]
    print(text_from_alert)

