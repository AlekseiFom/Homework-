
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.form-control"))).send_keys("SkyPro")
driver.find_element(By.CSS_SELECTOR,'button.btn-primary').click()
text_button =driver.find_element(By.CSS_SELECTOR,'#updatingButton').text
print(text_button)
driver.quit()