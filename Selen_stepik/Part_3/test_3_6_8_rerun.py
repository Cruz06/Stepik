from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser2):
    browser2.get(link)
    browser2.find_element(By.CSS_SELECTOR, "#login_link")

def test_guest_should_see_login_link_fail(browser2):
    browser2.get(link)
    browser2.find_element(By.CSS_SELECTOR, "#magic_link")
