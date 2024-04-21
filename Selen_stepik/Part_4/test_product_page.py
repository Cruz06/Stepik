import time

from .locators import ProductPageLocators
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
import pytest


def test_guest_can_add_product_to_basket(browser):
    # название книги и цена задается пользователем в файле locators.py
    page = ProductPage(browser, ProductPageLocators.BASKET_URL)
    page.open()
    # time.sleep(2)
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_msg_about_adding()
    page.check_product_name()
    page.check_product_price()


def test_guest_can_add_any_product_to_basket(browser):
    # если книга не указана явно, а будет найдена на странице
    page = ProductPage(browser, ProductPageLocators.BASKET_URL)
    page.open()
    # time.sleep(2)
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
    # time.sleep(2)
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
    # task 4.3.4
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


@pytest.mark.xfail
def test_guest_can_add_product_to_basket2(browser):
    # task 4.3.5
    page = ProductPage(browser, ProductPageLocators.BASKET_URL)
    page.open()
    print()
    print(f'"page {page} was open')
    name = page.find_product_name()
    page.add_product_to_basket()
    print(f'Book {name} was added to the basket')
    page.solve_quiz_and_get_code()
    print("quiz was solved")
    # page.should_not_be_success_message()
    page.elem_should_disappear()
    page.should_be_msg_about_adding(expected_book_name="Coders at Work")
    page.check_product_name_in_basket(expected_book_name="Coders at Work")


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, ProductPageLocators.BASKET_URL)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, browser.current_url)
    page.basket_should_be_empty()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # добавляем товар в корзину, проверяем что НЕТ сообщения об успехе
    page = ProductPage(browser, ProductPageLocators.PRODUCT_URL_EN)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    # на стрнаице каталога, проверяем что НЕТ сообщения об успехе (товар не добавляли)
    page = ProductPage(browser, ProductPageLocators.PRODUCT_URL_EN)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    # добавляем товар в корзину, проверяем что НЕТ сообщения о добавлении товара
    page = ProductPage(browser, ProductPageLocators.PRODUCT_URL_EN)
    page.open()
    page.add_product_to_basket()
    page.elem_should_disappear()
