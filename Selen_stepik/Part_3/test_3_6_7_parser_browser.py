from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser2):
    browser2.get(link)
    browser2.find_element(By.CSS_SELECTOR, "#login_link")