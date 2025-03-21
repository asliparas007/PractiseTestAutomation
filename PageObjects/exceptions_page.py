from selenium.webdriver.common.by import By


class ExceptionPage:
    def __init__(self,driver):
        self.driver = driver
        self.get_add_button = (By.XPATH,"//button[@id='add_btn']")
        self.get_input_field = (By.XPATH, "(//input[@class='input-field'])[2]")

    def is_row_2_displayed(self):
        self.driver.find_element(*self.get_add_button).click()
        input_field = self.driver.find_element(*self.get_input_field)
        assert input_field.is_displayed() , "Not displayed"
