from PageObjects.exceptions_page import ExceptionPage


def test_no_such_element(initialize_browser):
    driver = initialize_browser
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")
    page = ExceptionPage(driver)
    page.is_row_2_displayed()



