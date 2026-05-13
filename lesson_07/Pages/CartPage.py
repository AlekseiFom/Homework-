from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def go_to_checkout(self):
        element = self.driver.find_element(By.ID, "checkout")
        self.driver.execute_script("arguments[0].click();", element)