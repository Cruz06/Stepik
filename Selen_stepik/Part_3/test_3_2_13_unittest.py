import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

class TestRegForm(unittest.TestCase):

    def test_Registration_yes(self):
        browser = webdriver.Chrome()
        browser.get(link1)

        first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block div input.form-control.first")
        first_name.send_keys("Ola")

        last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block div input.form-control.second")
        last_name.send_keys("Olarut")

        email = browser.find_element(By.CSS_SELECTOR, "div.first_block div input.form-control.third")
        email.send_keys("Ola@ola.md")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        expected_text = "Congratulations! You have successfully registered!"

        self.assertEqual(expected_text, welcome_text, "User should be registered!")

        browser.quit()

    def test_Registration_no(self):
        browser = webdriver.Chrome()
        browser.get(link2)

        first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block div input.form-control.first")
        first_name.send_keys("Ola")

        last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block div input.form-control.second")
        last_name.send_keys("Olarut")

        email = browser.find_element(By.CSS_SELECTOR, "div.first_block div input.form-control.third")
        email.send_keys("Ola@ola.md")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        expected_text = "Congratulations! You have successfully registered!"
        self.assertEqual(expected_text, welcome_text, "User should be registered!")

        browser.quit()


if __name__ == "__main__":
    unittest.main()
