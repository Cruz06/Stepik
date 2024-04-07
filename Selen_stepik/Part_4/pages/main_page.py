from Selen_stepik.Part_4.pages.base_page import BasePage
from Selen_stepik.Part_4.locators import MainPageLocators
from Selen_stepik.Part_4.locators import ProductPageLocators


class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_product_page(self):
        product_link = self.browser.find_element(*ProductPageLocators.BASKET_URL)
        product_link.click()
