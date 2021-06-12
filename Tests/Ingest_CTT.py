import time
import pytest
from selenium import webdriver


from Pages.IngestPage import IngestPage
from Pages.LoginPage import LoginPage
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig

class Test_002_Ingest:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_Ingest_ConvertToTable(self, setup):
        self.logger.info("***************************Test_002_Ingest*************************")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.clickNext()
        time.sleep(3)
        self.lp.setPassword(self.password)
        self.lp.clickPswdSignIn()
        time.sleep(3)
        self.lp.clickYes()
        time.sleep(3)
        self.driver.get("https://tiplatform-uat.azurewebsites.net/")
        time.sleep(5)
        self.lp.clickSignIn()
        time.sleep(15)
        self.lp.ClickSearch()
        self.logger.info("***************************Table Convertion Validation *************************")
        # selecting file from files module to convert into table
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[contains(text(),' Files ')]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//tbody[@role='rowgroup']//div[@title='marks_new']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//img[@title='Convert to table']").click()
        time.sleep(8)
        self.IG = IngestPage(self.driver)
        self.IG.setSchemaName("Sandbox")
        time.sleep(5)
        self.driver.find_element_by_id("tableName").send_keys("File2Table")
        time.sleep(2)
        self.IG.setLoadType("Complete Refresh")
        time.sleep(5)
        self.IG.clickReviewandConvert()
        self.logger.info("***************************ReviewandConvert Passed *************************")
        time.sleep(10)
        self.driver.find_element_by_xpath("//div[contains(text(),' Datasets ')]").click()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='File2Table']")
        print(element.text)
        if element.text == "File2Table":
            assert True
            self.driver.close()
            self.logger.info("***************************ConvertToTable Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_ConvertToTable.png")
            self.driver.close()
            self.logger.error("***************************ConvertToTable Failed *************************")
            assert False

    def test_Ingest_ConvertToTable_Existing(self, setup):
        self.logger.info("***************************Test_002_Ingest*************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.clickNext()
        time.sleep(3)
        self.lp.setPassword(self.password)
        self.lp.clickPswdSignIn()
        time.sleep(3)
        self.lp.clickYes()
        time.sleep(3)
        self.driver.get("https://tiplatform-uat.azurewebsites.net/")
        time.sleep(5)
        self.lp.clickSignIn()
        time.sleep(15)
        self.lp.ClickSearch()
        self.logger.info("***************************File Selecting for Covertion *************************")
        # selecting file from files module to convert into table
        time.sleep(8)
        self.driver.find_element_by_xpath("//div[contains(text(),' Files ')]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@title='marks_new']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//img[@title='Convert to table']").click()
        time.sleep(8)
        self.logger.info("***************************Existing Table Covertion Validation *************************")
        self.IG = IngestPage(self.driver)
        self.driver.find_element_by_xpath("//label[contains(text(),' Load to existing table ')]").click()
        time.sleep(3)
        self.IG.setSchemaName("Sandbox")
        time.sleep(2)
        self.IG.setTableName("FileToTable")
        time.sleep(5)
        self.IG.clickReviewandConvert()
        time.sleep(10)
        self.driver.find_element_by_xpath("//div[contains(text(),' Datasets ')]").click()
        time.sleep(5)

        element = self.driver.find_element_by_xpath("//div[@title='File2Table']")
        print(element.text)
        if element.text == "File2Table":
            assert True
            self.driver.close()
            self.logger.info("***************************ConvertToTable Ingest Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_ConvertToTable.png")
            self.driver.close()
            self.logger.error("***************************ConvertToTable Ingestion Failed *************************")
            assert False

    def test_Ingest_ConvertToTable_IncrementalLoad(self, setup):
        self.logger.info("***************************Test_002_Ingest*************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.clickNext()
        time.sleep(3)
        self.lp.setPassword(self.password)
        self.lp.clickPswdSignIn()
        time.sleep(3)
        self.lp.clickYes()
        time.sleep(3)
        self.driver.get("https://tiplatform-uat.azurewebsites.net/")
        time.sleep(5)
        self.lp.clickSignIn()
        time.sleep(15)
        self.lp.ClickSearch()
        self.logger.info("***************************ConvertToTable_IncrementalLoad Validation **********************")
        # selecting file from files module to convert into table
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[contains(text(),' Files ')]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@title='marks_new']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//img[@title='Convert to table']").click()
        time.sleep(8)
        self.IG = IngestPage(self.driver)
        self.IG.setSchemaName("Sandbox")
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@name='tableName']").send_keys("Incremental Load 20")
        time.sleep(2)
        self.IG.setLoadType("Incremental Load")
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/footer/div[2]/div/label").click();
        time.sleep(2)
        self.IG.clickReviewandConvert()
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/span")

        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div/table/thead/tr[1]/th[1]/div/div[1]/div[2]/label").click();
        time.sleep(2)
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div/table/thead/tr[1]/th[2]/div/div[1]/div[2]/label").click();
        time.sleep(2)
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div/table/thead/tr[1]/th[3]/div/div[1]/div[2]/label").click();
        time.sleep(2)
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div/table/thead/tr[1]/th[5]/div/div[1]/div[2]/label").click();
        time.sleep(5)
        self.IG.clickReviewandConvert()
        time.sleep(10)
        self.driver.find_element_by_xpath("//div[contains(text(),' Datasets ')]").click()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='Incremental Load 20']")
        print(element.text)
        if element.text == "Incremental Load 20":
            assert True
            self.driver.close()
            self.logger.info("***************************Incremental Load Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_IncrementalLoad.png")
            self.driver.close()
            self.logger.error("***************************Incremental Load Failed *************************")
            assert False

    def test_Ingest_SameTableName_Conversion(self, setup):
        self.logger.info("***************************Test_002_Ingest*************************")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.clickNext()
        time.sleep(3)
        self.lp.setPassword(self.password)
        self.lp.clickPswdSignIn()
        time.sleep(3)
        self.lp.clickYes()
        time.sleep(3)
        self.driver.get("https://tiplatform-uat.azurewebsites.net/")
        time.sleep(5)
        self.lp.clickSignIn()
        time.sleep(15)
        self.lp.ClickSearch()
        self.logger.info("***************************Table Convertion Validation *************************")
        # selecting file from files module to convert into table
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[contains(text(),' Files ')]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@title='marks_new']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//img[@title='Convert to table']").click()
        time.sleep(8)
        self.IG = IngestPage(self.driver)
        self.IG.setSchemaName("Sandbox")
        time.sleep(5)
        self.driver.find_element_by_id("tableName").send_keys("FileToTable")
        time.sleep(2)
        self.IG.setLoadType("Complete Refresh")
        time.sleep(5)
        self.IG.clickReviewandConvert()
        time.sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(),'Yes')]").click()
        self.logger.info("***************************ReviewandConvert Passed *************************")
        time.sleep(10)
        self.driver.find_element_by_xpath("//div[contains(text(),' Datasets ')]").click()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='FileToTable']")
        print(element.text)
        if element.text == "FileToTable":
            assert True
            self.driver.close()
            self.logger.info("***************************ConvertToTable Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_ConvertToTable.png")
            self.driver.close()
            self.logger.error("***************************ConvertToTable Failed *************************")
            assert False

    def test_Ingest_Datatype_Happypath(self, setup):
        self.logger.info("***************************Test_002_Ingest*************************")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.clickNext()
        time.sleep(3)
        self.lp.setPassword(self.password)
        self.lp.clickPswdSignIn()
        time.sleep(3)
        self.lp.clickYes()
        time.sleep(3)
        self.driver.get("https://tiplatform-uat.azurewebsites.net/")
        time.sleep(5)
        self.lp.clickSignIn()
        time.sleep(15)
        self.lp.ClickSearch()
        self.logger.info("***************************Table Convertion Validation *************************")
        # selecting file from files module to convert into table
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[contains(text(),' Files ')]").click()
        time.sleep(8)
        self.driver.find_element_by_xpath("//div[@title='DataType']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//img[@title='Convert to table']").click()
        time.sleep(20)
        self.IG = IngestPage(self.driver)
        self.IG.setDatatypenvarchar("nvarchar")
        time.sleep(2)
        self.IG.setDatatypeInt_decimal("decimal")
        time.sleep(2)

        self.IG.setDatatypeDateTime("nvarchar")
        time.sleep(5)
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div/table/thead/tr[1]/th[7]/div/div[1]/div[1]/label").click()
        time.sleep(2)
        self.IG.setSchemaName("Sandbox")
        time.sleep(5)
        self.driver.find_element_by_id("tableName").send_keys("DatatypeHappy")
        time.sleep(2)
        self.IG.setLoadType("Complete Refresh")
        time.sleep(5)
        self.IG.clickReviewandConvert()
        self.logger.info("***************************ReviewandConvert Passed *************************")
        time.sleep(10)
        self.driver.find_element_by_xpath("//div[contains(text(),' Datasets ')]").click()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='DatatypeHappy']")
        print(element.text)
        if element.text == "DatatypeHappy":
            assert True
            self.driver.close()
            self.logger.info("***************************Datatype Validations Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_Datatype Validations.png")
            self.driver.close()
            self.logger.error("***************************Datatype Validations Failed *************************")
            assert False

    def test_Ingest_Datatype_Alternate(self, setup):
        self.logger.info("***************************Test_002_Ingest*************************")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.clickNext()
        time.sleep(3)
        self.lp.setPassword(self.password)
        self.lp.clickPswdSignIn()
        time.sleep(3)
        self.lp.clickYes()
        time.sleep(3)
        self.driver.get("https://tiplatform-uat.azurewebsites.net/")
        time.sleep(5)
        self.lp.clickSignIn()
        time.sleep(15)
        self.lp.ClickSearch()
        self.logger.info("***************************Table Convertion Validation *************************")
        # selecting file from files module to convert into table
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[contains(text(),' Files ')]").click()
        time.sleep(8)
        self.driver.find_element_by_xpath("//div[@title='DataType']").click()
        time.sleep(2)
        time.sleep(2)
        self.driver.find_element_by_xpath("//img[@title='Convert to table']").click()
        time.sleep(25)
        self.IG = IngestPage(self.driver)
        time.sleep(10)
        self.IG.setDatatypenvarchar("int")
        time.sleep(2)
        self.IG.setDatatypeInt_decimal("datetime")
        time.sleep(2)
        self.IG.setDatatypeDateTime("bigint")
        time.sleep(5)
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div/table/thead/tr[1]/th[7]/div/div[1]/div[1]/label").click()
        time.sleep(2)
        self.IG.setSchemaName("Sandbox")
        time.sleep(5)
        self.driver.find_element_by_id("tableName").send_keys("DatatypeAlternate")
        time.sleep(2)
        self.IG.setLoadType("Complete Refresh")
        time.sleep(5)
        self.IG.clickReviewandConvert()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/footer/div[4]/div")
        print(element.text)
        time.sleep(5)
        self.IG.setDatatypenvarchar("nvarchar")
        time.sleep(2)
        self.IG.setDatatypeInt_decimal("decimal")
        time.sleep(2)

        self.IG.setDatatypeDateTime("nvarchar")
        time.sleep(5)
        self.IG.clickReviewandConvert()

        self.logger.info("***************************ReviewandConvert Passed *************************")
        time.sleep(10)
        self.driver.find_element_by_xpath("//div[contains(text(),' Datasets ')]").click()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='DatatypeAlternate']")
        print(element.text)
        if element.text == "DatatypeAlternate":
            assert True
            self.driver.close()
            self.logger.info("***************************Datatype Validations Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_Datatype Validations.png")
            self.driver.close()
            self.logger.error("***************************Datatype Validations Failed *************************")
            assert False

    def test_Ingest_Delete(self, setup):
        self.logger.info("***************************Test_002_Ingest*************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.clickNext()
        time.sleep(3)
        self.lp.setPassword(self.password)
        self.lp.clickPswdSignIn()
        time.sleep(3)
        self.lp.clickYes()
        time.sleep(3)
        self.driver.get("https://tiplatform-uat.azurewebsites.net/")
        time.sleep(5)
        self.lp.clickSignIn()
        time.sleep(15)
        self.lp.ClickSearch()
        self.logger.info("*************************** File Delete Validation *************************")
        # Delete
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[contains(text(),' Files ')]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@title='marks_new']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//img[@alt='Delete']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(),'Delete')]").click()
