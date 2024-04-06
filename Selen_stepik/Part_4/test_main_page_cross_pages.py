from .pages.main_page import MainPage
from Selen_stepik.Part_4.locators import MainPageLocators
from .pages.login_page import LoginPage
from Selen_stepik.Part_4.locators import LoginPageLocators


def test_guest_can_do_login(browser):
    page = MainPage(browser, MainPageLocators.link)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, MainPageLocators.link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()
    #assert page.is_element_present(*MainPageLocators.LOGIN_LINK), "Link is invalid"


def test_should_login_page(browser):
    page = LoginPage(browser, LoginPageLocators.LOGIN_URL)
    page.open()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    #assert "login" in browser.current_url


def test_should_be_login_url(browser):
    page = LoginPage(browser, LoginPageLocators.LOGIN_URL)
    page.open()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()


def test_should_be_login_form(browser):
    page = LoginPage(browser, LoginPageLocators.LOGIN_URL)
    page.open()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_form()


def test_should_be_registration_form(browser):
    page = LoginPage(browser, LoginPageLocators.LOGIN_URL)
    page.open()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_register_form()
