from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color


def test_form_colors():
    driver = webdriver.Edge()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[name=first-name]'))).send_keys(
        "Иван")
    driver.find_element(By.CSS_SELECTOR, '[name=last-name]').send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, '[name=address]').send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, '[name=e-mail]').send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, '[name=phone]').send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, '[name=city]').send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, '[name=country]').send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, '[name=job-position]').send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, '[name=company]').send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, ".btn").click()

    RED_HEX = "#F8D7DA"
    GREEN_HEX = "#D1E7DD"

    green_ids = ["first-name", "last-name", "address", "city",
                 "country", "e-mail", "phone", "job-position", "company"]

    for field_id in green_ids:
        element = driver.find_element(By.ID, field_id)
        actual_hex = Color.from_string(element.value_of_css_property("background-color")).hex.upper()
        assert actual_hex == GREEN_HEX, f"Поле {field_id} не зеленое!"

    zip_element = driver.find_element(By.ID, "zip-code")
    zip_hex = Color.from_string(zip_element.value_of_css_property("background-color")).hex.upper()
    assert zip_hex == RED_HEX, "Zip-code должен быть красным!"

    driver.quit()
