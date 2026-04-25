from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_sum():
    driver = webdriver.Firefox()
    try:
        driver.get("https://www.saucedemo.com/")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#user-name"))).send_keys("standard_user")
        driver.find_element(By.CSS_SELECTOR, '#password').send_keys("secret_sauce")
        driver.find_element(By.CSS_SELECTOR, '#login-button').click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        driver.find_element(By.CSS_SELECTOR,".shopping_cart_badge").click()
        driver.find_element(By.ID, "checkout").click()
        driver.find_element(By.ID, "first-name").send_keys("Алексей")
        driver.find_element(By.ID, "last-name").send_keys("Фомин")
        driver.find_element(By.ID, "postal-code").send_keys("614094")
        driver.find_element(By.ID, "continue").click()
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.summary_total_label'), "$58.29")
        )
        result = driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
        assert  "$58.29" in result
        print(f"Итоговая сумма верна: {result}")
    finally:
        driver.quit()