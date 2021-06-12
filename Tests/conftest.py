import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    #driver=webdriver.Chrome()
    driver=webdriver.Chrome(executable_path="C:\\Users\\sonup\\PycharmProjects\\Project\\Drivers\\chromedriver.exe")
    return driver
########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Tesser Pro'
    config._metadata['Module Name'] = 'Login'
    config._metadata['Tester'] = 'Sony'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)