import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


link = "https://stepik.org/catalog"
login = "__"
password = "__"


def test_authorization_on_stepik(browser):
    browser.get(link)
    browser.implicitly_wait(8)
    browser.find_element(By.CLASS_NAME, "navbar__auth_login").click()
    browser.find_element(By.CSS_SELECTOR, '[name="login"]').send_keys(login)
    browser.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys(password)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    try:
        browser.find_element(By.CSS_SELECTOR, '[alt="User avatar"]')
        assert True, "No login"
    except NoSuchElementException:
        assert False

