from selenium.webdriver.common.by import By


class SearchCustomer:
    txtbox_searchemail_id="SearchEmail"
    txtbox_searchFname_id="SearchFirstName"
    txtbox_searchLname_id="SearchLastName"
    btn_search_xpath="//button[@id='search-customers']"

    tbleSearchResults="//table[@role='grid']"
    table_xapth="//table[@id='customers-grid']"
    tableRows_xpath="//table[@id='customers-grid']//tbody//tr"
    tableColumn_xpath="//table[@id='customers-grid']//tbody//tr/td"

    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,email):
        self.driver.find_element(By.ID,self.txtbox_searchemail_id).clear()
        self.driver.find_element(By.ID, self.txtbox_searchemail_id).send_keys(email)

    def setFirstname(self,fname):
        self.driver.find_element(By.ID,self.txtbox_searchFname_id).clear()
        self.driver.find_element(By.ID, self.txtbox_searchFname_id).send_keys(fname)

    def setLastname(self,lname):
        self.driver.find_element(By.ID,self.txtbox_searchLname_id).clear()
        self.driver.find_element(By.ID, self.txtbox_searchLname_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.XPATH,self.btn_search_xpath).click()

    def getNoofRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tableRows_xpath))

    def getNoofColumns(self):
        return len(self.driver.find_elements(By.XPATH,self.tableColumn_xpath))

    def searchCustomerbyEmail(self,email):
        flag=False
        for r in range(1,self.getNoofRows()+1):
            table=self.driver.find_element(By.XPATH,self.table_xapth)
            emailid=table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid==email:
                flag=True
                break
        return flag

    def searchCustomerbyName(self,Name):
        flag=False
        for r in range(1,self.getNoofRows()+1):
            table=self.driver.find_element(By.XPATH,self.table_xapth)
            name=table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name==Name:
                flag=True
                break
        return flag





