import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture
def chrome_browser():
    """Фикстура для Chrome"""
    options = ChromeOptions()
    options.add_argument("--no-first-run")
    # Отключаем менеджер паролей
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(4)
    yield driver
    driver.quit()


@pytest.fixture
def firefox_browser():
    """Фикстура для Firefox"""
    options = FirefoxOptions()
    options.add_argument("--no-first-run")
    # Отключаем менеджер паролей (Firefox способ)
    options.set_preference("signon.autofillForms", False)
    options.set_preference("signon.rememberSignons", False)
    options.set_preference("services.passwordSaving.enabled", False)

    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(4)
    yield driver
    driver.quit()