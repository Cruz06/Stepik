import time

from .locators import ProductPageLocators
from .pages.product_page import ProductPage
import pytest


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
    time.sleep(8)

    page.should_be_msg_about_adding()
    time.sleep(8)

    name = page.find_product_name()
    time.sleep(8)

    price = page.find_product_price()
    print(f'Вы положили в корзину книгу "{name}" по цене "{price}".')

def test2_guest_can_add_any_product_to_basket(browser):
    # если книга не указана явно, а будет найдена на странице new
    page = ProductPage(browser, ProductPageLocators.BASKET_URL)
    page.open()
    #time.sleep(2)
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_msg_about_adding()
    name = page.find_product_name
    time.sleep(8)
    price = page.find_product_price
    page.check_product_name_in_basket(name)
    page.check_product_price_in_basket(price)

    print(f'Вы положили в корзину книгу "{name}" по цене "{price}".')

link10 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"

@pytest.mark.parametrize('link', ProductPageLocators.all_products_links)
def test_guest_can_add_many_product_to_basket(browser, link):
    # много страниц - книга и цена не указана явно, а будет найдена на странице
    page = ProductPage(browser, link)
    page.open()
    page.find_product_name()
    page.find_product_price()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_msg_about_adding(expected_book_name="Coders at Work")
    page.check_product_name_in_basket(expected_book_name="Coders at Work")
    # page.check_product_price_in_basket(expected_book_price="19,99 £")
    # name = page.find_product_name()
    # price = page.find_product_price()
    # print(f'Вы положили в корзину книгу "{name}" по цене "{price}".')