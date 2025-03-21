import time

from PageObjects.interactable_exception_page import InteractableExceptionPage


def test_element_not_interactable_exception(initialize_browser):
    driver = initialize_browser
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")
    page = InteractableExceptionPage(driver)
    page.text_saved()
    time.sleep(5)

