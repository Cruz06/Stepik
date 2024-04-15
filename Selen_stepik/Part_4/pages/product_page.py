from Selen_stepik.Part_4 import locators
from Selen_stepik.Part_4.pages.base_page import BasePage
import time


class ProductPage(BasePage):
    def should_be_product_url(self):
        expected_url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        # print(self.browser.current_url)
        assert self.browser.current_url == expected_url, "ULR is not correct"

    def should_be_button_add_to_basket(self):
        result = len(self.browser.find_elements(*locators.ProductPageLocators.BASKET_URL))
        assert result == 1, "Login from is not present"

    def find_product_name(self):
        # найти название книги на странице
        expected_book_name = self.browser.find_element(*locators.ProductPageLocators.BOOK_NAME_IN_CATALOG)
        return expected_book_name.text

    def find_product_price(self):
        # найти цену книги на странице
        expected_book_price = self.browser.find_element(*locators.ProductPageLocators.BOOK_PRICE_IN_CATALOG)
        return expected_book_price.text

    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*locators.ProductPageLocators.BUTTON_ADD_BASKET)
        add_to_basket.click()

    def check_product_name(self, expected_book_name):
        actual_book_name = self.browser.find_element(*locators.ProductPageLocators.BOOK_NAME_IN_BASKET)
        time.sleep(15)
        print(f'Book title is: "{actual_book_name.text}"')
        assert actual_book_name.text == expected_book_name, "Product name is wrong or missing"

    def check_product_price(self, expected_book_price):
        actual_book_price = self.browser.find_element(*locators.ProductPageLocators.BOOK_PRICE_IN_CATALOG)
        print(f'Book price is: "{actual_book_price.text}"')
        assert actual_book_price.text == expected_book_price, "Product price is wrong or missing"

    def should_be_msg_about_adding(self, expected_book_name):
        # Проверка выхода сообщения что товар добавлен
        product_name = self.browser.find_element(*locators.ProductPageLocators.BOOK_NAME_IN_CATALOG).text
        message = self.browser.find_element(*locators.ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        print(f'Alert message is: {message}')
        assert message == expected_book_name, "Product name not found on message"

    def check_product_name_in_basket(self, expected_book_name):
        actual_message = self.browser.find_element(*locators.ProductPageLocators.MESSAGE_IN_BASKET).text
        expected_message = expected_book_name + " has been added to your basket."
        print(f'Expected Message in basket is: {expected_message}')
        assert actual_message == expected_message, actual_message
        # assert actual_message == expected_message, "Product name is wrong or missing"

    def check_product_price_in_basket(self, expected_book_price):
        # wrong test
        actual_book_price = self.browser.find_element(*locators.ProductPageLocators.MESSAGE_PRICE_IN_BASKET).text
        print(f'actual price message is: {actual_book_price}')
        expected_price_text = "Your basket total is now"+ expected_book_price
        assert actual_book_price == expected_price_text, "Product price is wrong or missing"

    def should_not_be_success_message(self):
        assert not self.is_element_present(*locators.ProductPageLocators.MESSAGE_ABOUT_ADDING), "Success message is presented"

    def elem_should_disappear(self):
        assert self.is_disappeared(*locators.ProductPageLocators.MESSAGE_ABOUT_ADDING), "Succes message dodn't disappeared in 4 sec"

