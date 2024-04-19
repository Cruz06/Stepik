from Selen_stepik.Part_4.pages.base_page import BasePage
from Selen_stepik.Part_4.locators import MainPageLocators
from Selen_stepik.Part_4.locators import ProductPageLocators
import allure


@allure.epic("testing main page 1")
class MainPage(BasePage):

    @allure.step("before log in")
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    @allure.step("before log in 2")
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    @allure.step("to product page")
    def go_to_product_page(self):
        product_link = self.browser.find_element(*ProductPageLocators.BASKET_URL)
        product_link.click()


    def go_to_basket(self):
        self.browser.find_element(*ProductPageLocators.GO_TO_BASKET).click()