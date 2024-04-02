from selenium.webdriver.common.by import By

from pages.main_page import MainPage


def test_guest_can_do_login(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.is_element_present(By.CSS_SELECTOR, "#login_link_invalid")
