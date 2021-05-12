from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginPage:

    testuser_email = (By.ID,"Email")
    testuser_password = (By.ID,"Password")
    login_button = (By.XPATH, "//button[normalize-space()='Log in']")
    logout_button = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self,driver):
        self.driver = driver

    def enterusername(self,username):
        self.driver.find_element(*LoginPage.testuser_email).clear()
        return self.driver.find_element(*LoginPage.testuser_email).send_keys(username)

    def enterpassword(self,password):
        self.driver.find_element(*LoginPage.testuser_password).clear()
        return self.driver.find_element(*LoginPage.testuser_password).send_keys(password)

    def clickonloginbutton(self):
        return self.driver.find_element(*LoginPage.login_button).click()

    def clickonlogoutbutton(self):
        return self.driver.find_element(*LoginPage.logout_button).click()

