from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from Selen_stepik.Part_4.locators import MainPageLocators
from Selen_stepik.Part_4.locators import BasePageLocators
from .pages.login_page import LoginPage
from Selen_stepik.Part_4.locators import LoginPageLocators
from Selen_stepik.Part_4.locators import ProductPageLocators
import pytest


@pytest.mark.login_guest
class TestLogingFromMainPage():
    pytestmark = pytest.mark.login_guest
    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, MainPageLocators.link)
        page.open()
        assert page.is_element_present(*BasePageLocators.LOGIN_LINK), "Link is invalid"

    def test_guest_can_do_login(self, browser):
        page = MainPage(browser, MainPageLocators.link)
        page.open()
        page.go_to_login_page()


def test_should_login_page(browser):
    page = LoginPage(browser, LoginPageLocators.LOGIN_URL)
    page.open()
    page.should_be_login_page()
    assert "login" in browser.current_url


def test_should_be_login_url(browser):
    page = LoginPage(browser, LoginPageLocators.LOGIN_URL)
    page.open()
    page.should_be_login_url()


def test_should_be_login_form(browser):
    page = LoginPage(browser, LoginPageLocators.LOGIN_URL)
    page.open()
    page.should_be_login_form()


def test_should_be_registration_form(browser):
    page = LoginPage(browser, LoginPageLocators.LOGIN_URL)
    page.open()
    page.should_be_register_form()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, MainPageLocators.link)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, browser.current_url)
    page.basket_should_be_empty()




