from Selen_stepik.Part_4 import locators
from Selen_stepik.Part_4.pages.base_page import BasePage


class ProductPage(BasePage):
    def should_be_product_url(self):
        expected_url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        # print(self.browser.current_url)
        assert self.browser.current_url == expected_url, "ULR is not correct"

    def should_be_button_add_to_basket(self):
        result = len(self.browser.find_elements(*locators.ProductPageLocators.BASKET_URL))
        assert result == 1, "Login from is not present"

    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*locators.ProductPageLocators.BUTTON_ADD_BASKET)
        add_to_basket.click()

    def check_product_name(self):
        expected_book_name = locators.ProductPageLocators.book_name_from_user
        actual_book_name = self.browser.find_element(*locators.ProductPageLocators.BOOK_NAME)
        print(f'Book title is: "{actual_book_name.text}"')
        assert actual_book_name.text == expected_book_name, "Product name is wrong or missing"

    def check_product_price(self):
        expected_book_price = locators.ProductPageLocators.book_price_from_user
        actual_book_price = self.browser.find_element(*locators.ProductPageLocators.BOOK_PRICE)
        print(f'Book price is: "{actual_book_price.text}"')
        assert actual_book_price.text == expected_book_price, "Product price is wrong or missing"

    def should_be_msg_about_adding(self):
        # Проверка выхода сообщения что товар добавлен
        product_name = self.browser.find_element(*locators.ProductPageLocators.BOOK_NAME).text
        message = self.browser.find_element(*locators.ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        print(f'Message is: "{message}"')
        assert product_name in message, "Product name not found on message"

    def find_product_name(self):
        # найти название книги на странице
        actual_book_name = self.browser.find_element(*locators.ProductPageLocators.BOOK_NAME)
        return actual_book_name.text

    def find_product_price(self):
        # найти цену книги на странице
        actual_book_price = self.browser.find_element(*locators.ProductPageLocators.BOOK_PRICE)
        return actual_book_price.text
