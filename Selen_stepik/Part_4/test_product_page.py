from .locators import ProductPageLocators
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    # название книги и цена задается пользователем в файле locators.py
    page = ProductPage(browser, ProductPageLocators.BASKET_URL)
    page.open()
    #time.sleep(2)
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_msg_about_adding()
    page.check_product_name()
    page.check_product_price()


def test_guest_can_add_any_product_to_basket(browser):
    # если книга не указана явно, а будет найдена на странице
    page = ProductPage(browser, ProductPageLocators.BASKET_URL)
    page.open()
    #time.sleep(2)
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_msg_about_adding()
    name = page.find_product_name()
    price = page.find_product_price()
    print(f'Вы положили в корзину книгу "{name}" по цене "{price}".')
