import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class InteractableExceptionPage:
    def __init__(self,driver):
        self.driver = driver
        self.get_add_button = (By.XPATH,"//button[@id='add_btn']")
        self.get_row_confirmation = (By.XPATH,"//div[@id='confirmation']")
        self.get_input_section = (By.XPATH,"(//input[@class='input-field'])[2]")
        self.get_save_button = (By.XPATH,"(//button[@id='save_btn'])[2]")


    def text_saved(self):
        self.driver.find_element(*self.get_add_button).click()
        print("add clicked")
        WebDriverWait(self.driver,5).until(expected_conditions.presence_of_element_located(self.get_row_confirmation))
        self.driver.find_element(*self.get_input_section).send_keys("Test")
        print("test enter")
        self.driver.find_element(*self.get_save_button).click()
        print("saved")


