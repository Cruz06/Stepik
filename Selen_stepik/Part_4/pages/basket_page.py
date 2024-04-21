from Selen_stepik.Part_4 import locators
from Selen_stepik.Part_4.pages.base_page import BasePage


class BasketPage(BasePage):

    def basket_should_be_empty(self):
        msg = self.browser.find_element(*locators.BasketPageLocators.MSG_BASKET_EMPTY)
        print(msg.text)
        text_message_eng = "Your basket is empty"
        text_message_ru = "Ваша корзина пуста"
        assert (text_message_eng in msg.text or text_message_ru in msg.text) , "Basket is not empty"


