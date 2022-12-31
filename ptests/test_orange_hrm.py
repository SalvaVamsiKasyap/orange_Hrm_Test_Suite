import time

import pytest
from selenium.webdriver import ActionChains, Keys

from pageObjects.login_Page import login_Page
from pageObjects.home_Page import home_Page
from pageObjects.pim_Module_Page import pim_Module_Page
from pageObjects.admin_Module_Page import admin_Module_Page
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
@pytest.mark.usefixtures("setup")
class Testorange_hrm(BaseClass):

    def test_successfullogin(self):

        log = self.get_logger()
        # orange-hrm login page
        #A = ActionChains(self.driver)
        ohlp = login_Page(self.driver)
        self.verify_element_presence('//input[@name="username"]')
        username_inp = ohlp.enter_user_name()
        log.info("Entering the username..")
        username_inp.send_keys('Admin')
        log.info("Entered user name as Admin.")
        userpassword_inp = ohlp.enter_user_password()
        log.info("Entering the password")
        userpassword_inp.send_keys('admin123')
        log.info("Entered the password..")
        userpassword_inp.send_keys(Keys.ENTER)
        #self.verify_element_presence("//p[text()='Invalid credentials']")
        #ohlp.error_message()
        log.info("Navigating to the homepage..")
        self.verify_element_presence("//ul[@class='oxd-main-menu']")
        log.info("Successfully Navigated to home page...")



@pytest.mark.usefixtures("setup")
class Testorange_hrm_unsuccessful(BaseClass):

    def test_unsuccessfullogin(self):

        desired_Message = "Invalid credentials"
        log = self.get_logger()
        # orange-hrm login page
        #A = ActionChains(self.driver)
        ohlp = login_Page(self.driver)
        self.verify_element_presence('//input[@name="username"]')
        username_inp = ohlp.enter_user_name()
        log.info("Entering the username..")
        username_inp.send_keys('Admin')
        log.info("Entered user name as Admin.")
        userpassword_inp = ohlp.enter_user_password()
        log.info("Entering the password")
        userpassword_inp.send_keys('vamsi')
        log.info("Entered the password..")
        userpassword_inp.send_keys(Keys.ENTER)
        #log.info("Navigating to the homepage..")
        log.info(self.verify_element_presence("//p[text()='Invalid credentials']"))
        assert self.verify_element_presence('//p[text()="Invalid credentials"]') == desired_Message
        #ohlp.error_message()
        #log.info("It seems you have entered invalid credentiails")


@pytest.mark.usefixtures('setup')
class Testorange_hrm_add_user_in_pim(BaseClass):

    def test_adduser(self):
        desired_Message = "Successfully Saved"
        log = self.get_logger()
        ohlp = login_Page(self.driver)
        self.verify_element_presence('//input[@name="username"]')
        username_inp = ohlp.enter_user_name()
        log.info("Entering the username..")
        username_inp.send_keys('Admin')
        log.info("Entered user name as Admin.")
        userpassword_inp = ohlp.enter_user_password()
        log.info("Entering the password")
        userpassword_inp.send_keys('admin123')
        log.info("Entered the password..")
        userpassword_inp.send_keys(Keys.ENTER)
        hmp = home_Page(self.driver)
        self.verify_element_presence('//a[@href="/web/index.php/pim/viewPimModule"]')
        log.info("Clicking on PIM Module..")
        hmp.selecting_Pim_Module()
        pim_M_P = pim_Module_Page(self.driver)
        self.verify_element_presence("//div[@class='orangehrm-header-container']/button")
        log.info("Entered the PIM Module page")
        self.verify_element_presence("//div[@class='orangehrm-header-container']/button")
        add_but = pim_M_P.clicking_Add_Button()
        self.verify_element_presence("//input[@name='firstName']")
        fris_nam = pim_M_P.entering_First_Name()
        fris_nam.send_keys("salva")
        self.verify_element_presence('//input[@name="middleName"]')
        midd_nam = pim_M_P.entering_Middle_Name()
        midd_nam.send_keys("vamsi")
        self.verify_element_presence('//input[@name="lastName"]')
        last_nam = pim_M_P.entering_Last_Name()
        last_nam.send_keys("kasyap")
        self.verify_element_presence('//label[text()="Employee Id"]//parent::div//following-sibling::div/input')
        emp_id = pim_M_P.entering_Employee_Id()
        emp_id.send_keys('999')
        sub_but = pim_M_P.clicking_Save_Button()
        log.info(self.verify_element_presence("//p[text()='Successfully Saved']"))
        assert self.verify_element_presence('//p[text()="Successfully Saved"]') == desired_Message
        #log.info("Verified..")


