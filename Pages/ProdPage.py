from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProdPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def add_multiple_items(self, list_of_items):
        for item in list_of_items:
            self.add_to_cart(item)
    def add_to_cart(self, item_name):
        formatted_name = item_name.lower().replace(" ", "-")
        locator = (By.CSS_SELECTOR, f"button[id*='{formatted_name}']")
        self.driver.find_element(*locator).click()
    def go_to_card_page(self):
        self.driver.get('https://www.saucedemo.com/cart.html')
        self.driver.maximize_window()