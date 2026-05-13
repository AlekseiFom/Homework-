from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException



class ProdPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def add_multiple_items(self, list_of_items):
        for item in list_of_items:
            self.add_to_cart(item)

    def add_to_cart(self, item_name):
        formatted_name = item_name.lower().replace(" ", "-")
        locator = (By.CSS_SELECTOR, f"button[id*='{formatted_name}']")

        for attempt in range(3):
            try:
                # Ждём появления кнопки
                button = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(locator)
                )
                # Если уже "Remove" — товар в корзине
                if button.text == "Remove":
                    print(f"Товар {item_name} уже в корзине, пропускаем")
                    return

                # Скроллим и кликаем
                self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator)).click()

                # Ждём, пока текст сменится на "Remove"
                WebDriverWait(self.driver, 5).until(
                    EC.text_to_be_present_in_element(locator, "Remove")
                )
                return  # Успешно добавили

            except StaleElementReferenceException:
                continue  # просто повторить попытку
            except (TimeoutException, Exception) as e:
                if attempt == 2:
                    raise  # если последняя попытка — выбрасываем ошибку
                continue  # иначе пробуем снова
        raise Exception(f"Не удалось добавить товар {item_name} после 3 попыток")
    def go_to_card_page(self):
        self.driver.get('https://www.saucedemo.com/cart.html')
        self.driver.maximize_window()