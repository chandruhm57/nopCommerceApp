import random
import string
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from pageObjects.AddCustomersPage import AddCustomers
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import Loggen
from utilities.readProperties import ReadConfig

@allure.severity(allure.severity_level.CRITICAL)
class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = Loggen.loggen()

    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_addCustomer(self,setup):
        self.logger.info("********** Test_003_AddCustomer ************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.useremail)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        self.logger.info("********** Login successful **************")
        self.logger.info("********** Starting AddCustomer Test *************")

        self.addcust=AddCustomers(self.driver)
        self.addcust.clickCustomerModule()
        self.addcust.clickCustomerSubmodule()
        self.addcust.clickAddnewCustomer()
        self.logger.info("********* Providing Customer Info ***********")
        self.email=random_generator()+"@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword('test123')
        self.addcust.setFirstname('Chandra')
        self.addcust.setLastname('Shekar')
        self.addcust.clickGender('Male')
        self.addcust.setDOB('7/28/1991')  #Formate: MM/DD/YYYY
        self.addcust.setCompanyname('busyQA')
        #self.addcust.setCustomerRole('Forum Moderators')
        #self.addcust.setManagervendor('Vendor1')
        self.addcust.setAdminComment('This is for testing.........')
        self.addcust.clickonSave()

        self.logger.info("********** Saving customer inf **************")

        self.logger.info("********** Add customer validation started ***********")

        self.msg=self.driver.find_element(By.TAG_NAME,"body").text

        if "The new customer has been added successfully." in self.msg:
            assert True==True
            self.logger.info("********* Add Customer Test Passed **********")
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="test_addcustomer_scr.png",
                                   attachment_type=AttachmentType.PNG)
            #self.driver.save_screenshot(".\\ScreenShots\\"+"test_addcustomer_scr.png") #screenshot
            self.logger.info("********* Add Customer Test Failed **********")
            assert True==False

        self.driver.close()
        self.logger.info("********** Ending Add Customer Test **********")

def random_generator(size=8, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))