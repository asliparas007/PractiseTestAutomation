import time

from PageObjects.Hompage import HomePage

def test_HomePage(initialize_browser):
    driver = initialize_browser
    home_page = HomePage(driver)
    home_page.get_Practice_page()
    time.sleep(5)
