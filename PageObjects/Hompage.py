from selenium.webdriver.common.by import By


class HomePage():
    def __init__(self,driver):
        self.driver = driver
        self.get_practice_option = (By.XPATH,"//a[text()='Practice']")

    def get_Practice_page(self):
        self.driver.find_element(*self.get_practice_option).click()
