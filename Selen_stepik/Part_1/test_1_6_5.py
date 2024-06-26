from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"
value1= "input"
#таких (value1) 4 штуки на странице, но нужен первый, поэтому его можно использовать
value2= "last_name"
value3= "city"
value4 = "country"


def test_165():
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        link1 = browser.find_element(By.LINK_TEXT, f'{str(math.ceil(math.pow(math.pi, math.e)*10000))}')
        link1.click()

        input1 = browser.find_element(By.TAG_NAME, value1)
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.NAME, value2)
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, value3)
        input3.send_keys("Smolensk")
        input4 = browser.find_element(By.ID, "country")
        input4.send_keys("Russia")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

    # не забываем оставить пустую строку в конце файла