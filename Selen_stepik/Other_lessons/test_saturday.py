import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

link = "https://demoqa.com/select-menu"


def test_form():
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(7)

    # 1. Select Value (first)   !!! no
    browser.find_element(By.CSS_SELECTOR, '#withOptGroup div div').click()
    browser.find_element(By.XPATH, '//*[contains(text(), "Group 1, option 2")]').click()

    # 2. Select One (second)
    browser.find_element(By.CSS_SELECTOR, '[id="selectOne"]').click()
    browser.find_element(By.XPATH, '//*[contains(text(), "Mrs")]').click()

    # 3. Old Style Select Menu
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text("Purple")

    # 4. Multiselect drop down  !!! no
    browser.find_element(By.CSS_SELECTOR, '#selectMenuContainer > div:nth-child(8) > div > div > div').click()
    browser.find_element(By.XPATH, '//div[contains(text(), "Blue")]').click()

    browser.execute_script("window.scrollBy(0, 100);")

    # 5/ Standard multiple select
    browser.find_element(By.CSS_SELECTOR, '[value="saab"]').click()
    browser.find_element(By.CSS_SELECTOR, '[value="audi"]').click()

    time.sleep(2)

    assert True
