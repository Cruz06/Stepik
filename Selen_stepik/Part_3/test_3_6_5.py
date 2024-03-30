import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
from selenium import webdriver
#answer = math.log(int(time.time()))


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()


login = "__"
password = "__"
list_of_urls = ["https://stepik.org/lesson/236895/step/1",
                "https://stepik.org/lesson/236896/step/1",
                "https://stepik.org/lesson/236897/step/1",
                "https://stepik.org/lesson/236898/step/1",
                "https://stepik.org/lesson/236899/step/1",
                "https://stepik.org/lesson/236903/step/1",
                "https://stepik.org/lesson/236904/step/1",
                "https://stepik.org/lesson/236905/step/1"
                 ]
rez = []


@pytest.mark.parametrize('url', list_of_urls)
def test_find_many_answers(browser, url):
    browser.get(f'{url}')
    browser.implicitly_wait(10)
    # authorization
    browser.find_element(By.CLASS_NAME, "navbar__auth_login").click()
    browser.find_element(By.CSS_SELECTOR, '[name="login"]').send_keys(login)
    browser.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys(password)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    # solve example and send answer
    a = str(math.log(int(time.time())))
    WebDriverWait(browser, 8).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'textarea'))).clear()
    time.sleep(1)
    WebDriverWait(browser, 8).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'textarea'))).send_keys(a)
    time.sleep(5)
    WebDriverWait(browser,12).until(EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission'))).click()

    # take result

    time.sleep(2)
    response = WebDriverWait(browser, 8).until(EC.visibility_of_element_located((By.CLASS_NAME, 'smart-hints__hint')))
    text_from_response = response.text
    print(text_from_response)

    if text_from_response != "Correct!":
        rez.append(text_from_response)

    print(*rez)

    assert text_from_response == "Correct!", f"Answer is '{text_from_response}' - it is not correct!!!"

