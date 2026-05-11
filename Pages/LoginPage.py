from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    def login(self, user, password ):
        self.driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(user)
        self.driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password )
        self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("/inventory.html"))