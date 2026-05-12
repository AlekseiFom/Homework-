from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get("http://the-internet.herokuapp.com/login")
sleep(2)
search_input = driver.find_element(By.CSS_SELECTOR, "#username")
search_input.send_keys("tomsmith")
password_field = driver.find_element(By.CSS_SELECTOR, "#password")
#password_field.send_keys("SuperSecretPassword!")
password_field.send_keys("SuperSecretPassword!", Keys.RETURN)
sleep(2)
green_flash = driver.find_element(By.CSS_SELECTOR, "div#flash.flash.success")
print(green_flash.text)
driver.quit()

