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

    emp_details_ver = (By.XPATH,"//div[@class='orangehrm-tabs']/div")

    input_first_name = (By.XPATH,'//input[@name="firstName"]')

    input_middle_name = (By.XPATH,'//input[@name="middleName"]')

    input_last_name = (By.XPATH,'//input[@name="lastName"]')

    input_nick_name = (By.XPATH,"//label[text()='Nickname']//parent::div//parent::div/div/input")

    input_emp_id = (By.XPATH,"//label[text()='Employee Id']//parent::div//parent::div/div/input")

    input_other_id = (By.XPATH,"//label[text()='Other Id']//parent::div//parent::div/div/input")

    input_driver_license_number = (By.XPATH,"//label[text()=\"Driver's License Number\"]//parent::div//parent::div/div/input")

    input_license_expiry_date = (By.XPATH,"//label[text()='License Expiry Date']//parent::div//parent::div//parent::div/div/div/div/div/input")

    input_ssn_number = (By.XPATH,"//label[text()='SSN Number']//parent::div//parent::div/div/input")

    input_sin_number = (By.XPATH,"//label[text()='SIN Number']//parent::div//parent::div/div/input")

    #//label[text()='Nationality']//parent::div//parent::div/div/div/div/div[@class='oxd-select-text-input']

    #//div[@role='listbox']/div/span[text()='Indian']

    input_nationality = (By.XPATH,"//label[text()='Nationality']//parent::div//parent::div/div/div/div/div[@class='oxd-select-text-input']")

    select_nationality_option = (By.XPATH,"//div[@role='listbox']/div/span[text()='Indian']")

    input_maritalstatus = (By.XPATH,"//label[text()='Marital Status']//parent::div//parent::div/div/div/div/div[@class='oxd-select-text-input']")

    select_marital_status_option = (By.XPATH,"//div[@role='listbox']/div/span[text()='Other']")

    input_date_of_birth = (By.XPATH,"//label[text()='Date of Birth']//parent::div//parent::div/div/div/div/input")

    input_military_service = (By.XPATH,"//label[text()='Military Service']//parent::div//parent::div/div/input")

    input_Blood_type = (By.XPATH,'//label[text()="Blood Type"]//parent::div//parent::div/div/div[@class="oxd-select-wrapper"]/div/div[@class="oxd-select-text-input"]')

    blood_type_option = (By.XPATH,'//div[@role="listbox"]/div/span[text()="A+"]')

    save_button_click_personal_details = (By.XPATH,'//h6[text()="Custom Fields"]/parent::div/form/div/button')


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

    def validating_emp_personal_details(self):

        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.find_element(*pim_Module_Page.emp_details_ver))
        personal_details_options = self.driver.find_elements(*pim_Module_Page.emp_details_ver)
        options_text = []
        for option in personal_details_options:
            options_text.append(option.text)
        return options_text

    def updating_personal_details(self):

        first_name = self.driver.find_element(*pim_Module_Page.input_first_name)
        first_name.send_keys('vaibhav')
        middle_name = self.driver.find_element(*pim_Module_Page.input_middle_name)
        middle_name.send_keys('valli')
        last_name = self.driver.find_element(*pim_Module_Page.input_last_name)
        last_name.send_keys('khan')
        nick_name = self.driver.find_element(*pim_Module_Page.input_nick_name)
        nick_name.send_keys('kitchu')
        emp_id = self.driver.find_element(*pim_Module_Page.input_emp_id)
        emp_id.send_keys('6789')
        oth_id = self.driver.find_element(*pim_Module_Page.input_other_id)
        oth_id.send_keys('8765')
        license_number = self.driver.find_element(*pim_Module_Page.input_driver_license_number)
        license_number.send_keys('357247')
        license_exp_date = self.driver.find_element(*pim_Module_Page.input_license_expiry_date)
        license_exp_date.send_keys('2022-10-03')
        ssn_number = self.driver.find_element(*pim_Module_Page.input_ssn_number)
        ssn_number.send_keys('45675221')
        sin_number = self.driver.find_element(*pim_Module_Page.input_sin_number)
        sin_number.send_keys('91578')
        nationality = self.driver.find_element(*pim_Module_Page.input_nationality)
        nationality.click()
        nationality_option = self.driver.find_element(*pim_Module_Page.select_nationality_option)
        nationality_option.click()
        marital_stats = self.driver.find_element(*pim_Module_Page.input_maritalstatus)
        marital_stats.click()
        marital_stats_option = self.driver.find_element(*pim_Module_Page.select_marital_status_option)
        marital_stats_option.click()
        dob = self.driver.find_element(*pim_Module_Page.input_date_of_birth)
        mili_ser = self.driver.find_element(*pim_Module_Page.input_military_service)
        mili_ser.send_keys('no')
        blood_type = self.driver.find_element(*pim_Module_Page.input_Blood_type)
        blood_type.click()
        blood_type_option = self.driver.find_element(*pim_Module_Page.blood_type_option)
        blood_type_option.click()
        save_button = self.driver.find_element(*pim_Module_Page.save_button_click_personal_details)
        save_button.click()