import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser(request) -> webdriver:
    browser_name = request.config.getoption("browser_name")
    lang_name = request.config.getoption("language")
    browser = None
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': lang_name})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose lang")

