import time

from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
from selenium.webdriver.common.keys import Keys
from tabulate import tabulate


class admin_Module_Page(BaseClass):

    def __init__(self,driver):

        self.driver = driver
        #.get_attribute("innerHTML")

    admin_options = (By.XPATH,"//ul[@class='oxd-main-menu']/li/a/span")

    search_locator = (By.XPATH,'//input[@placeholder="Search"]')

    result_locator = (By.XPATH,'//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"]//parent::a')

    usermanagment_locator = (By.XPATH,'//span[text()="User Management "]')

    useroption_locator = (By.XPATH,'//ul/li/a[text()="Users"]')

    userrole_locator = (By.XPATH,"//label[text()='User Role']//parent::div//parent::div/div/div")

    adminoption_locator =(By.XPATH,"//div[@role='option']/span[text()='Admin']")

    status_locator = (By.XPATH,"//label[text()='Status']//parent::div//parent::div/div/div")

    enabledoption_locator = (By.XPATH,'//span[text()="Enabled"]')

    ESSoption_locator = (By.XPATH,"//div[@role='option']/span[text()='ESS']")

    disabledoption_locator = (By.XPATH,'//span[text()="Disabled"]')

    def verifying_admin_options(self):

        options = self.driver.find_elements(*admin_Module_Page.admin_options)
        counter = 0
        text_options = []
        if len(options) == 11:
            for option in options:
                if option != '':
                    counter += 1
                    text_options.append(option.text)
        assert counter == len(options)
        return text_options

    #//input[@placeholder="Search"]

    def searching_The_Options(self,options_To_Check):

        search_locator = self.driver.find_element(*admin_Module_Page.search_locator)
        result_locator = self.driver.find_element(*admin_Module_Page.result_locator)
        counter = 0
        for option in options_To_Check:
            search_locator.send_keys(option)
            self.verify_element_presence('//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"]')
            search_locator.send_keys(Keys.CONTROL, 'a')
            search_locator.send_keys(Keys.BACKSPACE)
            counter += 1
            #result_locator.click()
            #self.verify_element_presence("//ul[@class='oxd-main-menu']")
        assert counter == 11
        return counter

    def clicking_on_usermanagment(self):

        usr_mngmt_options = self.driver.find_element(*admin_Module_Page.usermanagment_locator)
        usr_mngmt_options.click()
        self.verify_element_presence('//ul/li/a[text()="Users"]')
        usr_option = self.driver.find_element(*admin_Module_Page.useroption_locator)
        usr_option.click()
        #//div[@role='option']/span[text()='Admin']
        #//div[@class="oxd-select-text oxd-select-text--focus"]
        self.verify_element_presence("//label[text()='User Role']//parent::div//parent::div/div/div")
        userrole_loc = self.driver.find_element(*admin_Module_Page.userrole_locator)
        userrole_loc.click()
        admin_option = self.driver.find_element(*admin_Module_Page.adminoption_locator)
        admin_option.click()
        self.verify_element_presence("//label[text()='Status']//parent::div//parent::div/div/div")
        status_locator = self.driver.find_element(*admin_Module_Page.status_locator)
        status_locator.click()
        enabledoption_locator = self.driver.find_element(*admin_Module_Page.enabledoption_locator)
        enabledoption_locator.click()
        admin_final = self.verify_element_presence("//label[text()='User Role']//parent::div//parent::div/div/div/div/div[text()='Admin']")
        admin_final_status = self.verify_element_presence("//label[text()='Status']//parent::div//parent::div/div/div/div/div[text()='Enabled']")
        userrole_loc = self.driver.find_element(*admin_Module_Page.userrole_locator)
        userrole_loc.click()
        ESS_option = self.driver.find_element(*admin_Module_Page.ESSoption_locator)
        ESS_option.click()
        status_locator = self.driver.find_element(*admin_Module_Page.status_locator)
        status_locator.click()
        disabledoption_locator = self.driver.find_element(*admin_Module_Page.disabledoption_locator)
        disabledoption_locator.click()
        ESS_final = self.verify_element_presence("//label[text()='User Role']//parent::div//parent::div/div/div/div/div[text()='ESS']")
        ESS_final_status = self.verify_element_presence("//label[text()='Status']//parent::div//parent::div/div/div/div/div[text()='Disabled']")
        #//div[text()='ESS']
        mydata = [
            [admin_final, admin_final_status],
            [ESS_final, ESS_final_status],
            ]
        head = ["User Role", "Status"]
        return tabulate(mydata, headers=head, tablefmt="grid")

