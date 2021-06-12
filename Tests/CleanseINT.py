import time
import pytest
from selenium import webdriver

from Pages.CleansePage import CleansePage
from Pages.IngestPage import IngestPage
from Pages.LoginPage import LoginPage
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig


class Test_004_CleanseINTColumn:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_Cleanse_ArithmaticAdd(self, setup):
        self.logger.info("***************************Test_004_CleanseINTColumn*************************")
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
        self.logger.info("***************************Cleanse Function*************************")
        time.sleep(8)
        self.cp = CleansePage(self.driver)
        self.cp.setSearch("Cleansed")
        self.cp.clickSearch()
        assert True
        time.sleep(5)
        self.cp.clickCleanse()
        time.sleep(5)

        self.logger.info("***************************Cleanse Arithmatic Function *************************")

        self.cp.clickAddColumn()
        time.sleep(5)
        self.cp.setSearchColumn("Prepexam1")
        time.sleep(5)
        self.cp.clickPrepexam1()
        self.cp.clickAdd()
        time.sleep(5)
        self.cp.clickAddfunction()
        time.sleep(5)
        self.cp.clickArithmatic()
        time.sleep(5)
        self.logger.info("***************************Cleanse Arithmatic Addition *************************")

        self.cp.clickOperator()
        time.sleep(5)
        # ADD
        self.cp.clickADD()
        time.sleep(5)
        self.driver.find_element_by_id("mathOperatorValue").send_keys("5")
        time.sleep(5)
        self.cp.clickUpdate()
        time.sleep(10)
        self.cp.clickPreviewicon()
        time.sleep(10)
        self.logger.info("***************************Cleanse Arithmatic Addition Validation *************************")

        table = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody")
        TotalRows = table.find_elements_by_tag_name("tr")

        rowCount = len(TotalRows)
        print(rowCount)
        print("Before" + "  " + "After")
        for r in range(1, rowCount + 1):
            table = self.driver.find_element_by_xpath("//table[@role='table']")

            a = int(table.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[1]").text)
            num = 5
            after = a + num
            print(a, "    ", after)
            b = int(table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[2]").text)
            if after == b:
                assert True
                self.logger.info(
                    "***************************Cleanse Arithmatic Addition Passed *************************")
            else:

                self.driver.save_screenshot(".\\Screenshots\\" + "test_Cleanse Arithmatic Addition.png")
                self.logger.error(
                    "***************************Cleanse Arithmatic Addition Failed *************************")
                assert False
        time.sleep(5)
        self.cp.clickPreviewclose()

        # FormQuery
        self.logger.info("***********************FormQuery Function Copy****************")

        self.cp.clickFormQuery()
        time.sleep(5)
        self.cp.clickCopyFormQuery()
        time.sleep(2)
        self.cp.clickCloseFormQuery()
        time.sleep(5)

        self.logger.info("***********************FormQuery Validation****************")

        # Cleanse

        self.logger.info("***********************Cleanse Function ****************")

        self.driver.find_element_by_id("cleanseName").send_keys("CleanseADD")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.setSchemaName("Sandbox")
        time.sleep(2)
        self.driver.find_element_by_id("outputName").send_keys("ADDCleanse")
        self.IG.setLoadType("Complete Refresh")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),' Cleanse ')]").click()
        time.sleep(5)

        self.logger.info("***************************Arithmatic Cleanse Validation *************************")

        self.lp.clickDatsets()
        time.sleep(5)
        self.lp.clickPrepared()
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='ADDCleanse']")
        print(element.text)
        if element.text == "ADDCleanse":
            assert True
            self.driver.close()
            self.logger.info("***************************Arithmatic Cleanse Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_Arithmatic Cleanse.png")
            self.driver.close()
            self.logger.error("**************************Arithmatic Cleanse Failed *************************")
            assert False

    def test_Cleanse_ArithmaticSub(self, setup):
        self.logger.info("***************************Test_004_CleanseINTColumn*************************")
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
        self.logger.info("***************************Cleanse Function*************************")
        time.sleep(8)
        self.cp = CleansePage(self.driver)
        self.cp.setSearch("Cleansed")
        self.cp.clickSearch()
        assert True
        time.sleep(5)
        self.cp.clickCleanse()
        time.sleep(5)
        self.logger.info("***************************Cleanse Arithmatic Function *************************")

        self.cp.clickAddColumn()
        time.sleep(5)
        self.cp.setSearchColumn("Prepexam1")
        time.sleep(5)
        self.cp.clickPrepexam1()
        self.cp.clickAdd()
        time.sleep(5)
        self.cp.clickAddfunction()
        time.sleep(5)
        self.cp.clickArithmatic()
        time.sleep(5)

        self.logger.info("***************************Cleanse Arithmatic Subtraction *************************")
        # Subtraction
        self.cp.clickOperator()
        time.sleep(5)
        self.driver.find_element_by_xpath("//img[@alt='subtract']").click()
        time.sleep(5)
        self.driver.find_element_by_id("mathOperatorValue").clear()
        self.driver.find_element_by_id("mathOperatorValue").send_keys("3")
        time.sleep(5)
        self.cp.clickUpdate()
        time.sleep(5)
        self.cp.clickPreviewicon()
        time.sleep(5)
        self.logger.info(
            "***************************Cleanse Arithmatic Subtraction  Validation*************************")
        table = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody")
        TotalRows = table.find_elements_by_tag_name("tr")

        rowCount = len(TotalRows)
        print(rowCount)
        print("Before" + "  " + "After")
        for r in range(1, rowCount + 1):
            table = self.driver.find_element_by_xpath("//table[@role='table']")

            a = int(table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[1]").text)
            # print(a)
            num = 3
            after = a - num
            # print(after,end="         ")
            print(a, "    ", after)
            b = int(table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[2]").text)
            if after == b:
                assert True
                self.logger.info(
                    "***************************Cleanse Arithmatic Subtraction Passed *************************")
            else:

                self.driver.save_screenshot(".\\Screenshots\\" + "test_Cleanse Arithmatic Subtraction.png")
                self.logger.error(
                    "***************************Cleanse Arithmatic Subtraction Failed *************************")
                assert False

        time.sleep(5)
        self.cp.clickPreviewclose()

        # FormQuery
        self.logger.info("***********************FormQuery Function Copy****************")

        self.cp.clickFormQuery()
        time.sleep(5)
        self.cp.clickCopyFormQuery()
        time.sleep(2)
        self.cp.clickCloseFormQuery()
        time.sleep(5)

        self.logger.info("***********************FormQuery Validation****************")

        # Cleanse

        self.logger.info("***********************Cleanse Function ****************")

        self.driver.find_element_by_id("cleanseName").send_keys("CleanseSUB")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.setSchemaName("Sandbox")
        time.sleep(2)
        self.driver.find_element_by_id("outputName").send_keys("SUBCleanse")
        self.IG.setLoadType("Complete Refresh")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),' Cleanse ')]").click()
        time.sleep(5)

        self.logger.info("***************************Arithmatic Cleanse Validation *************************")

        self.lp.clickDatsets()
        time.sleep(5)
        self.lp.clickPrepared()
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='SUBCleanse']")
        print(element.text)
        if element.text == "SUBCleanse":
            assert True
            self.driver.close()
            self.logger.info("***************************SUB Arithmatic Cleanse Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_SUB Arithmatic Cleanse.png")
            self.driver.close()
            self.logger.error("**************************SUB Arithmatic Cleanse Failed *************************")
            assert False

    def test_Cleanse_ArithmaticMul(self, setup):
        self.logger.info("***************************Test_004_CleanseINTColumn*************************")
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
        self.logger.info("***************************Cleanse Function*************************")
        time.sleep(8)
        self.cp = CleansePage(self.driver)
        self.cp.setSearch("Cleansed")
        self.cp.clickSearch()
        assert True
        time.sleep(5)
        self.cp.clickCleanse()
        time.sleep(5)
        self.logger.info("***************************Cleanse Arithmatic Function *************************")

        self.cp.clickAddColumn()
        time.sleep(5)
        self.cp.setSearchColumn("Prepexam1")
        time.sleep(5)
        self.cp.clickPrepexam1()
        self.cp.clickAdd()
        time.sleep(5)
        self.cp.clickAddfunction()
        time.sleep(5)
        self.cp.clickArithmatic()
        time.sleep(5)

        self.logger.info("***************************Cleanse Arithmatic Multiply *************************")
        self.cp.clickOperator()
        time.sleep(5)
        self.driver.find_element_by_xpath("//img[@alt='multiply']").click()
        time.sleep(5)
        self.driver.find_element_by_id("mathOperatorValue").clear()
        self.driver.find_element_by_id("mathOperatorValue").send_keys("2")
        time.sleep(5)
        self.cp.clickUpdate()
        time.sleep(5)
        self.cp.clickPreviewicon()
        time.sleep(5)
        self.logger.info(
            "***************************Cleanse Arithmatic Multiplication Validation *************************")
        table = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody")
        TotalRows = table.find_elements_by_tag_name("tr")

        rowCount = len(TotalRows)
        print(rowCount)
        print("Before" + "  " + "After")
        for r in range(1, rowCount + 1):
            table = self.driver.find_element_by_xpath("//table[@role='table']")

            a = int(table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[1]").text)
            # print(a)
            num = 2
            after = a * num
            # print(after,end="         ")
            print(a, "    ", after)
            b = int(table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[2]").text)
            if after == b:
                assert True
                self.logger.info(
                    "***************************Cleanse Arithmatic Multiplication Passed *************************")
            else:

                self.driver.save_screenshot(".\\Screenshots\\" + "test_Cleanse Arithmatic Multiplication.png")
                self.logger.error(
                    "***************************Cleanse Arithmatic Multiplication Failed *************************")
                assert False

        time.sleep(5)
        self.cp.clickPreviewclose()
        # FormQuery
        self.logger.info("***********************FormQuery Function Copy****************")

        self.cp.clickFormQuery()
        time.sleep(5)
        self.cp.clickCopyFormQuery()
        time.sleep(2)
        self.cp.clickCloseFormQuery()
        time.sleep(5)

        self.logger.info("***********************FormQuery Validation****************")

        # Cleanse

        self.logger.info("***********************Cleanse Function ****************")

        self.driver.find_element_by_id("cleanseName").send_keys("CleanseMUL")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.setSchemaName("Sandbox")
        time.sleep(2)
        self.driver.find_element_by_id("outputName").send_keys("MULCleanse")
        self.IG.setLoadType("Complete Refresh")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),' Cleanse ')]").click()
        time.sleep(5)

        self.logger.info("***************************Arithmatic Cleanse Validation *************************")

        self.lp.clickDatsets()
        time.sleep(5)
        self.lp.clickPrepared()
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='MULCleanse']")
        print(element.text)
        if element.text == "MULCleanse":
            assert True
            self.driver.close()
            self.logger.info("***************************MUL Arithmatic Cleanse Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_MUL Arithmatic Cleanse.png")
            self.driver.close()
            self.logger.error("**************************Arithmatic MUL Cleanse Failed *************************")
            assert False

    def test_Cleanse_ArithmaticDiv(self, setup):
        self.logger.info("***************************Test_004_CleanseINTColumn*************************")
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
        self.logger.info("***************************Cleanse Function*************************")
        time.sleep(8)
        self.cp = CleansePage(self.driver)
        self.cp.setSearch("Cleansed")
        self.cp.clickSearch()
        assert True
        time.sleep(5)
        self.cp.clickCleanse()
        time.sleep(5)
        self.logger.info("***************************Cleanse Arithmatic Function *************************")

        self.cp.clickAddColumn()
        time.sleep(5)
        self.cp.setSearchColumn("Prepexam1")
        time.sleep(5)
        self.cp.clickPrepexam1()
        self.cp.clickAdd()
        time.sleep(5)
        self.cp.clickAddfunction()
        time.sleep(5)
        self.cp.clickArithmatic()
        time.sleep(5)

        self.logger.info("***************************Cleanse Arithmatic Divide *************************")
        self.cp.clickOperator()
        time.sleep(5)
        self.driver.find_element_by_xpath("//img[@alt='divide']").click()
        time.sleep(5)
        self.driver.find_element_by_id("mathOperatorValue").clear()
        self.driver.find_element_by_id("mathOperatorValue").send_keys("3")
        time.sleep(5)
        self.cp.clickUpdate()
        time.sleep(5)
        self.cp.clickPreviewicon()
        time.sleep(5)
        self.logger.info("***************************Cleanse Arithmatic Division Validation*************************")
        table = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody")
        TotalRows = table.find_elements_by_tag_name("tr")

        rowCount = len(TotalRows)
        print(rowCount)
        print("Before" + "  " + "After")
        for r in range(1, rowCount + 1):
            table = self.driver.find_element_by_xpath("//table[@role='table']")

            a = int(table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[1]").text)
            # print(a)
            num = 3
            after = int(a / num)
            # print(after,end="         ")
            print(a, "    ", after)
            b = int(table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[2]").text)
            if after == b:
                assert True
                self.logger.info(
                    "***************************Cleanse Arithmatic Division Passed *************************")
            else:

                self.driver.save_screenshot(".\\Screenshots\\" + "test_Cleanse Arithmatic Division.png")
                self.logger.error(
                    "***************************Cleanse Arithmatic Division Failed *************************")
                assert False
        time.sleep(5)
        self.cp.clickPreviewclose()
        # FormQuery
        self.logger.info("***********************FormQuery Function Copy****************")

        self.cp.clickFormQuery()
        time.sleep(5)
        self.cp.clickCopyFormQuery()
        time.sleep(2)
        self.cp.clickCloseFormQuery()
        time.sleep(5)

        self.logger.info("***********************FormQuery Validation****************")

        # Cleanse

        self.logger.info("***********************Cleanse Function ****************")

        self.driver.find_element_by_id("cleanseName").send_keys("CleanseDIV")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.setSchemaName("Sandbox")
        time.sleep(2)
        self.driver.find_element_by_id("outputName").send_keys("DIVCleanse")
        self.IG.setLoadType("Complete Refresh")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),' Cleanse ')]").click()
        time.sleep(5)

        self.logger.info("***************************Arithmatic Cleanse Validation *************************")

        self.lp.clickDatsets()
        time.sleep(5)
        self.lp.clickPrepared()
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='DIVCleanse']")
        print(element.text)
        if element.text == "DIVCleanse":
            assert True
            self.driver.close()
            self.logger.info("***************************Div Arithmatic Cleanse Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_Div Arithmatic Cleanse.png")
            self.driver.close()
            self.logger.error("**************************Arithmatic Div Cleanse Failed *************************")
            assert False


    def test_Cleanse_ArithmaticMod(self, setup):
        self.logger.info("***************************Test_004_CleanseINTCOlumn*************************")
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
        self.logger.info("***************************Cleanse Function*************************")
        time.sleep(8)
        self.cp = CleansePage(self.driver)
        self.cp.setSearch("Cleansed")
        self.cp.clickSearch()
        assert True
        time.sleep(5)
        self.cp.clickCleanse()
        time.sleep(5)
        self.logger.info("***************************Cleanse Arithmatic Function *************************")

        self.cp.clickAddColumn()
        time.sleep(5)
        self.cp.setSearchColumn("Prepexam1")
        time.sleep(5)
        self.cp.clickPrepexam1()
        self.cp.clickAdd()
        time.sleep(5)
        self.cp.clickAddfunction()
        time.sleep(5)
        self.cp.clickArithmatic()
        time.sleep(5)

        self.logger.info("***************************Cleanse Arithmatic Modulus *************************")
        self.cp.clickOperator()
        time.sleep(5)
        self.driver.find_element_by_xpath("//img[@alt='modulus']").click()
        time.sleep(5)
        self.driver.find_element_by_id("mathOperatorValue").clear()
        self.driver.find_element_by_id("mathOperatorValue").send_keys("2")
        time.sleep(5)
        self.cp.clickUpdate()
        time.sleep(5)
        self.cp.clickPreviewicon()
        time.sleep(5)

        self.logger.info("***************************Cleanse Arithmatic Modulus Validation *************************")
        table = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody")
        TotalRows = table.find_elements_by_tag_name("tr")

        rowCount = len(TotalRows)
        print(rowCount)
        print("Before" + "  " + "After")
        for r in range(1, rowCount + 1):
            table = self.driver.find_element_by_xpath("//table[@role='table']")

            a = int(table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[1]").text)
            # print(a)
            num = 2
            after = int(a % num)

            # print(after,end="         ")
            print(a, "    ", after)
            b = int(table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[2]").text)
            if after == b:
                assert True
                self.logger.info(
                    "***************************Cleanse Arithmatic Modulus Passed *************************")
            else:

                self.driver.save_screenshot(".\\Screenshots\\" + "test_Cleanse Arithmatic Modulus.png")
                self.logger.error(
                    "***************************Cleanse Arithmatic Modulus Failed *************************")
                assert False

        time.sleep(5)
        self.cp.clickPreviewclose()
        # FormQuery
        self.logger.info("***********************FormQuery Function Copy****************")

        self.cp.clickFormQuery()
        time.sleep(5)
        self.cp.clickCopyFormQuery()
        time.sleep(2)
        self.cp.clickCloseFormQuery()
        time.sleep(5)

        self.logger.info("***********************FormQuery Validation****************")

        # Cleanse

        self.logger.info("***********************Cleanse Function ****************")

        self.driver.find_element_by_id("cleanseName").send_keys("CleanseMOD")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.setSchemaName("Sandbox")
        time.sleep(2)
        self.driver.find_element_by_id("outputName").send_keys("MODCleanse")
        self.IG.setLoadType("Complete Refresh")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),' Cleanse ')]").click()
        time.sleep(5)

        self.logger.info("***************************Arithmatic Cleanse Validation *************************")

        self.lp.clickDatsets()
        time.sleep(5)
        self.lp.clickPrepared()
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='MODCleanse']")
        print(element.text)
        if element.text == "MODCleanse":
            assert True
            self.driver.close()
            self.logger.info("***************************Mod Arithmatic Cleanse Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_Mod Arithmatic Cleanse.png")
            self.driver.close()
            self.logger.error("**************************Arithmatic Mod Cleanse Failed *************************")
            assert False
    def test_Cleanse_Concat(self, setup):
        self.logger.info("***************************Test_004_CleanseINTColumn*************************")
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
        self.logger.info("***************************Cleanse Function*************************")
        time.sleep(8)
        self.cp = CleansePage(self.driver)
        self.cp.setSearch("Cleansed")
        self.cp.clickSearch()
        assert True
        time.sleep(5)
        self.cp.clickCleanse()
        time.sleep(5)

        self.cp.clickAddColumn()
        time.sleep(5)
        self.cp.setSearchColumn("Prepexam1")
        time.sleep(5)
        self.cp.clickPrepexam1()
        self.cp.clickAdd()
        time.sleep(5)
        self.cp.clickAddfunction()
        time.sleep(5)
        self.logger.info("***************************Cleanse CONCAT Function *************************")
        self.driver.find_element_by_xpath("//img[@alt='CONCAT']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/img").click()
        time.sleep(5)
        self.driver.find_element_by_id("concatValue").send_keys("Concat")
        time.sleep(5)
        self.cp.clickUpdate()
        time.sleep(5)
        self.cp.clickPreviewicon()
        time.sleep(5)
        time.sleep(5)
        self.logger.info("***************************Cleanse ConCat Validation*************************")
        table = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody")
        TotalRows = table.find_elements_by_tag_name("tr")

        rowCount = len(TotalRows)
        print(rowCount)
        print("Before" + "  " + "After")
        for r in range(1, rowCount + 1):
            table = self.driver.find_element_by_xpath("//table[@role='table']")

            a = table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[1]").text
            value = "Concat"
            after = a + value
            # print(after,end="         ")
            print(a, "    ", after)
            b = table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[2]").text
            if after == b:
                assert True
                self.logger.info(
                    "***************************Cleanse Concat Passed *************************")
            else:

                self.driver.save_screenshot(".\\Screenshots\\" + "test_Cleanse Concat.png")
                self.logger.error(
                    "***************************Cleanse Concat Failed *************************")
                assert False

        self.cp.clickPreviewclose()
        time.sleep(5)

        # FormQuery
        self.logger.info("***********************FormQuery Function Copy****************")

        self.cp.clickFormQuery()
        time.sleep(5)
        self.cp.clickCopyFormQuery()
        time.sleep(2)
        self.cp.clickCloseFormQuery()
        time.sleep(5)

        self.logger.info("***********************FormQuery Validation****************")

        # Cleanse

        self.logger.info("***********************Cleanse Function ****************")

        self.driver.find_element_by_id("cleanseName").send_keys("ConcatCleanse")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.setSchemaName("Sandbox")
        time.sleep(2)
        self.driver.find_element_by_id("outputName").send_keys("CleanseConcat")
        self.IG.setLoadType("Complete Refresh")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),' Cleanse ')]").click()
        time.sleep(5)
        self.logger.info("***************************Concat Cleanse Validation *************************")
        self.lp.clickDatsets()
        time.sleep(5)
        self.lp.clickPrepared()
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='CleanseConcat']")
        print(element.text)
        if element.text == "CleanseConcat":
            assert True
            self.driver.close()
            self.logger.info("***************************Concat Cleanse Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_Concat Cleanse.png")
            self.driver.close()
            self.logger.error("**************************Concat Cleanse Failed *************************")
            assert False

    def test_Cleanse_ConvertBIGINT(self, setup):
        self.logger.info("***************************Test_004_CleanseINTColumn*************************")
        self.driver = setup
        self.driver.get(self.

                        baseURL)
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
        self.logger.info("***************************Cleanse Function*************************")
        time.sleep(8)
        self.cp = CleansePage(self.driver)
        self.cp.setSearch("Cleansed")
        self.cp.clickSearch()
        assert True
        time.sleep(5)
        self.cp.clickCleanse()
        time.sleep(5)
        self.logger.info("***************************Cleanse CONVERT *************************")

        self.cp.clickAddColumn()
        time.sleep(5)
        self.cp.setSearchColumn("Prepexam1")
        time.sleep(5)
        self.cp.clickPrepexam1()
        self.cp.clickAdd()
        time.sleep(5)
        self.cp.clickAddfunction()
        time.sleep(5)
        self.cp.clickConvert()
        time.sleep(5)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/img").click()
        time.sleep(5)

        self.logger.info("***********************Cleanse Convert BIGINT Function****************")
        self.cp.setDatatype("BIGINT")
        time.sleep(5)
        self.cp.clickUpdate()
        time.sleep(5)
        self.cp.clickPreviewicon()
        time.sleep(10)

        self.logger.info("***************************Cleanse BIGINT  Validation *************************")
        table = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody")
        TotalRows = table.find_elements_by_tag_name("tr")

        rowCount = len(TotalRows)
        print(rowCount)
        print("Before" + "  " + "After")
        for r in range(1, rowCount + 1):
            table = self.driver.find_element_by_xpath("//table[@role='table']")

            a = int(table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[1]").text)
            after = int(float(a))
            print(a, "    ", after)
            b = int(table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[2]").text)

            if after == b:
                assert True
                self.logger.info(
                    "***************************BIGINT Passed *************************")
            else:

                self.driver.save_screenshot(".\\Screenshots\\" + "test_BIGINT.png")
                self.logger.error(
                    "***************************BIGINT Convert Failed *************************")
                assert False

        self.cp.clickPreviewclose()
        time.sleep(5)

        # FormQuery
        self.logger.info("***********************FormQuery Function Copy****************")

        self.cp.clickFormQuery()
        time.sleep(5)
        self.cp.clickCopyFormQuery()
        time.sleep(2)
        self.cp.clickCloseFormQuery()
        time.sleep(5)

        self.logger.info("***********************FormQuery Validation****************")

        # Cleanse

        self.logger.info("***********************Cleanse Convert Function ****************")

        self.driver.find_element_by_id("cleanseName").send_keys("CleanseBIGINT")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.setSchemaName("Sandbox")
        time.sleep(2)
        self.driver.find_element_by_id("outputName").send_keys("BIGINTCleanse")
        self.IG.setLoadType("Complete Refresh")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),' Cleanse ')]").click()
        time.sleep(5)

        self.logger.info("***************************Convert Cleanse Validation *************************")

        self.lp.clickDatsets()
        time.sleep(5)
        self.lp.clickPrepared()
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='BIGINTCleanse']")
        print(element.text)
        if element.text == "BIGINTCleanse":
            assert True
            self.driver.close()
            self.logger.info("***************************Convert BIGINT Cleanse Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_ConvertBIGINT Cleanse.png")
            self.driver.close()
            self.logger.error("**************************Convert BIGINT Cleanse Failed *************************")
            assert False






    def test_Cleanse_ConvertBIT(self, setup):
        self.logger.info("***************************Test_004_CleanseINTColumn*************************")
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
        self.logger.info("***************************Cleanse Function*************************")
        time.sleep(8)
        self.cp = CleansePage(self.driver)
        self.cp.setSearch("Cleansed")
        self.cp.clickSearch()
        assert True
        time.sleep(5)
        self.cp.clickCleanse()
        time.sleep(5)
        self.logger.info("***************************Cleanse CONVERT *************************")

        self.cp.clickAddColumn()
        time.sleep(5)
        self.cp.setSearchColumn("Prepexam1")
        time.sleep(5)
        self.cp.clickPrepexam1()
        self.cp.clickAdd()
        time.sleep(5)
        self.cp.clickAddfunction()
        time.sleep(5)
        self.cp.clickConvert()
        time.sleep(5)
        self.logger.info("***********************Cleanse Convert BIT Function****************")
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/img").click()
        time.sleep(5)
        self.cp.setDatatype("BIT")
        time.sleep(5)
        self.cp.clickUpdate()
        time.sleep(5)
        self.cp.clickPreviewicon()
        time.sleep(5)


        self.logger.info("***************************Cleanse BIT  Validation *************************")
        table = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody")
        TotalRows = table.find_elements_by_tag_name("tr")

        rowCount = len(TotalRows)
        print(rowCount)
        print("Before" + "  " + "After")
        for r in range(1, rowCount + 1):
            table = self.driver.find_element_by_xpath("//table[@role='table']")

            a = int(table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[1]").text)
            after=int(bool(a))
            print(a, "    ", after)
            b = int(table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[2]").text)

            if after == b:
                assert True
                self.logger.info(
                    "***************************BIT Passed *************************")
            else:

                self.driver.save_screenshot(".\\Screenshots\\" + "test_BIT.png")
                self.logger.error(
                    "***************************BIT Convert Failed *************************")
                assert False

        self.cp.clickPreviewclose()
        time.sleep(5)

        # FormQuery
        self.logger.info("***********************FormQuery Function Copy****************")

        self.cp.clickFormQuery()
        time.sleep(5)
        self.cp.clickCopyFormQuery()
        time.sleep(2)
        self.cp.clickCloseFormQuery()
        time.sleep(5)

        self.logger.info("***********************FormQuery Validation****************")

        # Cleanse

        self.logger.info("***********************Cleanse Convert Function ****************")

        self.driver.find_element_by_id("cleanseName").send_keys("CleanseBIT")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.setSchemaName("Sandbox")
        time.sleep(2)
        self.driver.find_element_by_id("outputName").send_keys("BITCleanse")
        self.IG.setLoadType("Complete Refresh")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),' Cleanse ')]").click()
        time.sleep(5)

        self.logger.info("***************************Convert Cleanse Validation *************************")

        self.lp.clickDatsets()
        time.sleep(5)
        self.lp.clickPrepared()
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='BITCleanse']")
        print(element.text)
        if element.text == "BITCleanse":
            assert True
            self.driver.close()
            self.logger.info("***************************Convert BIT Cleanse Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_ConvertBIT Cleanse.png")
            self.driver.close()
            self.logger.error("**************************Convert BIT Cleanse Failed *************************")
            assert False

    def test_Cleanse_ConvertNVARCHAR(self, setup):
        self.logger.info("***************************Test_004_CleanseINTColumn*************************")
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
        self.logger.info("***************************Cleanse Function*************************")
        time.sleep(8)
        self.cp = CleansePage(self.driver)
        self.cp.setSearch("Cleansed")
        self.cp.clickSearch()
        assert True
        time.sleep(5)
        self.cp.clickCleanse()
        time.sleep(5)
        self.logger.info("***************************Cleanse CONVERT *************************")

        self.cp.clickAddColumn()
        time.sleep(5)
        self.cp.setSearchColumn("Prepexam1")
        time.sleep(5)
        self.cp.clickPrepexam1()
        self.cp.clickAdd()
        time.sleep(5)
        self.cp.clickAddfunction()
        time.sleep(5)
        self.cp.clickConvert()
        time.sleep(5)
        self.logger.info("***********************Cleanse Convert NVARCHAR Function****************")
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/img").click()
        time.sleep(5)
        self.cp.setDatatype("NVARCHAR")
        time.sleep(5)
        self.cp.clickUpdate()
        time.sleep(5)
        self.cp.clickPreviewicon()
        time.sleep(5)
        self.logger.info("***************************Cleanse NVARCHAR  Validation *************************")
        table = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody")
        TotalRows = table.find_elements_by_tag_name("tr")

        rowCount = len(TotalRows)
        print(rowCount)
        print("Before" + "  " + "After")
        for r in range(1, rowCount + 1):
            table = self.driver.find_element_by_xpath("//table[@role='table']")

            a = int(table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[1]").text)
            after = str(a)
            print(a, "    ", after)
            b = table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[2]").text

            if after == b:
                assert True
                self.logger.info(
                    "***************************NVARCHAR Passed *************************")
            else:

                self.driver.save_screenshot(".\\Screenshots\\" + "test_NVARCHAR.png")
                self.logger.error(
                    "***************************NVARCHAR Convert Failed *************************")
                assert False

        self.cp.clickPreviewclose()
        time.sleep(5)

        # FormQuery
        self.logger.info("***********************FormQuery Function Copy****************")

        self.cp.clickFormQuery()
        time.sleep(5)
        self.cp.clickCopyFormQuery()
        time.sleep(2)
        self.cp.clickCloseFormQuery()
        time.sleep(5)

        self.logger.info("***********************FormQuery Validation****************")

        # Cleanse

        self.logger.info("***********************Cleanse Convert Function ****************")

        self.driver.find_element_by_id("cleanseName").send_keys("CleanseNVARCHAR")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.setSchemaName("Sandbox")
        time.sleep(2)
        self.driver.find_element_by_id("outputName").send_keys("NVARCHARCleanse")
        self.IG.setLoadType("Complete Refresh")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),' Cleanse ')]").click()
        time.sleep(5)

        self.logger.info("***************************Convert Cleanse Validation *************************")

        self.lp.clickDatsets()
        time.sleep(5)
        self.lp.clickPrepared()
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='NVARCHARCleanse']")
        print(element.text)
        if element.text == "NVARCHARCleanse":
            assert True
            self.driver.close()
            self.logger.info("***************************Convert NVARCHAR Cleanse Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_ConvertNVARCHAR Cleanse.png")
            self.driver.close()
            self.logger.error("**************************Convert NVARCHAR Cleanse Failed *************************")
            assert False
