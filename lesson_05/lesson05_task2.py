from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver.get("http://uitestingplayground.com/dynamicid")
sleep(2)
search_input = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
search_input.send_keys(Keys.RETURN)

print("Кнопка найдена и нажата")
sleep(2)