import time
from selenium import webdriver


def test_224():
    browser = webdriver.Chrome()

    browser.execute_script("alert('Robots at work');")
    time.sleep(3)
    browser.execute_script("document.title='Script executing';")
    time.sleep(3)
    browser.execute_script('document.title="Script executing 2222";')
    time.sleep(3)
    browser.execute_script("document.title='Script executing 333';alert('Robots at work');")
    time.sleep(3)

