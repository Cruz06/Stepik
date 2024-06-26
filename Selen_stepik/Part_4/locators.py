from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    invalid_link = (By.CSS_SELECTOR, "#login_link_a")


class BasketPageLocators():
    BUTTON_MAKE_ORDER = (By.CSS_SELECTOR, '[href$="checkout/"]')
    MSG_BASKET_EMPTY = (By.CSS_SELECTOR, '#content_inner p')


class LoginPageLocators():
    LOGIN_URL = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

    LOGIN_USER = (By.CSS_SELECTOR, 'input[name="login-username"]')
    PASSWORD_USER = (By.CSS_SELECTOR, 'input[name="login-password"]')
    BUTTON_SUBMIT_USER = (By.CSS_SELECTOR, '[name="login_submit"]')

    EMAIL_REGISTRATION = (By.CSS_SELECTOR, 'input[name="registration-email"]')
    PASSWORD_REGISTRATION = (By.CSS_SELECTOR, 'input[name="registration-password1"]')
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, 'input[name="registration-password2"]')
    BUTTON_SUBMIT_REGISTRATION = (By.CSS_SELECTOR, '[name="registration_submit"]')


class MainPageLocators():

    link = "http://selenium1py.pythonanywhere.com/"
    link1 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"


class ProductPageLocators():
    PRODUCT_URL_EN = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    BASKET_URL = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    BASKET_URL0 = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    URL_CITY_AND_STARS = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    book_name0_from_user = "The shellcoder's handbook"
    book_name_from_user = "Coders at Work"
    book_price0_from_user = "9,99 £"
    book_price_from_user = "19,99 £"
    GO_TO_BASKET = (By.CSS_SELECTOR, '[href$="basket/"]:first-child')
    #BUTTON_ADD_BASKET = (By.CSS_SELECTOR, '[value="Добавить в корзину"]')
    BUTTON_ADD_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    # BOOK_NAME_IN_CATALOG = (By.CSS_SELECTOR, 'div.col-sm-6.product_main > h1')
    # BOOK_PRICE_IN_CATALOG = (By.CSS_SELECTOR, '.price_color:nth-child(2)')
    BOOK_NAME_IN_CATALOG = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    BOOK_PRICE_IN_CATALOG = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')

    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, 'div.alert:nth-child(1) strong')
    MESSAGE_IN_BASKET = (By.XPATH, '//*[@id="messages"]/div[1]/div')
    MESSAGE_PRICE_IN_BASKET = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/text()')

    all_products_links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]


