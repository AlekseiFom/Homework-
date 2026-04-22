from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.color import Color
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver.get("http://uitestingplayground.com/classattr")
sleep(2)
buttons = driver.find_elements(By.TAG_NAME, "button")

target_button = None
for btn in buttons:
    color = btn.value_of_css_property("background-color")
    hex_color = Color.from_string(color).hex
    print(color, "=>", hex_color)
    if hex_color == "#007bff":
        target_button = btn

if target_button:
    target_button.send_keys(Keys.RETURN)
    print("Кнопка найдена по стилю и нажата")
sleep(5)