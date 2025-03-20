from PageObjects.Login import TestLogin


def test_positiveUserLogin(initialize_browser):
    driver = initialize_browser
    driver.get("https://practicetestautomation.com/practice/")
    login = TestLogin(driver)
    login.loginpageredirect()
    login.loginuser("student","Password123")
    url = "practicetestautomation.com/logged-in-successfully/"
    assert url in driver.current_url, f"Expected {url}, but got {driver.current_url}"
    login.check_authenticUser()
    login.logout()


def test_negativeUserName(initialize_browser):
    driver = initialize_browser
    driver.get("https://practicetestautomation.com/practice-test-login/")
    login = TestLogin(driver)
    login.loginuser("incorrectUser","Password123")
    login.error_login()

def test_negativePassword(initialize_browser):
    driver = initialize_browser
    driver.get("https://practicetestautomation.com/practice-test-login/")
    login = TestLogin(driver)
    login.loginuser("student","Password1234")
    login.error_login()




