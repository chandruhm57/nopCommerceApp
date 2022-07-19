import pytest
import allure
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import Loggen
from utilities import XLUtils
import time

@allure.severity(allure.severity_level.MINOR)
class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path=".//TestData//LoginData.xlsx"
    logger=Loggen.loggen()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("************************Test_002_DDT_Login*****************************")
        self.logger.info("*************************Varifyig Login*******************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)

        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of rows in Excel:",self.rows)

        lst_status=[]

        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password=XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp=XLUtils.readData(self.path,'Sheet1',r,3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clicklogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=='Pass':
                    self.logger.info("******Passed*******")
                    self.lp.clicklogout()
                    lst_status.append("Pass")
                elif self.exp=='Fail':
                    self.logger.info("*******Fail*******")
                    lst_status.append("Fail")

            elif act_title!=exp_title:
                if self.exp=='Pass':
                    self.logger.info("*******Failed*******")
                    lst_status.append("Fail")
                elif self.exp=='Fail':
                    self.logger.info("*******Passed*******")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("*******Login DDT test passed*******")
            self.driver.close()
            assert True
        else:
            self.logger.info("*******Login DDT test failed********")
            self.driver.close()
            assert False

        self.logger.info("*******End of Login DDT Test*******")
        self.logger.info("*******Completed TC_LoginDDT_002*******")
