from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#image-container img:nth-of-type(3)')))
divs = driver.find_elements(By.CSS_SELECTOR, '#image-container img')
div = divs[2]
css_class = div.get_attribute("src")
print(css_class)
driver.quit()