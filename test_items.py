from selenium.webdriver.common.by import By
import time


def test_add_to_cart_button_exists(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    add_to_cart_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert add_to_cart_button.is_displayed(), "test failed see 'assert'"

