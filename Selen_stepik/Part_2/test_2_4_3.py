from selenium import webdriver
from selenium.webdriver.common.by import By


def test_243():
    # Automated test will fall due to delay caused by JavaScript code
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait1.html")

    # time.sleep(1)

    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text
