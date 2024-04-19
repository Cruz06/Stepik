from Selen_stepik.Part_4.pages.base_page import BasePage
from Selen_stepik.Part_4 import locators
from Selen_stepik.Part_4.pages import main_page
import allure


class LoginPage(BasePage):
    @allure.step("login page")
    def should_be_login_page(self):
        assert "login" in self.browser.current_url

    @allure.step("login url")
    def should_be_login_url(self):
        expected_url = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
        #print(self.browser.current_url)
        assert self.browser.current_url == expected_url, "ULR is not correct"

    @allure.step("log in form")
    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        result = len(self.browser.find_elements(*locators.LoginPageLocators.LOGIN_FORM))
        assert result == 1, "Login from is not present"
        # self.browser.find_element(*locators.LoginPageLocators.LOGIN_USER)
        # self.browser.find_element(*locators.LoginPageLocators.PASSWORD_USER)
        # self.browser.find_element(*locators.LoginPageLocators.BUTTON_SUBMIT_USER)

    @allure.step("register form")
    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        result = len(self.browser.find_elements(*locators.LoginPageLocators.REGISTER_FORM))
        assert result == 1, "Registration from is not present"
        # assert self.browser.is_element_present(*locators.LoginPageLocators.EMAIL_REGISTRATION)
        # assert self.browser.is_element_present(*locators.LoginPageLocators.PASSWORD_REGISTRATION)
        # assert self.browser.is_element_present(*locators.LoginPageLocators.PASSWORD_CONFIRM)
        # assert self.browser.is_element_present(*locators.LoginPageLocators.BUTTON_SUBMIT_REGISTRATION)
