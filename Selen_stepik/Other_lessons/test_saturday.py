import time
from selenium.webdriver.common.by import By
from selenium import webdriver

link = "https://demoqa.com/select-menu"


def test_form():
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.XPATH, '//*[@id="selectMenuContainer"]/div[7]/div/div/div/div[2]').click()

    time.sleep(65)
    assert True
