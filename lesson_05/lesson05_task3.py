from time import sleep
from selenium import webdriver
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver.get("http://the-internet.herokuapp.com/inputs")
sleep(2)
search_input = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
search_input.send_keys("12345")
sleep(2)
search_input.clear()
sleep(2)
search_input.send_keys("54321")
sleep(2)
driver.quit()