from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        from selenium.webdriver.chrome.service import Service
        serv_obj=Service("C:\\Drivers\\chromedriver.exe")
        driver=webdriver.Chrome(service=serv_obj)
        #driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")
    elif browser=='firefox':
        from selenium.webdriver.firefox.service import Service
        serv_obj = Service("C:\\Drivers\\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
        #driver=webdriver.Firefox(executable_path="C:\\Drivers\\geckodriver.exe")
    else:
        from selenium.webdriver.chrome.service import Service
        serv_obj=Service("C:\\Drivers\\chromedriver.exe")
        driver=webdriver.Chrome(service=serv_obj)
        #driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")
    return driver

def pytest_addoption(parser): #This will get the value from CLI/Hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will return the Browser value to setup method
    return request.config.getoption("--browser")

############### PyTest HTML Reports #####################

# It is hook for adding Environment info to HTML Report.
def pytest_configure(config):
    config._metadata['Project Name']='nopCommerceApp'
    config._metadata['Module Name']='Customers'
    config._metadata['Tester']='Chandrashekar'

# It is hook for delete/Modify Environment info to HTML Report.
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA HOME",None)
    metadata.pop("Plugins",None)