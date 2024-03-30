import time

from selenium.webdriver.common.by import By
from selenium import webdriver

link1 = "https://testpages.eviltester.com/styled/basic-html-form-test.html"
link = "https://testpages.eviltester.com/styled/alerts/alert-test.html"
path_file = r"C:\Users\Olga\Desktop\рис2.JPG"


def test_check_alert_button():
    browser = webdriver.Chrome()
    browser.get(link)
    alert_button = browser.find_element(By.ID, 'alertexamples')
    alert_button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    text_from_alert = alert_text.split(': ')[-1]
    print(text_from_alert)
    assert "I am an alert box!" in text_from_alert


def test_form():
    browser = webdriver.Chrome()
    browser.get(link1)
    browser.find_element(By.CSS_SELECTOR, '[name="username"]').send_keys("Ola")
    browser.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys("123")
    browser.find_element(By.CSS_SELECTOR, '[name="comments"]').send_keys("Many many text!!!")

    browser.find_element(By.CSS_SELECTOR, '[type="file"]').send_keys(path_file)
    # checkbox remove default value
    browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]').click()
    browser.find_element(By.CSS_SELECTOR, '[value="cb3"]').click()   # remove
    browser.find_element(By.CSS_SELECTOR, '[value="cb1"]').click()
    browser.find_element(By.XPATH, '//tr[5]//input[1]').click()
    browser.find_element(By.XPATH, '(//*[@type="radio"])[1]').click()

    # multiselect remove default value
    browser.find_element(By.CSS_SELECTOR, '[value="ms4"]').click()  # remove
    browser.find_element(By.CSS_SELECTOR, '[value="ms1"]').click()
    browser.find_element(By.CSS_SELECTOR, '[value="ms2"]').click()

    browser.find_element(By.CSS_SELECTOR, '[name="dropdown"]').click()
    browser.find_element(By.CSS_SELECTOR, '[value="dd1"]').click()

    browser.find_element(By. CSS_SELECTOR, '[type="submit"]').click()

    expected_url = "https://testpages.eviltester.com/styled/the_form_processor.php"
    time.sleep(5)
    assert browser.current_url == expected_url

