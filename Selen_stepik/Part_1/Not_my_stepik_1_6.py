from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# passing test
link_pass = "http://suninjuly.github.io/registration1.html"

browser = webdriver.Chrome()
browser.get(link_pass)

first_name_field = browser.find_element(by=By.CSS_SELECTOR, value='input[placeholder="Input your first name"]')
first_name_field.send_keys("Kate")

last_name_field = browser.find_element(by=By.CSS_SELECTOR, value='input[placeholder="Input your last name"]')
last_name_field.send_keys("Bibilova")

email_field = browser.find_element(by=By.CSS_SELECTOR, value='input[placeholder="Input your email"]')
email_field.send_keys("kate@gmail.com")

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.TAG_NAME, "h1"))
)

welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
welcome_text = welcome_text_elt.text

assert "Congratulations! You have successfully registered!" == welcome_text

browser.quit()

# failing test
link_fail = "http://suninjuly.github.io/registration2.html"

browser = webdriver.Chrome()
browser.get(link_fail)

first_name_field = browser.find_element(by=By.CSS_SELECTOR, value='input[placeholder="Input your first name"]')
first_name_field.send_keys("Kate")

last_name_field = browser.find_element(by=By.CSS_SELECTOR, value='input[placeholder="Input your last name"]')
last_name_field.send_keys("Bibilova")

email_field = browser.find_element(by=By.CSS_SELECTOR, value='input[placeholder="Input your email"]')
email_field.send_keys("kate@gmail.com")

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.TAG_NAME, "h1"))
)

welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
welcome_text = welcome_text_elt.text

assert "Congratulations! You have successfully registered!" == welcome_text

browser.quit()
