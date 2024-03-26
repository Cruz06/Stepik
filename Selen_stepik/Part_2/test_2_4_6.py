from selenium import webdriver
from selenium.webdriver.common.by import By


def test_246():
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/cats.html")
    button = browser.find_element(By.ID, "button")

    assert button.is_displayed()
