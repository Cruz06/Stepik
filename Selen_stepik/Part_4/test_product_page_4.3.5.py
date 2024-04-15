import time
from Selen_stepik.Part_4.locators import ProductPageLocators
from Selen_stepik.Part_4.pages.product_page import ProductPage

# about desappearing elements
# link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"


def test_guest_can_add_product_to_basket(browser):
    # название книги и цена задается пользователем в файле locators.py
    page = ProductPage(browser, ProductPageLocators.BASKET_URL)
    print("open")
    page.open()
    #time.sleep(2)
    page.add_product_to_basket()
    print("add product")
    page.solve_quiz_and_get_code()
    print("solved problem")
    page.should_be_msg_about_adding()
    print("msg is here")
    page.check_product_name()
    page.check_product_price()


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