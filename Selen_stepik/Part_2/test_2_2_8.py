from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


link = "http://suninjuly.github.io/file_input.html"
first_name = "firstname"    # name
last_name = "lastname"      # name
email = "Enter email"       #text in placeholder
send_file_button = "input#file"
button_submit = ".btn"


def test_228():
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        name1 = browser.find_element(By.NAME, first_name)
        name1.send_keys("Eliza")

        name2 = browser.find_element(By.NAME, last_name)
        name2.send_keys("Rut")

        mail = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter email"]')
        mail.send_keys("test_mail@mail.ru")

        current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
        file_path = os.path.join(current_dir, 'for_2_2_8.txt')  # добавляем к этому пути имя файла
        send_button = browser.find_element(By.CSS_SELECTOR, send_file_button)   # находим кнопку загрузки файла
        send_button.send_keys(file_path)                                        # загружаем

        button = browser.find_element(By.TAG_NAME, "button")
        button.click()

    finally:
        time.sleep(5)
        browser.quit()
