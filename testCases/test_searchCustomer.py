import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomersPage import AddCustomers
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import Loggen

class Test_004_SearchCustomer:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=Loggen.loggen()

    @pytest.mark.regression
    def test_saerchCustomerByEmail(self,setup):
        self.logger.info("*********** Verify search Customer by Email ***********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        self.logger.info("********** Login successful **********")

        self.logger.info("********* Start Search Customer By Email *********")
        self.addcust=AddCustomers(self.driver)
        self.addcust.clickCustomerModule()
        self.addcust.clickCustomerSubmodule()

        self.logger.info("********* Searching Customer By Email ***********")
        searchcust=SearchCustomer(self.driver)
        searchcust.setEmail('victoria_victoria@nopCommerce.com')
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerbyEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("********* Search CustomerbyEmail test passed *************")
        self.logger.info("*******Completed TC_LoginDDT_002*******")
        self.driver.close()

    @pytest.mark.regression
    def test_saerchCustomerByName(self,setup):
        self.logger.info("*********** Verify search Customer by Name ***********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        self.logger.info("********** Login successful **********")

        self.logger.info("********* Start Search Customer by Name *********")
        self.addcust=AddCustomers(self.driver)
        self.addcust.clickCustomerModule()
        self.addcust.clickCustomerSubmodule()

        self.logger.info("********* Searching Customer By Email ***********")
        searchcust=SearchCustomer(self.driver)
        searchcust.setFirstname('James')
        searchcust.setLastname('Pan')
        searchcust.clickSearch()
        time.sleep(5)

        status = searchcust.searchCustomerbyName("James Pan")
        assert True == status
        self.logger.info("********* Search CustomerbyName test passed *************")

        self.logger.info("******* Completed Test_004_SearchCustomer *******")
        self.driver.close()


