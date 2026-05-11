from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_loaded(self):
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "title"),
                "Checkout: Overview"
            )
        )

    def get_total_amount(self, expected_value: str):
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".summary_total_label"),
                expected_value
            )
        )
        element = self.driver.find_element(By.CSS_SELECTOR, ".summary_total_label")
        text = element.text
        return float(text.split("$")[1].strip())
