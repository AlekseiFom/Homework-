from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:

    def __init__(self, driver, delay):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.implicitly_wait(4)
        self.delay = delay
        self.driver.maximize_window()

    def set_delay(self):
            self.driver.find_element(By.CSS_SELECTOR, '#delay').clear()
            self.driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(str(self.delay))

    def send_expression(self, expr: str):
        display_map = {
            "0": "0", "1": "1", "2": "2", "3": "3", "4": "4",
            "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",
            ".": ".", "+": "+", "-": "-", "/": "÷", "*": "x"
        }
        for ch in expr:
            if ch == "=": continue

            text = display_map[ch]
            self.driver.find_element(By.XPATH, f"//span[text()='{text}']").click()

    def click_equal(self):
        equal_locator = (By.XPATH, "//span[@class='btn btn-outline-warning' and text()='=']")
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(equal_locator)).click()

    def get_result_text(self, expected: str):
        locator = (By.CSS_SELECTOR, "div.screen")
        WebDriverWait(self.driver, self.delay + 5).until(
            EC.text_to_be_present_in_element(locator, expected)
        )
        return self.driver.find_element(*locator).text