from .pages.main_page import MainPage
from Selen_stepik.Part_4.locators import MainPageLocators
from Selen_stepik.Part_4.locators import LoginPageLocators

def test_if_login_page_url(browser):
    page = MainPage(browser, MainPageLocators.link)
    page.open()
    browser.find_element(*LoginPageLocators.L)


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, MainPageLocators.link)
    page.open()
    assert page.is_element_present(*MainPageLocators.LOGIN_LINK), "Link is invalid"