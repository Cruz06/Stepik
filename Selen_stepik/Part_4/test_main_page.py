from .pages.main_page import MainPage
from Selen_stepik.Part_4.locators import MainPageLocators
from Selen_stepik.Part_4.locators import LoginPageLocators


def test_guest_can_do_login(browser):
    page = MainPage(browser, MainPageLocators.link)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, MainPageLocators.link)
    page.open()
    assert page.is_element_present(*MainPageLocators.LOGIN_LINK), "Link is invalid"
