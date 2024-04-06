from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    link = "http://selenium1py.pythonanywhere.com/"
    link1 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    invalid_link = (By.CSS_SELECTOR, "#login_link_a")


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

