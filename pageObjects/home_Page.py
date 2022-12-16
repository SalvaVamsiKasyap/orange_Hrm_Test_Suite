from selenium.webdriver.common.by import By

class home_Page():

    def __init__(self,driver):

        self.driver = driver

    pim_module = (By.XPATH,'//a[@href="/web/index.php/pim/viewPimModule"]')

    def selecting_Pim_Module(self):

        pim = self.driver.find_element(*home_Page.pim_module)
        pim.click()