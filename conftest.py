import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    options = webdriver.ChromeOptions()
    #options.add_argument(r"--user-data-dir=C:\Users\Пользователь\Tracing\chrome-profile-tests")
    options.add_argument("--no-first-run")

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