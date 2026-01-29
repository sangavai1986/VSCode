from selenium.webdriver.common.by import By
from UIProject.pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")

    def login(self, username, password):
        self.send_keys(self.USERNAME, username, "Username field")
        self.send_keys(self.PASSWORD, password, "Password field")
        self.click(self.LOGIN_BTN, "Login button")