from .base_page import BasePage
from Selen_stepik.Part_4 import locators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url(*locators.LoginPageLocators.LOGIN_URL), "URL is not correct"


    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.browser.is_element_present(*locators.LoginPageLocators.LOGIN_USER)
        assert self.browser.is_element_present(*locators.LoginPageLocators.PASSWORD_USER)
        assert self.browser.is_element_present(*locators.LoginPageLocators.BUTTON_SUBMIT_USER)


    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.browser.is_element_present(*locators.LoginPageLocators.EMAIL_REGISTRATION)
        assert self.browser.is_element_present(*locators.LoginPageLocators.PASSWORD_REGISTRATION)
        assert self.browser.is_element_present(*locators.LoginPageLocators.PASSWORD_CONFIRM)
        assert self.browser.is_element_present(*locators.LoginPageLocators.BUTTON_SUBMIT_REGISTRATION)

