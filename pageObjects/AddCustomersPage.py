from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

class AddCustomers:
    lnkcustomer_customer_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    lnkcustomer_customersub_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnadd_customer_xpath="//a[@class='btn btn-primary']"
    txtbox_email_xpath="//input[@name='Email']"
    txtbox_password_xpath="//input[@id='Password']"
    txtbox_firstname_xpath="//input[@id='FirstName']"
    txtbox_lastname_xpath="//input[@id='LastName']"
    rdbtn_malegender_xpath="//input[@id='Gender_Male']"
    rdbtn_femalegender_xpath="//input[@id='Gender_Female']"
    txtbox_datepicker_xpath="//input[@id='DateOfBirth']"
    txtbox_companyname_xpath="//input[@id='Company']"
    chkbox_istaxexempt_xpath="//input[@id='IsTaxExempt']"
    txt_newsletter_xpath="(//div[@class='k-multiselect-wrap k-floatwrap'])[1]"
    lstitem_yourstorename_xpath="//li[contains(text(),'Your store name')]"
    lstitem_teststore2_xpath="//li[contains(text(),'Test store 2')]"
    txt_customerrole_xpath="(//div[@class='k-multiselect-wrap k-floatwrap'])[2]"
    lstitem_administrators_xpath="//li[contains(text(),'Administrators')]"
    lstitem_forummoderators_xpath="//li[contains(text(),'Forum Moderators')]"
    lstitem_guests_xpath="//li[contains(text(),'Guests')]"
    lstitem_registered_xpath="//li[contains(text(),'Registered')]"
    lstitem_vendors_xpath="//li[contains(text(),'Vendors')]"
    drpdwn_mgrvndr_xpath="//select[@id='VendorId']"
    textbox_admincmt_xpath="//textarea[@class='form-control']"
    btn_save_xpath="//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def clickCustomerModule(self):
        self.driver.find_element(By.XPATH,self.lnkcustomer_customer_xpath).click()

    def clickCustomerSubmodule(self):
        self.driver.find_element(By.XPATH,self.lnkcustomer_customersub_xpath).click()

    def clickAddnewCustomer(self):
        self.driver.find_element(By.XPATH,self.btnadd_customer_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtbox_email_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.txtbox_password_xpath).send_keys(password)

    def setFirstname(self,firstname):
        self.driver.find_element(By.XPATH,self.txtbox_firstname_xpath).send_keys(firstname)

    def setLastname(self,lastname):
        self.driver.find_element(By.XPATH,self.txtbox_lastname_xpath).send_keys(lastname)

    def clickGender(self,gender):
        if gender=='Male':
            self.driver.find_element(By.XPATH,self.rdbtn_malegender_xpath).click()
        elif gender=='Female':
            self.driver.find_element(By.XPATH,self.rdbtn_femalegender_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rdbtn_malegender_xpath).click()

    def setDOB(self,dob):
        self.driver.find_element(By.XPATH,self.txtbox_datepicker_xpath).send_keys(dob)

    def setCompanyname(self,companyname):
        self.driver.find_element(By.XPATH,self.txtbox_companyname_xpath).send_keys(companyname)

    def clickIsTaxexampted(self,taxexampt):
        self.driver.find_element(By.XPATH,self.chkbox_istaxexempt_xpath).click()

    def setNewsletter(self,letter):
        self.driver.find_element(By.XPATH,self.txt_newsletter_xpath).click()
        if letter=='Your store name':
            self.listitem1=self.driver.find_element(By.XPATH,self.lstitem_yourstorename_xpath)
        else:
            self.listitem1=self.driver.find_element(By.XPATH,self.lstitem_teststore2_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem1)

    def setCustomerRole(self,role):
        self.driver.find_element(By.XPATH,self.txt_customerrole_xpath).click()
        if role=='Registered':
            self.listitem=self.driver.find_element(By.XPATH,self.lstitem_registered_xpath)
        elif role=='Administrators':
           self.listitem=self.driver.find_element(By.XPATH,self.lstitem_administrators_xpath)
        elif role=='Guests':
            time.sleep(3)
            #Here user can be Registered (or) Guest, only one.
            self.driver.find_element(By.XPATH, self.lstitem_registered_xpath).click()
            self.listitem=self.driver.find_element(By.XPATH,self.lstitem_guests_xpath)
        elif role=='Forum Moderators':
            self.listitem=self.driver.find_element(By.XPATH,self.lstitem_forummoderators_xpath)
        elif role=='Vendors':
            self.listitem=self.driver.find_element(By.XPATH,self.lstitem_vendors_xpath)
        else:
            self.driver.find_element(By.XPATH, self.lstitem_registered_xpath).click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_guests_xpath)

        time.sleep(3)
        #self.listitem.click()
        self.driver.execute_script("arguments[0].click();",self.listitem)

    def setManagervendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.drpdwn_mgrvndr_xpath))
        drp.select_by_visible_text(value)

    def setAdminComment(self,admincomment):
        self.driver.find_element(By.XPATH,self.textbox_admincmt_xpath).send_keys(admincomment)

    def clickonSave(self):
        self.driver.find_element(By.XPATH,self.btn_save_xpath).click()






