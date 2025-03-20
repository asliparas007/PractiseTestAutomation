import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def initialize_browser():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


