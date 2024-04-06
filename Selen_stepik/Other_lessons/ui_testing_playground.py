import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Selen_stepik.Part_3.conftest import browser
link = "http://uitestingplayground.com/overlapped"


def test_input_id(browser):
    browser.get(link)
    ii = browser.find_element(By.ID, "id")
    ii.send_keys("Ola")
    expected_text_id = "Ola"

    assert ii.get_attribute("value") == expected_text_id


def test_input_scroll(browser):
    browser.get(link)
    ii = browser.find_element(By.ID, "id")
    ii.send_keys("Ola")
    # expected_text_id = "Ola"
    time.sleep(4)
    # first variant
    #browser.execute_script("arguments[0].scrollBy(0, 100);", browser.find_element(By.CSS_SELECTOR, '[style="overflow-y: scroll; height:100px;"]'))

    # second variant
    browser.execute_script('arguments[0].scrollIntoView(true);', browser.find_element(By.ID, "name"))

    # 3rd not here!!!
    #ActionChains(browser).scroll_to_element(browser.find_element(By.ID, "name")).click().send_keys("vladimir").perform()

    nn = browser.find_element(By.ID, "name")
    nn.send_keys("vladimir")

    expected_text_name = "vladimir"
    time.sleep(4)
    assert nn.get_attribute("value") == expected_text_name


link1 = "http://uitestingplayground.com/verifytext"


def test_verify_text(browser):
    browser.get(link1)
    #elem = browser.find_element(By.CLASS_NAME, "bg-primary")
    elem = browser.find_element(By.XPATH, "//span[normalize-space(.)='Welcome UserName!']")
    #print(elem.text)
    expected_text = "Welcome UserName!"
    assert elem.text == expected_text


link3 = "http://uitestingplayground.com/nbsp"


# site with simbols : https://unicode-explorer.com/c/00A0
def test_nonbreaking_spaces(browser):
    browser.get(link3)
    elem = browser.find_element(By.XPATH, "//*[text()='My Button']")
    print(elem.text)

