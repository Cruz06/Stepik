from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://magento.softwaretestingboard.com/search/term/popular/"


def test_count_goods():
    browser.get(link)
    # collect goods
    list_of_goods = []
    list_font_sizes = []
    q_of_goods = len(browser.find_elements(By.CSS_SELECTOR, '[class="item"]'))

    terms = browser.find_elements(By.CSS_SELECTOR, '[class="item"] a')
    for g in terms:
        list_of_goods.append(g.text)
        #print(g.get_attribute("outerHTML"))
        g_font, g_size = g.get_attribute("style").split(": ")
        list_font_sizes.append(g_size)

    sorted_list = sorted(list_of_goods)
    print(list_of_goods)
    print(list_font_sizes)
    print(q_of_goods)

    assert list_of_goods == sorted_list, "Goods are not filtered from A to Z"

    browser.quit()
