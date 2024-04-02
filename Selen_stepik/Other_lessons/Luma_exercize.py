from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
link = "https://magento.softwaretestingboard.com/search/term/popular/"


def test_count_goods():
    browser.get(link)
    # collect goods
    list_of_goods = []
    list_fonts = []
    list_font_sizes = []
    q_of_goods = len(browser.find_elements(By.CSS_SELECTOR, '[class="item"]'))

    iti = browser.find_elements(By.CSS_SELECTOR, '[class="item"]')
    # # iti = iter(browser.find_elements(By.XPATH, '//div[3]/div/ul/li'))
    # for g in iti:
    #     next(iti)
    #     new_g = browser.find_element(By.CSS_SELECTOR, '[class="item"]')
    #     list_of_goods.append(new_g.text)
    #     # g_font, g_size = new_g.get_attribute("style").split(": ")
    #     # list_fonts.append(g_font)
    #     # list_font_sizes.append(g_size)
    #
    # sorted_list = sorted(list_of_goods)
    print(iti)
    # print(list_of_goods)
    # print()
    # print(list_fonts)
    # print()
    # print(list_font_sizes)
    # print(q_of_goods)

    # assert list_of_goods == sorted_list, "Goods are not filtered from A to Z"

    browser.quit()