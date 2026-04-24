from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def test_slow_calculator():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#delay')))
    element.clear()
    element.send_keys("45")
    btns = driver.find_elements(By.CSS_SELECTOR, ".btn")
    def click_button(btns, value):
        for btn in btns:
            if btn.text.strip() == value:
                btn.click()
                break


    btns = driver.find_elements(By.CSS_SELECTOR, "span.btn")

    click_button(btns, "7")
    click_button(btns, "+")
    click_button(btns, "8")
    click_button(btns, "=")
    wait = WebDriverWait(driver, 50)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'), "15"))
    result = driver.find_element(By.CSS_SELECTOR, 'div.screen').text
    assert result == "15"
    driver.quit()
