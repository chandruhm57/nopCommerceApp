import pytest
from allure_commons.types import AttachmentType
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import Loggen
import allure

@allure.severity(allure.severity_level.CRITICAL)
class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger=Loggen.loggen()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_homePage_title(self,setup):
        self.logger.info("*********************** Test 001 Login ******************************")
        self.logger.info("*******************Varifyig Home Page Tittle*************************")
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*******************Home page title test is passed*************************")
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="test_homePage_title.png",
                          attachment_type=AttachmentType.PNG)
            #self.driver.save_screenshot(".\\ScreenShots\\" + "test_homePage_title.png")
            self.driver.close()
            self.logger.error("*******************Home page title test is failed*************************")
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("*************************Varifyig Login*******************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.useremail)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("**************************Login test is passed******************************")

        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="test_login.png",
                          attachment_type=AttachmentType.PNG)
            #self.driver.save_screenshot(".\\ScreenShots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("**************************Login test is failed*****************************")
            assert False