@pytest.mark.usefixtures('setup')
class Testorange_hrm_edit_user_in_pim(BaseClass):

    def test_edituser(self):
        desired_Message = "Successfully Saved"
        log = self.get_logger()
        ohlp = login_Page(self.driver)
        self.verify_element_presence('//input[@name="username"]')
        username_inp = ohlp.enter_user_name()
        log.info("Entering the username..")
        username_inp.send_keys('Admin')
        log.info("Entered user name as Admin.")
        userpassword_inp = ohlp.enter_user_password()
        log.info("Entering the password")
        userpassword_inp.send_keys('admin123')
        log.info("Entered the password..")
        userpassword_inp.send_keys(Keys.ENTER)
        hmp = home_Page(self.driver)
        self.verify_element_presence('//a[@href="/web/index.php/pim/viewPimModule"]')
        log.info("Clicking on PIM Module..")
        hmp.selecting_Pim_Module()
        log.info("Successfully Clicked PIM Module")
        pim_M_P = pim_Module_Page(self.driver)
        self.verify_element_presence("//i[@class='oxd-icon bi-pencil-fill']//parent::button")
        log.info("Clicking on edit button..")
        pim_M_P.editing_existing_employee_details()
        log.info("Successfully clicked edit button")
        self.verify_element_presence("//input[@name='firstName']")
        fris_nam = pim_M_P.entering_First_Name()
        fris_nam.clear()
        fris_nam.send_keys("salva")
        log.info("Entered the first name as a part of editing..")
        self.verify_element_presence("//input[@name='middleName']")
        middl_nam = pim_M_P.entering_Middle_Name()
        log.info("Entering the middle name as a part of editing..")
        middl_nam.clear()
        middl_nam.send_keys('gandhi')
        log.info("Entered the middlename name as a part of editing..")
        self.verify_element_presence("//input[@name='lastName']")
        las_nam = pim_M_P.entering_Last_Name()
        log.info("Entering the last name as a part of editing..")
        las_nam.clear()
        las_nam.send_keys("damodara")
        log.info("Entered the last name as a part of editing..")
        self.verify_element_presence('//label[text()="Employee Id"]//parent::div//following-sibling::div/input')
        employe_id = pim_M_P.entering_Employee_Id()
        log.info("Entering the employee id as a part of editing..")
        employe_id.send_keys("3456")
        #employe_id.send_keys(Keys.ENTER)
        log.info("Entered the employee id as a part of editing..")
        self.verify_element_presence('//label[text()="Blood Type"]//parent::div//parent::div//parent::div//parent::div//parent::div//parent::form/div/button')
        edit = pim_M_P.saving_post_editing()
        log.info(self.verify_element_presence('//p[text()="Successfully Saved"]'))
        assert self.verify_element_presence('//p[text()="Successfully Saved"]') == desired_Message
#
#         #log.info(f"Editing operation successful {edit}")


@pytest.mark.usefixtures('setup')
class Testorange_hrm_delte_user_in_pim(BaseClass):

    def test_deleteuser(self):

        desired_Message = "Successfully Deleted"
        log = self.get_logger()
        ohlp = login_Page(self.driver)
        self.verify_element_presence('//input[@name="username"]')
        username_inp = ohlp.enter_user_name()
        log.info("Entering the username..")
        username_inp.send_keys('Admin')
        log.info("Entered user name as Admin.")
        userpassword_inp = ohlp.enter_user_password()
        log.info("Entering the password")
        userpassword_inp.send_keys('admin123')
        log.info("Entered the password..")
        userpassword_inp.send_keys(Keys.ENTER)
        hmp = home_Page(self.driver)
        self.verify_element_presence('//a[@href="/web/index.php/pim/viewPimModule"]')
        log.info("Clicking on PIM Module..")
        hmp.selecting_Pim_Module()
        log.info("Successfully Clicked PIM Module")
        pim_M_P = pim_Module_Page(self.driver)
        log.info("Clicking on delete icon..")
        self.verify_element_presence("//i[@class='oxd-icon bi-trash']//parent::button")
        pim_M_P.delete_existing_employee_details()
        log.info(self.verify_element_presence("//p[text()='Successfully Deleted']"))
        assert self.verify_element_presence('//p[text()="Successfully Deleted"]') == desired_Message



