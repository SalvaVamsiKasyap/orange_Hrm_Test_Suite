from selenium.webdriver.common.by import By

class login_Page:

    def __init__(self, driver):
        self.driver = driver


    input_user_name = (By.XPATH, '//input[@name="username"]')

    input_user_password = (By.XPATH, '//input[@name="password"]')


    def enter_user_name(self):

        return self.driver.find_element(*login_Page.input_user_name)

    def enter_user_password(self):

        return self.driver.find_element(*login_Page.input_user_password)


