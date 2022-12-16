import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class pim_Module_Page():

    def __init__(self,driver):

        self.driver = driver

    locate_add_button = (By.XPATH,"//div[@class='orangehrm-header-container']/button")

    locate_first_name = (By.XPATH,"//input[@name='firstName']")

    locate_middle_name = (By.XPATH,'//input[@name="middleName"]')

    locate_last_name = (By.XPATH,'//input[@name="lastName"]')

    locate_employee_id = (By.XPATH,'//label[text()="Employee Id"]//parent::div//following-sibling::div/input')

    locate_submit_button = (By.XPATH,'//button[@type="submit"]')

    #locate_verifier = (By.XPATH,'//label[text()="Employee Name"]//parent::div//following-sibling::div/div/div/input')

    #suggestions_select = (By.XPATH,"//span[text()='salva vamsi kasyap']")

    edit_existing_emp_details = (By.XPATH,"//i[@class='oxd-icon bi-pencil-fill']//parent::button")

    #edit_save = (By.XPATH,"//p[text()=' * Required']//parent::div/button")

    edit_save = (By.XPATH,'//label[text()="Blood Type"]//parent::div//parent::div//parent::div//parent::div//parent::div//parent::form/div/button')

    delete_existing_emp_details = (By.XPATH,"//i[@class='oxd-icon bi-trash']//parent::button")

    confirm_deletion = (By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin"]')

    def clicking_Add_Button(self):

        add = self.driver.find_element(*pim_Module_Page.locate_add_button)
        add.click()

    def entering_First_Name(self):

        return self.driver.find_element(*pim_Module_Page.locate_first_name)

    def entering_Middle_Name(self):

        return self.driver.find_element(*pim_Module_Page.locate_middle_name)

    def entering_Last_Name(self):

        return self.driver.find_element(*pim_Module_Page.locate_last_name)

    def entering_Employee_Id(self):

        return self.driver.find_element(*pim_Module_Page.locate_employee_id)

    def clicking_Save_Button(self):

        button = self.driver.find_element(*pim_Module_Page.locate_submit_button)
        button.click()

    #def performing_verification(self):

        #give_input = self.driver.find_element(*pim_Module_Page.locate_verifier)

        #select_suggestion = self.driver.find_element(*pim_Module_Page.suggestions_select)

        #select_suggestion.click()

    def editing_existing_employee_details(self):

        button = self.driver.find_element(*pim_Module_Page.edit_existing_emp_details)
        button.click()
        # self.driver.find_element(*pim_Module_Page.locate_first_name)
        #
        # self.driver.find_element(*pim_Module_Page.locate_middle_name)
        #
        # self.driver.find_element(*pim_Module_Page.locate_last_name)
        #
        # self.driver.find_element(*pim_Module_Page.locate_employee_id)

    def saving_post_editing(self):

        button = self.driver.find_element(*pim_Module_Page.edit_save)
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.find_element(By.XPATH,"//label[text()='Smoker']"))
        time.sleep(5)
        button.click()
        #return 'successfully edited'


    def delete_existing_employee_details(self):

        button = self.driver.find_element(*pim_Module_Page.delete_existing_emp_details)
        button.click()
        time.sleep(5)
        deletion_button = self.driver.find_element(*pim_Module_Page.confirm_deletion)
        deletion_button.click()
        #//p[text()='Successfully Deleted']
        #//button[@class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin"]
        #return "successfully deleted"