@pytest.mark.usefixtures('setup')
class Testorange_hrm_admin_page_menu_options_search(BaseClass):

    def test_adminoptionssearch(self):

        desired_Message = ""
        log = self.get_logger()
        ohlp = login_Page(self.driver)
        self.verify_element_presence('//input[@name="username"]')
        username_inp = ohlp.enter_user_name()
        log.info("Entering the username..")
        username_inp.send_keys('Admin')
        log.info("Entered user name as Admin.")
        userpassword_inp = ohlp.enter_user_password()
        log.info("Entering the password")
        userpassword_inp.send_keys('admin123')
        log.info("Entered the password..")
        userpassword_inp.send_keys(Keys.ENTER)
        hmp = home_Page(self.driver)
        self.verify_element_presence('//a[@href="/web/index.php/admin/viewAdminModule"]')
        log.info("Clicking on admin module..")
        hmp.selecting_Admin_Module()
        log.info("Successfully clicked on admin module")
        ohap = admin_Module_Page(self.driver)
        self.verify_element_presence("//ul[@class='oxd-main-menu']/li/a/span")
        options_To_Check = ohap.verifying_admin_options()
        log.info(f"User is able to search all {ohap.searching_The_Options(options_To_Check)} options")



@pytest.mark.usefixtures('setup')
class Testorange_hrm_admin_page_user_managment(BaseClass):

    def test_adminusermanagmentoption(self):

        desired_Message = ""
        log = self.get_logger()
        ohlp = login_Page(self.driver)
        self.verify_element_presence('//input[@name="username"]')
        username_inp = ohlp.enter_user_name()
        log.info("Entering the username..")
        username_inp.send_keys('Admin')
        log.info("Entered user name as Admin.")
        userpassword_inp = ohlp.enter_user_password()
        log.info("Entering the password")
        userpassword_inp.send_keys('admin123')
        log.info("Entered the password..")
        userpassword_inp.send_keys(Keys.ENTER)
        hmp = home_Page(self.driver)
        self.verify_element_presence('//a[@href="/web/index.php/admin/viewAdminModule"]')
        log.info("Clicking on admin module..")
        hmp.selecting_Admin_Module()
        log.info("Successfully clicked on admin module")
        ohap = admin_Module_Page(self.driver)
        self.verify_element_presence("//ul[@class='oxd-main-menu']/li/a/span")
        options_To_Check = ohap.verifying_admin_options()
        log.info(ohap.clicking_on_usermanagment())

    def test_admincreateemployeepim(self):

        desired_Message = "Successfully Saved"
        log = self.get_logger()
        ohlp = login_Page(self.driver)
        self.verify_element_presence('//input[@name="username"]')
        username_inp = ohlp.enter_user_name()
        log.info("Entering the username..")
        username_inp.send_keys('Admin')
        log.info("Entered user name as Admin.")
        userpassword_inp = ohlp.enter_user_password()
        log.info("Entering the password")
        userpassword_inp.send_keys('admin123')
        log.info("Entered the password..")
        userpassword_inp.send_keys(Keys.ENTER)
        hmp = home_Page(self.driver)
        self.verify_element_presence('//a[@href="/web/index.php/admin/viewAdminModule"]')
        log.info("Clicking on admin module..")
        hmp.selecting_Admin_Module()
        log.info("Successfully clicked on admin module")
        #ohap = admin_Module_Page(self.driver)
        #self.verify_element_presence("//ul[@class='oxd-main-menu']/li/a/span")
        #options_To_Check = ohap.verifying_admin_options()
        #log.info(ohap.clicking_on_usermanagment())
        ohap = admin_Module_Page(self.driver)
        self.verify_element_presence('//a[@href="/web/index.php/pim/viewPimModule"]')
        ohap.clicking_pimoption()
        ohap.verifying_admin_options()
        self.verify_element_presence("//div[@class='orangehrm-header-container']/button")
        ohap.clicking_addoption()
        self.verify_element_presence("//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")
        ohap.clicking_toggleoption()
        result = ohap.providing_details()
        assert self.verify_element_presence('//p[text()="Successfully Saved"]') == desired_Message
        self.verify_element_presence(f'//h6[text()="{result}"]')
        self.driver.save_screenshot("image.png")
        return result



