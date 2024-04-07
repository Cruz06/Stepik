from Selen_stepik.Part_4.locators import ProductPageLocators
from Selen_stepik.Part_4.pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('link', ProductPageLocators.all_products_links)
def test_guest_can_add_many_product_to_basket(browser, link):
    # много страниц - книга и цена не указана явно, а будет найдена на странице
    page = ProductPage(browser, ProductPageLocators.BASKET_URL)
    page.open()
    #time.sleep(2)
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_msg_about_adding()
    name = page.find_product_name()
    price = page.find_product_price()
    print(f'Вы положили в корзину книгу "{name}" по цене "{price}".')

