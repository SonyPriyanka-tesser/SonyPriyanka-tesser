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
    server = ReadConfig.getServer()
    portnumber = ReadConfig.getPortNumber()
    Database = ReadConfig.getDatabases()
    user = ReadConfig.getUser()
    pwd = ReadConfig.getPass()

    logger = LogGen.loggen()

    def test_Ingest_CSV(self, setup):
        self.logger.info("***************************Test_002_Ingest*************************")
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
        self.logger.info("***************************CSV File Ingestion *************************")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.clickIngest()
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(
            "C:\\Users\\sonup\\PycharmProjects\\Project\\TestData\\marks_new.csv")
        time.sleep(2)
        self.IG.setDelimiter("Comma")
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(),'Ingest')]").click()
        time.sleep(5)
        self.logger.info("***************************CSV File Validation *************************")
        self.lp.clickDatsets()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[contains(text(),' Files ')]").click()
        time.sleep(2)
        element = self.driver.find_element_by_xpath("//div[contains(text(),'marks_new')]")
        print(element.text)
        if element.text == "marks_new":
            assert True
            self.driver.close()
            self.logger.info("***************************CSV File Ingest Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_CSV_File.png")
            self.driver.close()
            self.logger.error("***************************CSV File Ingestion Failed *************************")
            assert False

    def test_Ingest_TXT(self, setup):
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
        time.sleep(10)
        self.lp.clickSignIn()
        time.sleep(15)
        self.lp.ClickSearch()
        self.logger.info("***************************TXT File Ingest  *************************")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.clickIngest()
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(
            "C:\\Users\\sonup\\PycharmProjects\\Project\\TestData\\Test_Uat_Tab.txt")
        time.sleep(2)
        self.IG.setDelimiter("Tab")
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(),'Ingest')]").click()
        time.sleep(5)
        self.logger.info("***************************TXT File Validation *************************")
        self.lp.clickDatsets()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[contains(text(),' Files ')]").click()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[contains(text(),'Test_Uat_Tab')]")
        print(element.text)
        if element.text == "Test_Uat_Tab":
            assert True
            self.driver.close()
            self.logger.info("***************************TXT File Ingest Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_TXT_File.png")
            self.driver.close()
            self.logger.error("***************************TXT File Ingestion Failed *************************")
            assert False

    def test_Ingest_Existing(self, setup):
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
        time.sleep(10)
        self.lp.clickSignIn()
        time.sleep(15)
        self.lp.ClickSearch()
        self.logger.info("***************************Existing File Ingestion *************************")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.clickIngest()
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(
            "C:\\Users\\sonup\\PycharmProjects\\Project\\TestData\\marks_new.csv")
        time.sleep(3)
        self.IG.setDelimiter("Comma")
        time.sleep(3)

        self.driver.find_element_by_xpath("//button[contains(text(),'Ingest')]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/button").click()
        time.sleep(5)
        self.logger.info("***************************Existing File Validation *************************")
        self.driver.find_element_by_xpath("//div[contains(text(),' Files ')]").click()
        time.sleep(2)
        element = self.driver.find_element_by_xpath("//div[contains(text(),'marks_new')]")
        print(element.text)
        if element.text == "marks_new":
            assert True
            self.driver.close()
            self.logger.info("***************************Existing File Ingest Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_Existing_File.png")
            self.driver.close()
            self.logger.error("***************************Existing File Ingestion Failed *************************")
            assert False

    def test_Ingest_Filesize_Exceed(self, setup):
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
        time.sleep(10)
        self.lp.clickSignIn()
        time.sleep(15)
        self.lp.ClickSearch()
        self.logger.info("*************************** File Size Exceed Validation *************************")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.clickIngest()
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(
            "C:\\Users\\sonup\\PycharmProjects\\Project\\TestData\\SizeExceed.csv")
        time.sleep(2)
        # Validation of File exceed
        element = self.driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/span")
        print(element.text)
        if element.text == "The file size must not exceed 15MB and must be of one of the file extensions - csv,txt,xls,xlsx":
            assert True
            self.driver.close()
            self.logger.info("***************************File Exceed Passed *************************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_File_Exceed.png")
            self.driver.close()
            self.logger.error("***************************File ExceedFailed *************************")
            assert False

    def test_Ingest_PreviewAll(self, setup):
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
        self.logger.info("***************************File Preview Validation *************************")
        # file is present in datalake or not
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[contains(text(),' Files ')]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@title='marks_new']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//img[@title='View all']").click()
        time.sleep(5)
        # Validation Preview All
        # Analyze Path Validation
        element = self.driver.find_element_by_xpath("//div[@class='object-name d-inline-block']")
        print(element.text)
        if element.text == "marks_new":
            assert True
            self.driver.close()
            self.logger.info("***************************File Preview Passed *************************")

        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_File_Preiview.png")
            self.driver.close()
            self.logger.error("***************************File Preview Failed *************************")
            assert False

    def test_Ingest_Download(self, setup):
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
        self.logger.info("***************************File Download Validation *************************")
        # Download
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[contains(text(),' Files ')]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@title='marks_new']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//img[@title='Download']").click()
        time.sleep(5)
        # Validation Download
        element = self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/span")
        print(element.text)
        if element.text == "Downloaded Successfully":
            assert True
            self.driver.close()
            self.logger.info("***************************File Downloaded Successfully *************************")

        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_File_Download.png")
            self.driver.close()
            self.logger.error("***************************File Download is Failed *************************")
            assert False

    def test_Ingest_Copy(self, setup):
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
        self.logger.info("***************************File Copy Validation *************************")
        # Copy
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[contains(text(),' Files ')]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@title='marks_new']").click()
        time.sleep(5)

        self.driver.find_element_by_xpath("//img[@title='Copy']").click()
        time.sleep(2)
        self.driver.find_element_by_id("toFileName").send_keys("FileCopied")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),'Copy')]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[contains(text(),' Files ')]").click()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='FileCopied']")
        print(element.text)
        if element.text == "FileCopied":
            assert True
            self.driver.close()
            self.logger.info("***************************CSV File Ingest Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_CSV_Failed.png")
            self.driver.close()
            self.logger.error("***************************CSV File Ingestion Failed *************************")
            assert False

    def test_Ingest_Database1(self, setup):
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
        time.sleep(10)
        self.lp.clickSignIn()
        time.sleep(15)
        self.lp.ClickSearch()
        self.logger.info("***************************DataBase Validation *************************")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.clickIngest()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[contains(text(),'Databases ')]").click()
        # time.sleep(15)
        self.IG.setDatabases("Azure SQL Database")
        time.sleep(5)
        self.IG.setServer(self.server)
        time.sleep(2)
        self.IG.setPortNumber(self.portnumber)
        time.sleep(2)
        self.IG.setDatabaseName(self.Database)
        time.sleep(2)
        self.IG.setUser(self.user)
        time.sleep(2)
        self.IG.setPwd(self.pwd)
        time.sleep(2)
        self.IG.clickConnect()
        time.sleep(10)
        self.IG.setSourceSchema("IncorpTax")
        time.sleep(3)
        self.IG.setSourceTable("ti_dim_accountlets")
        time.sleep(3)
        self.IG.setTargetSchema("Sandbox")
        time.sleep(3)
        self.driver.find_element_by_id("target-table").send_keys("Accts")
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(),'Ingest')]").click()
        time.sleep(10)
        self.driver.find_element_by_xpath("//div[contains(text(),' Files ')]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[contains(text(),' Datasets ')]").click()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='Accts']")
        print(element.text)
        if element.text == "Accts":
            assert True
            self.driver.close()
            self.logger.info("***************************CSV File Ingest Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_CSV_Failed.png")
            self.driver.close()
            self.logger.error("***************************CSV File Ingestion Failed *************************")
            assert False

    def test_Ingest_Database_Existing(self, setup):
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
        time.sleep(10)
        self.lp.clickSignIn()
        time.sleep(15)
        self.lp.ClickSearch()
        self.logger.info("***************************DataBase Existing Validation *************************")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.clickIngest()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[contains(text(),'Databases ')]").click()
        # time.sleep(15)
        self.IG.setDatabases("Azure SQL Database")
        time.sleep(5)
        self.IG.setServer(self.server)
        time.sleep(2)
        self.IG.setPortNumber(self.portnumber)
        time.sleep(2)
        self.IG.setDatabaseName(self.Database)
        time.sleep(2)
        self.IG.setUser(self.user)
        time.sleep(2)
        self.IG.setPwd(self.pwd)
        time.sleep(2)
        self.IG.clickConnect()
        time.sleep(8)
        self.IG.setSourceSchema("IncorpTax")
        time.sleep(3)
        self.IG.setSourceTable("ti_dim_accountlets")
        time.sleep(3)
        self.IG.setTargetSchema("Sandbox")
        time.sleep(3)
        self.driver.find_element_by_id("target-table").send_keys("Accts")
        time.sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(),'Ingest')]").click()
        time.sleep(10)
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div/div/div/div/div/div/span/form/div/div[2]/div/div[4]/div[2]/button").click()
        time.sleep(10)
        self.driver.find_element_by_xpath("//div[contains(text(),' Files ')]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[contains(text(),' Datasets ')]").click()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='Accts']")
        print(element.text)
        if element.text == "Accts":
            assert True
            self.driver.close()
            self.logger.info("***************************CSV File Ingest Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_CSV_Failed.png")
            self.driver.close()
            self.logger.error("***************************CSV File Ingestion Failed *************************")
            assert False

    def test_Ingest_MultipleFiles(self, setup):
        self.logger.info("***************************Test_002_Ingest*************************")
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
        time.sleep(10)
        self.lp.ClickSearch()
        self.logger.info("***************************CSV File Ingestion *************************")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.clickIngest()
        time.sleep(5)
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(
            "C:\\Users\\sonup\\PycharmProjects\\Project\\TestData\\marks_new.csv")

        time.sleep(3)
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(
            "C:\\Users\\sonup\\PycharmProjects\\Project\\TestData\\Students-Pipe.txt")
        time.sleep(3)
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(
            "C:\\Users\\sonup\\PycharmProjects\\Project\\TestData\\Students-Comma.csv")
        self.IG.setDelimiter("Comma")
        time.sleep(3)
        self.IG.setDelimiter1("Comma")
        time.sleep(5)
        self.IG.setDelimiter2("Comma")
        time.sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(),'Ingest')]").click()
        time.sleep(10)
        self.driver.find_element_by_xpath("//button[contains(text(),'Yes')]").click();

        self.logger.info("***************************Multiple Files Ingestion Validation*************************")
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[contains(text(),' Files ')]").click()
        time.sleep(2)
        element = self.driver.find_element_by_xpath("//div[@title='marks_new']")
        print(element.text)
        if element.text == "marks_new":
            assert True
            self.driver.close()
            self.logger.info("***************************Multiple Files Ingest Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_CSV_Failed.png")
            self.driver.close()
            self.logger.error("***************************Multiple Files Ingestion Failed *************************")
            assert False

    def test_UnSupportedFiles(self, setup):
        self.logger.info("***************************Test_002_Ingest*************************")
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
        time.sleep(5)
        self.lp.clickSignIn()
        time.sleep(15)
        self.lp.ClickSearch()
        self.logger.info("***************************CSV File Ingestion *************************")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.clickIngest()
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(
            "C:\\Users\\sonup\\PycharmProjects\\Project\\TestData\\marks_new (4).CSV")
        time.sleep(2)
        self.IG.setDelimiter("Comma")
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(),'Ingest')]").click()
        time.sleep(10)
        self.logger.info(
            "***************************File name should not contain special charecters Validation*************************")

        element = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/div[2]/div")

        print(element.text)

        if element.text == "Filename contains special characters ()":
            assert True
            self.driver.close()
            self.logger.info("***************************Unsupported file Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_UnsupportedFile.png")
            self.driver.close()
            self.logger.error("***************************Unsupported File Ingestion Failed *************************")
            assert False