#//a[text()='Memberships']
@pytest.mark.usefixtures('setup')
class Testorange_hrm_pim_page_emp_details_validation(BaseClass):
    def test_validateemppersonaldetails(self):
        desired_Message = "Successfully Saved"
        log = self.get_logger()
        ohlp = login_Page(self.driver)
        self.verify_element_presence('//input[@name="username"]')
        username_inp = ohlp.enter_user_name()
        log.info("Entering the username..")
        username_inp.send_keys('Admin')
        log.info("Entered user name as Admin.")
        userpassword_inp = ohlp.enter_user_password()
        log.info("Entering the password")
        userpassword_inp.send_keys('admin123')
        log.info("Entered the password..")
        userpassword_inp.send_keys(Keys.ENTER)
        hmp = home_Page(self.driver)
        self.verify_element_presence('//a[@href="/web/index.php/admin/viewAdminModule"]')
        log.info("Clicking on admin module..")
        hmp.selecting_Admin_Module()
        log.info("Successfully clicked on admin module")
        # ohap = admin_Module_Page(self.driver)
        # self.verify_element_presence("//ul[@class='oxd-main-menu']/li/a/span")
        # options_To_Check = ohap.verifying_admin_options()
        # log.info(ohap.clicking_on_usermanagment())
        ohap = admin_Module_Page(self.driver)
        self.verify_element_presence('//a[@href="/web/index.php/pim/viewPimModule"]')
        ohap.clicking_pimoption()
        ohap.verifying_admin_options()
        self.verify_element_presence("//div[@class='orangehrm-header-container']/button")
        ohap.clicking_addoption()
        self.verify_element_presence("//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")
        ohap.clicking_toggleoption()
        result = ohap.providing_details()
        assert self.verify_element_presence('//p[text()="Successfully Saved"]') == desired_Message
        self.verify_element_presence(f'//h6[text()="{result}"]')
        self.driver.save_screenshot("image.png")
        ohpp = pim_Module_Page(self.driver)
        emp_options = ['Personal Details', 'Contact Details', 'Emergency Contacts', 'Dependents', 'Immigration', 'Job', 'Salary', 'Tax Exemptions', 'Report-to', 'Qualifications', 'Memberships']
        assert emp_options == ohpp.validating_emp_personal_details()


@pytest.mark.usefixtures('setup')
class Testorange_hrm_pim_page_emp_personal_details_updation(BaseClass):
    def test_updateemppersonaldetails(self):
        desired_Message = "Successfully Saved"
        log = self.get_logger()
        ohlp = login_Page(self.driver)
        self.verify_element_presence('//input[@name="username"]')
        username_inp = ohlp.enter_user_name()
        log.info("Entering the username..")
        username_inp.send_keys('Admin')
        log.info("Entered user name as Admin.")
        userpassword_inp = ohlp.enter_user_password()
        log.info("Entering the password")
        userpassword_inp.send_keys('admin123')
        log.info("Entered the password..")
        userpassword_inp.send_keys(Keys.ENTER)
        hmp = home_Page(self.driver)
        self.verify_element_presence('//a[@href="/web/index.php/admin/viewAdminModule"]')
        log.info("Clicking on admin module..")
        hmp.selecting_Admin_Module()
        log.info("Successfully clicked on admin module")
        # ohap = admin_Module_Page(self.driver)
        # self.verify_element_presence("//ul[@class='oxd-main-menu']/li/a/span")
        # options_To_Check = ohap.verifying_admin_options()
        # log.info(ohap.clicking_on_usermanagment())
        ohap = admin_Module_Page(self.driver)
        self.verify_element_presence('//a[@href="/web/index.php/pim/viewPimModule"]')
        ohap.clicking_pimoption()
        ohap.verifying_admin_options()
        self.verify_element_presence("//div[@class='orangehrm-header-container']/button")
        ohap.clicking_addoption()
        self.verify_element_presence("//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")
        ohap.clicking_toggleoption()
        result = ohap.providing_details()
        assert self.verify_element_presence('//p[text()="Successfully Saved"]') == desired_Message
        self.verify_element_presence(f'//h6[text()="{result}"]')
        self.driver.save_screenshot("image.png")
        ohpp = pim_Module_Page(self.driver)
        emp_options = ['Personal Details', 'Contact Details', 'Emergency Contacts', 'Dependents', 'Immigration', 'Job', 'Salary', 'Tax Exemptions', 'Report-to', 'Qualifications', 'Memberships']
        assert emp_options == ohpp.validating_emp_personal_details()
        ohpp.updating_personal_details()
        assert self.verify_element_presence('//p[text()="Successfully Saved"]') == desired_Message
        self.driver.save_screenshot("personal_details.png")
        time.sleep(10)









