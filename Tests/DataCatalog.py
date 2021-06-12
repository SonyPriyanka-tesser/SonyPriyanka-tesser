import time
import pytest
from selenium import webdriver
from self import self

from Pages.DataCatalogPage import DataCatalogPage
from Pages.IngestPage import IngestPage
from Pages.LoginPage import LoginPage
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig

class Test_002_DataCatalog:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    server = ReadConfig.getServer()
    portnumber = ReadConfig.getPortNumber()
    Database = ReadConfig.getDatabases()
    user = ReadConfig.getUser()
    pwd = ReadConfig.getPass()

    logger = LogGen.loggen()

    def test_003_Table_Copy(self, setup):
        self.logger.info("***************************Test_003_DataCatalog*************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.clickNext()
        time.sleep(2)
        self.lp.setPassword(self.password)
        self.lp.clickPswdSignIn()
        time.sleep(2)
        self.lp.clickYes()
        time.sleep(2)
        self.driver.get("https://tiplatform-uat.azurewebsites.net/")
        time.sleep(10)
        self.lp.clickSignIn()
        time.sleep(15)
        self.lp.ClickSearch()
        self.logger.info("***************************Table Copy Validation *************************")
        # Copy
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@title='File2Table']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//img[@title='Copy']").click()
        time.sleep(2)
        self.DCP = DataCatalogPage(self.driver)
        self.DCP.setTableName("ABC")
        time.sleep(2)
        self.DCP.setSchemaName("Sandbox")
        time.sleep(2)
        self.DCP.ClickCopy()
        time.sleep(5)
        self.DCP.ClickFiles()
        time.sleep(5)
        self.DCP.ClickDatasets()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='ABC']")
        print(element.text)
        if element.text == "ABC":
            assert True
            self.driver.close()
            self.logger.info("***************************Table Copy Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_Table_Copy.png")
            self.driver.close()
            self.logger.error("***************************Table Copy Failed *************************")
            assert False

    def test_Table_Preview(self, setup):
        self.logger.info("***************************Test_003_DataCatalog*************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.clickNext()
        time.sleep(2)
        self.lp.setPassword(self.password)
        self.lp.clickPswdSignIn()
        time.sleep(2)
        self.lp.clickYes()
        time.sleep(2)
        self.driver.get("https://tiplatform-uat.azurewebsites.net/")
        time.sleep(10)
        self.lp.clickSignIn()
        time.sleep(15)
        self.lp.ClickSearch()
        self.logger.info("***************************Table Preview Validation *************************")
        # Copy
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@title='dfg']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//img[@title='View all']").click()
        time.sleep(2)
        self.logger.info("***************************Select Operator CONTAINS Validation *************************")
        DCP = DataCatalogPage(self.driver)
        DCP.setSelectOne("Loginemail")
        time.sleep(2)
        DCP.setSelectOperator("CONTAINS")
        time.sleep(5)
        DCP.setSearch("rachel@example.com")
        time.sleep(5)
        DCP.ClickSearchIcon()
        time.sleep(5)
        status = DCP.searchLoginEmail_Contains("rachel@example.com")
        assert True == status
        self.logger.info("***************************Select Operator CONTAINS PASSED *************************")
        self.driver.back()
        time.sleep(5)
        self.lp.ClickSearch()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@title='dfg']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//img[@title='View all']").click()
        time.sleep(2)
        self.logger.info("***************************Select Operator CONTAINS Validation *************************")
        DCP = DataCatalogPage(self.driver)
        DCP.setSelectOne("Loginemail")
        time.sleep(2)
        DCP.setSelectOperator("NOT CONTAINS")
        time.sleep(5)
        DCP.setSearch("rachel@example.com")
        time.sleep(5)
        DCP.ClickSearchIcon()
        time.sleep(5)

        element = self.driver.find_element_by_xpath("//td[contains(text(),'rachel@example.com')]")

        if element == True:
            print("Successfull")