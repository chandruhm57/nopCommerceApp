from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        from selenium.webdriver.chrome.service import Service
        serv_obj=Service("C:\\Drivers\\chromedriver.exe")
        ops=webdriver.ChromeOptions()
        ops.headless=True
        driver=webdriver.Chrome(service=serv_obj,options=ops)
        #driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")
    elif browser=='firefox':
        from selenium.webdriver.firefox.service import Service
        serv_obj = Service("C:\Drivers\geckodriver.exe")
        ops = webdriver.FirefoxOptions()
        ops.headless = True
        driver = webdriver.Firefox(service=serv_obj, options=ops)
    elif browser=='edge':
        from selenium.webdriver.edge.service import Service
        serv_obj = Service("C:\Drivers\msedgedriver.exe")
        ops = webdriver.EdgeOptions()
        ops.headless = True
        driver = webdriver.Edge(service=serv_obj, options=ops)
    else:
        from selenium.webdriver.chrome.service import Service
        serv_obj = Service("C:\\Drivers\\chromedriver.exe")
        ops = webdriver.ChromeOptions()
        ops.headless = True
        driver = webdriver.Chrome(service=serv_obj, options=ops)
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