import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def chrome_browser():
    """Фикстура, которая запускает Chrome и закрывает его после теста."""
    # Автоматическая установка драйвера через webdriver-manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver  # передаём драйвер в тест
    driver.quit()  # закрываем браузер после завершения теста
