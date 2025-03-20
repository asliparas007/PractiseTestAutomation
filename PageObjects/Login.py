from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin():
    def __init__(self,driver):
        self.driver = driver
        self.get_login_page = (By.LINK_TEXT,"Test Login Page")
        self.get_username = (By.XPATH,"//input[@name='username']")
        self.get_password = (By.XPATH, "//input[@name='password']")
        self.get_submit_button = (By.ID,"submit")
        self.get_success_text = (By.XPATH,"//p[@class='has-text-align-center']")
        self.get_user_logout = (By.LINK_TEXT, "Log out")
        self.get_error_location = (By.ID,"error")

    def loginpageredirect(self):
        self.driver.find_element(*self.get_login_page).click()

    def loginuser(self,username,password):
        self.driver.find_element(*self.get_username).send_keys(username)
        self.driver.find_element(*self.get_password).send_keys(password)
        self.driver.find_element(*self.get_submit_button).click()
    def check_authenticUser(self):
        text = "Congratulations"
        success_text = self.driver.find_element(*self.get_success_text).text
        assert text in success_text, f"{success_text}"

    def logout(self):
        self.driver.find_element(*self.get_user_logout).click

    def error_login(self):
        wait = WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(self.get_error_location))
        assert "invalid" in wait.text, f"{wait.text}"

