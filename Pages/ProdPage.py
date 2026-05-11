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

        # Повторяем до 3 раз на случай stale element
        for attempt in range(3):
            try:

                button = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(locator)
                )

                if button.text == "Remove":
                    print(f"Товар {item_name} уже в корзине, пропускаем")
                    return


                self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
                WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable(locator)
                )
                button.click()

                WebDriverWait(self.driver, 5).until(
                    EC.text_to_be_present_in_element(locator, "Remove")
                )
                return  # Выходим, если всё ок

            except StaleElementReferenceException:
                continue
            except TimeoutException as e:

                try:
                    button = self.driver.find_element(*locator)
                    if button.text != "Remove":
                        self.driver.execute_script("arguments[0].click();", button)
                        WebDriverWait(self.driver, 3).until(
                            EC.text_to_be_present_in_element(locator, "Remove")
                        )
                        return
                except:
                    pass
                if attempt == 2:
                    raise
            except Exception as e:
                print(f"Неизвестная ошибка: {e}")
                if attempt == 2:
                    raise

        raise Exception(f"Не удалось добавить товар {item_name} после 3 попыток")

    def go_to_card_page(self):
        self.driver.get('https://www.saucedemo.com/cart.html')
        self.driver.maximize_window()