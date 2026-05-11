from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def fill_checkout_form(self, first_name, last_name, zip_code):
        WebDriverWait(self.driver, 10).until(EC.url_contains("checkout-step-one"))

        first_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        )
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "continue"))
        ).click()
