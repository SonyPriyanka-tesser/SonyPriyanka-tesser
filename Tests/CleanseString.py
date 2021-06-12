import time
import datetime

import pytest
from selenium import webdriver


from Pages.CleansePage import CleansePage
from Pages.DataCatalogPage import DataCatalogPage
from Pages.IngestPage import IngestPage
from Pages.LoginPage import LoginPage
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig

class Test_004_CleanseString:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_Cleanse_RTRIM(self, setup):
        self.logger.info("***************************Test_004_CleanseStringColumn*************************")
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
        self.logger.info("***************************Cleanse RTRIM *************************")

        self.cp.clickAddColumn()
        time.sleep(5)
        self.cp.setSearchColumn("Email")
        time.sleep(5)
        self.cp.clickEmail()
        self.cp.clickAdd()
        time.sleep(5)
        self.cp.clickAddfunction()
        time.sleep(5)
        self.cp.clickRTRIM()
        time.sleep(5)
        self.logger.info("***********************Cleanse RTRIM Function****************")

        self.cp.clickPreviewicon()
        time.sleep(5)
        self.logger.info("***************************Cleanse RTRIM  Validation *************************")
        table = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody")
        TotalRows = table.find_elements_by_tag_name("tr")

        rowCount = len(TotalRows)
        print(rowCount)
        print("Before" + "                            " + "After")
        for r in range(1, rowCount + 1):
            table = self.driver.find_element_by_xpath("//table[@role='table']")

            before = table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[1]").text
            after = before.rstrip()
            print(before, "         ", after)
            b = table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[2]").text

            if after == b:
                assert True
                self.logger.info(
                    "***************************RTRIM Passed *************************")
            else:

                self.driver.save_screenshot(".\\Screenshots\\" + "test_RTRIM.png")
                self.logger.error(
                    "***************************RTRIM Failed *************************")
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

        self.logger.info("***********************Cleanse RTRIM Function ****************")

        self.driver.find_element_by_id("cleanseName").send_keys("CleanseRTRIM")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.setSchemaName("Sandbox")
        time.sleep(2)
        self.driver.find_element_by_id("outputName").send_keys("RTRIMCleanse")
        self.IG.setLoadType("Complete Refresh")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),' Cleanse ')]").click()
        time.sleep(5)

        self.logger.info("***************************RTRIM Cleanse Validation *************************")

        self.lp.clickDatsets()
        time.sleep(5)
        self.lp.clickPrepared()
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='RTRIMCleanse']")
        print(element.text)
        if element.text == "RTRIMCleanse":
            assert True
            self.driver.close()
            self.logger.info("*************************** RTRIM Cleanse Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_RTRIM Cleanse.png")
            self.driver.close()
            self.logger.error("**************************RTRIM Cleanse Failed *************************")
            assert False

    def test_Cleanse_LTRIM(self, setup):
        self.logger.info("***************************Test_004_CleanseStringColumn*************************")
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
        self.logger.info("***************************Cleanse LTRIM *************************")

        self.cp.clickAddColumn()
        time.sleep(5)
        self.cp.setSearchColumn("Email")
        time.sleep(5)
        self.cp.clickEmail()
        self.cp.clickAdd()
        time.sleep(5)
        self.cp.clickAddfunction()
        time.sleep(5)
        self.cp.clickLTRIM()
        time.sleep(5)
        self.logger.info("***********************Cleanse LTRIM Function****************")

        self.cp.clickPreviewicon()
        time.sleep(5)
        self.logger.info("***************************Cleanse LTRIM  Validation *************************")
        table = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody")
        TotalRows = table.find_elements_by_tag_name("tr")

        rowCount = len(TotalRows)
        print(rowCount)
        print("Before" + "                            " + "After")
        for r in range(1, rowCount + 1):
            table = self.driver.find_element_by_xpath("//table[@role='table']")

            before = table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[1]").text
            after = before.lstrip()
            print(before, "         ", after)
            b = table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[2]").text

            if after == b:
                assert True
                self.logger.info(
                    "***************************LTRIM Passed *************************")
            else:

                self.driver.save_screenshot(".\\Screenshots\\" + "test_LTRIM.png")
                self.logger.error(
                    "***************************LTRIM Failed *************************")
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

        self.logger.info("***********************Cleanse LTRIM Function ****************")

        self.driver.find_element_by_id("cleanseName").send_keys("CleanseLTRIM")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.setSchemaName("Sandbox")
        time.sleep(2)
        self.driver.find_element_by_id("outputName").send_keys("LTRIMCleanse")
        self.IG.setLoadType("Complete Refresh")
        time.sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(),' Cleanse ')]").click()
        time.sleep(5)

        self.logger.info("***************************LTRIM Cleanse Validation *************************")

        self.lp.clickDatsets()
        time.sleep(5)
        self.lp.clickPrepared()
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='LTRIMCleanse']")
        print(element.text)
        if element.text == "LTRIMCleanse":
            assert True
            self.driver.close()
            self.logger.info("*************************** LTRIM Cleanse Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_LTRIM Cleanse.png")
            self.driver.close()
            self.logger.error("**************************LTRIM Cleanse Failed *************************")
            assert False

    def test_Cleanse_Length(self, setup):
        self.logger.info("***************************Test_004_CleanseStringColumn*************************")
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
        time.sleep(5)
        self.cp.clickCleanse()
        time.sleep(5)
        self.logger.info("***************************Cleanse Length *************************")

        self.cp.clickAddColumn()
        time.sleep(5)
        self.cp.setSearchColumn("Email")
        time.sleep(5)
        self.cp.clickEmail()
        self.cp.clickAdd()
        time.sleep(5)
        self.cp.clickAddfunction()
        time.sleep(5)
        self.cp.clickLength()
        time.sleep(5)
        self.logger.info("***********************Cleanse Length Function****************")

        self.cp.clickPreviewicon()
        time.sleep(5)
        self.logger.info("***************************Cleanse Length  Validation *************************")
        table = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody")
        TotalRows = table.find_elements_by_tag_name("tr")

        rowCount = len(TotalRows)
        print(rowCount)
        print("Before" + "       " + "After")
        for r in range(1, rowCount + 1):
            table = self.driver.find_element_by_xpath("//table[@role='table']")

            before = table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[1]").text

            after = len(before)
            # print(before, "         ", after)
            b = int(table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[2]").text)
            print(before, "         ", after)
            if after == b:
                assert True
                self.logger.info(
                    "***************************Length Passed *************************")
            else:

                self.driver.save_screenshot(".\\Screenshots\\" + "test_Length.png")
                self.logger.error(
                    "***************************Length Failed *************************")
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

        self.logger.info("***********************Cleanse Length Function ****************")

        self.driver.find_element_by_id("cleanseName").send_keys("CleanseLength")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.setSchemaName("Sandbox")
        time.sleep(2)
        self.driver.find_element_by_id("outputName").send_keys("LengthCleanse")
        self.IG.setLoadType("Complete Refresh")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),' Cleanse ')]").click()
        time.sleep(5)

        self.logger.info("***************************Length Cleanse Validation *************************")

        self.lp.clickDatsets()
        time.sleep(5)
        self.lp.clickPrepared()
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='LengthCleanse']")
        print(element.text)
        if element.text == "LengthCleanse":
            assert True
            self.driver.close()
            self.logger.info("*************************** Length Cleanse Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_Length Cleanse.png")
            self.driver.close()
            self.logger.error("**************************Length Cleanse Failed *************************")
            assert False


    def test_Cleanse_Right(self, setup):
        self.logger.info("***************************Test_004_CleanseStringColumn*************************")
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
        time.sleep(5)
        self.cp.clickCleanse()
        time.sleep(5)
        self.logger.info("***************************Cleanse Right *************************")

        self.cp.clickAddColumn()
        time.sleep(5)
        self.cp.setSearchColumn("Email")
        time.sleep(5)
        self.cp.clickEmail()
        self.cp.clickAdd()
        time.sleep(5)
        self.cp.clickAddfunction()
        time.sleep(5)
        self.cp.clickRight()
        time.sleep(5)
        self.driver.find_element_by_xpath(
            "/html/body/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/img").click()
        time.sleep(5)
        self.driver.find_element_by_id("trimLength").send_keys("3")
        time.sleep(5)
        self.cp.clickUpdate()
        time.sleep(5)
        self.logger.info("***********************Cleanse Right Function****************")

        self.cp.clickPreviewicon()
        time.sleep(5)
        self.logger.info("***************************Cleanse Right  Validation *************************")
        table = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody")
        TotalRows = table.find_elements_by_tag_name("tr")

        rowCount = len(TotalRows)
        print(rowCount)
        print("Before" + "       " + "After")
        for r in range(1, rowCount + 1):
            table = self.driver.find_element_by_xpath("//table[@role='table']")

            before = table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[1]").text
            after = before[-3:]

            #print(before, "         ", after)
            b = table.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[2]").text
            print(before, "         ", after)
            if after == b:
                assert True
                self.logger.info(
                    "***************************Right Passed *************************")
            else:

                self.driver.save_screenshot(".\\Screenshots\\" + "test_Length.png")
                self.logger.error(
                    "***************************Right Failed *************************")
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

        self.logger.info("***********************Cleanse Right Function ****************")

        self.driver.find_element_by_id("cleanseName").send_keys("CleanseRight")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.setSchemaName("Sandbox")
        time.sleep(2)
        self.driver.find_element_by_id("outputName").send_keys("RightCleanse")
        self.IG.setLoadType("Complete Refresh")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),' Cleanse ')]").click()
        time.sleep(5)

        self.logger.info("***************************Right Cleanse Validation *************************")
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        self.lp.clickPrepared()
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='RightCleanse']")
        print(element.text)
        if element.text == "RightCleanse":
            assert True
            self.driver.close()
            self.logger.info("*************************** Right Cleanse Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_Right Cleanse.png")
            self.driver.close()
            self.logger.error("**************************Right Cleanse Failed *************************")
            assert False

    def test_Cleanse_Left(self, setup):
        self.logger.info("***************************Test_004_CleanseStringColumn*************************")
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
        time.sleep(5)
        self.cp.clickCleanse()
        time.sleep(5)
        self.logger.info("***************************Cleanse Left *************************")

        self.cp.clickAddColumn()
        time.sleep(5)
        self.cp.setSearchColumn("Email")
        time.sleep(5)
        self.cp.clickEmail()
        self.cp.clickAdd()
        time.sleep(5)
        self.cp.clickAddfunction()
        time.sleep(5)
        self.cp.clickLeft()
        time.sleep(5)
        self.driver.find_element_by_xpath(
            "/html/body/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/img").click()
        time.sleep(5)
        self.driver.find_element_by_id("trimLength").send_keys("3")
        time.sleep(5)
        self.cp.clickUpdate()
        time.sleep(5)
        self.logger.info("***********************Cleanse Left Function****************")

        self.cp.clickPreviewicon()
        time.sleep(5)
        self.logger.info("***************************Cleanse Left  Validation *************************")
        table = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody")
        TotalRows = table.find_elements_by_tag_name("tr")

        rowCount = len(TotalRows)
        print(rowCount)
        print("Before" + "       " + "After")
        for r in range(1, rowCount + 1):
            table = self.driver.find_element_by_xpath("//table[@role='table']")

            before = table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[1]").text
            after = before[0:3]

            # print(before, "         ", after)
            b = table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[2]").text
            print(before, "         ", after)
            if after == b:
                assert True
                self.logger.info(
                    "***************************Left Passed *************************")
            else:

                self.driver.save_screenshot(".\\Screenshots\\" + "test_Left.png")
                self.logger.error(
                    "***************************Left Failed *************************")
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

        self.logger.info("***********************Cleanse Left Function ****************")

        self.driver.find_element_by_id("cleanseName").send_keys("CleanseLeft")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.setSchemaName("Sandbox")
        time.sleep(2)
        self.driver.find_element_by_id("outputName").send_keys("LeftCleanse")
        self.IG.setLoadType("Complete Refresh")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),' Cleanse ')]").click()
        time.sleep(5)

        self.logger.info("***************************Left Cleanse Validation *************************")
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        self.lp.clickPrepared()
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='LeftCleanse']")
        print(element.text)
        if element.text == "LeftCleanse":
            assert True
            self.driver.close()
            self.logger.info("*************************** Left Cleanse Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_Left Cleanse.png")
            self.driver.close()
            self.logger.error("**************************Left Cleanse Failed *************************")
            assert False

    def test_Cleanse_Reverse(self, setup):
        self.logger.info("***************************Test_004_CleanseStringColumn*************************")
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
        time.sleep(5)
        self.cp.clickCleanse()
        time.sleep(5)
        self.logger.info("***************************Cleanse Reverse *************************")

        self.cp.clickAddColumn()
        time.sleep(5)
        self.cp.setSearchColumn("Email")
        time.sleep(5)
        self.cp.clickEmail()
        self.cp.clickAdd()
        time.sleep(5)
        self.cp.clickAddfunction()
        time.sleep(5)
        self.cp.clickReverse()
        time.sleep(5)

        self.logger.info("***********************Cleanse Reverse Function****************")

        self.cp.clickPreviewicon()
        time.sleep(5)
        self.logger.info("***************************Cleanse Reverse  Validation *************************")
        table = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody")
        TotalRows = table.find_elements_by_tag_name("tr")

        rowCount = len(TotalRows)
        print(rowCount)
        print("Before" + "       " + "After")
        for r in range(1, rowCount + 1):
            table = self.driver.find_element_by_xpath("//table[@role='table']")

            before = table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[1]").text
            after = before[::-1]

            #print(before, "         ", after)
            b = table.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[2]").text
            print(before, "         ", after)
            if after == b:
                assert True
                self.logger.info(
                    "***************************Reverse Passed *************************")
            else:

                self.driver.save_screenshot(".\\Screenshots\\" + "test_Reverse.png")
                self.logger.error(
                    "***************************Reverse Failed *************************")
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

        self.logger.info("***********************Cleanse Reverse Function ****************")

        self.driver.find_element_by_id("cleanseName").send_keys("CleanseReverse")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.setSchemaName("Sandbox")
        time.sleep(2)
        self.driver.find_element_by_id("outputName").send_keys("ReverseCleanse")
        self.IG.setLoadType("Complete Refresh")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),' Cleanse ')]").click()
        time.sleep(5)

        self.logger.info("***************************Reverse Cleanse Validation *************************")
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        self.lp.clickPrepared()
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='ReverseCleanse']")
        print(element.text)
        if element.text == "ReverseCleanse":
            assert True
            self.driver.close()
            self.logger.info("*************************** Reverse Cleanse Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_Reverse Cleanse.png")
            self.driver.close()
            self.logger.error("**************************Reverse Cleanse Failed *************************")
            assert False

    def test_Cleanse_Lower(self, setup):
        self.logger.info("***************************Test_004_CleanseStringColumn*************************")
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
        self.logger.info("***************************Cleanse Lower *************************")

        self.cp.clickAddColumn()
        time.sleep(5)
        self.cp.setSearchColumn("Email")
        time.sleep(5)
        self.cp.clickEmail()
        self.cp.clickAdd()
        time.sleep(5)
        self.cp.clickAddfunction()
        time.sleep(5)
        self.cp.clickLower()
        time.sleep(5)

        self.logger.info("***********************Cleanse Lower Function****************")

        self.cp.clickPreviewicon()
        time.sleep(5)
        self.logger.info("***************************Cleanse Lower  Validation *************************")
        table = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody")
        TotalRows = table.find_elements_by_tag_name("tr")

        rowCount = len(TotalRows)
        print(rowCount)
        print("Before" + "       " + "After")
        for r in range(1, rowCount + 1):
            table = self.driver.find_element_by_xpath("//table[@role='table']")

            before = table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[1]").text
            after = before.lower()

            #print(before, "         ", after)
            b = table.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[2]").text
            print(before, "         ", after)
            if after == b:
                assert True
                self.logger.info(
                    "***************************Lower Passed *************************")
            else:

                self.driver.save_screenshot(".\\Screenshots\\" + "test_Lower.png")
                self.logger.error(
                    "***************************Lower Failed *************************")
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

        self.logger.info("***********************Cleanse Lower Function ****************")

        self.driver.find_element_by_id("cleanseName").send_keys("CleanseLower")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.setSchemaName("Sandbox")
        time.sleep(2)
        self.driver.find_element_by_id("outputName").send_keys("LowerCleanse")
        self.IG.setLoadType("Complete Refresh")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),' Cleanse ')]").click()
        time.sleep(5)

        self.logger.info("***************************Lower Cleanse Validation *************************")
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        self.lp.clickPrepared()
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='LowerCleanse']")
        print(element.text)
        if element.text == "LowerCleanse":
            assert True
            self.driver.close()
            self.logger.info("*************************** Lower Cleanse Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_LowerCleanse.png")
            self.driver.close()
            self.logger.error("**************************Lower Cleanse Failed *************************")
            assert False

    def test_Cleanse_Upper(self, setup):
        self.logger.info("***************************Test_004_CleanseStringColumn*************************")
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
        self.logger.info("***************************Cleanse Upper *************************")

        self.cp.clickAddColumn()
        time.sleep(5)
        self.cp.setSearchColumn("Email")
        time.sleep(5)
        self.cp.clickEmail()
        self.cp.clickAdd()
        time.sleep(5)
        self.cp.clickAddfunction()
        time.sleep(5)
        self.cp.clickUpper()
        time.sleep(5)

        self.logger.info("***********************Cleanse Upper Function****************")

        self.cp.clickPreviewicon()
        time.sleep(5)
        self.logger.info("***************************Cleanse Upper  Validation *************************")
        table = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody")
        TotalRows = table.find_elements_by_tag_name("tr")

        rowCount = len(TotalRows)
        print(rowCount)
        print("Before" + "                        " + "After")
        for r in range(1, rowCount + 1):
            table = self.driver.find_element_by_xpath("//table[@role='table']")

            before = table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[1]").text
            after = before.upper()

            #print(before, "         ", after)
            b = table.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[2]").text
            print(before, "         ", after)
            if after == b:
                assert True
                self.logger.info(
                    "***************************Upper Passed *************************")
            else:

                self.driver.save_screenshot(".\\Screenshots\\" + "test_Upper.png")
                self.logger.error(
                    "***************************Upper Failed *************************")
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

        self.logger.info("***********************Cleanse Upper Function ****************")

        self.driver.find_element_by_id("cleanseName").send_keys("CleanseUpper")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.setSchemaName("Sandbox")
        time.sleep(2)
        self.driver.find_element_by_id("outputName").send_keys("UpperCleanse")
        self.IG.setLoadType("Complete Refresh")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),' Cleanse ')]").click()
        time.sleep(5)

        self.logger.info("***************************Upper Cleanse Validation *************************")
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        self.lp.clickPrepared()
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='UpperCleanse']")
        print(element.text)
        if element.text == "UpperCleanse":
            assert True
            self.driver.close()
            self.logger.info("*************************** Upper Cleanse Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_UpperCleanse.png")
            self.driver.close()
            self.logger.error("**************************Upper Cleanse Failed *************************")
            assert False

    def test_Cleanse_Replace(self, setup):
        self.logger.info("***************************Test_004_CleanseStringColumn*************************")
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
        self.logger.info("***************************Cleanse Replace *************************")

        self.cp.clickAddColumn()
        time.sleep(10)
        self.cp.setSearchColumn("Email")
        time.sleep(5)
        self.cp.clickEmail()
        self.cp.clickAdd()
        time.sleep(5)
        self.cp.clickAddfunction()
        time.sleep(5)
        self.cp.clickReplace()
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/img").click()
        time.sleep(5)
        self.driver.find_element_by_id("replaceString").send_keys("example")
        time.sleep(5)
        self.driver.find_element_by_id("replaceStringWith").send_keys("gmail")
        time.sleep(5)
        self.cp.clickUpdate()
        time.sleep(5)

        self.logger.info("***********************Cleanse Replace Function****************")

        self.cp.clickPreviewicon()
        time.sleep(5)
        self.logger.info("***************************Cleanse Replace  Validation *************************")
        table = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody")
        TotalRows = table.find_elements_by_tag_name("tr")

        rowCount = len(TotalRows)
        print(rowCount)
        print("Before" + "                        " + "After")
        for r in range(1, rowCount + 1):
            table = self.driver.find_element_by_xpath("//table[@role='table']")

            before = table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[1]").text
            after = before.replace("example", "gmail")

            #print(before, "         ", after)
            b = table.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[2]").text
            print(before, "         ", after)
            if after == b:
                assert True
                self.logger.info(
                    "***************************Replace Passed *************************")
            else:

                self.driver.save_screenshot(".\\Screenshots\\" + "test_Replace.png")
                self.logger.error(
                    "***************************Replace Failed *************************")
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

        self.logger.info("***********************Cleanse Replace Function ****************")

        self.driver.find_element_by_id("cleanseName").send_keys("CleanseReplace")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.setSchemaName("Sandbox")
        time.sleep(2)
        self.driver.find_element_by_id("outputName").send_keys("ReplaceCleanse")
        self.IG.setLoadType("Complete Refresh")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),' Cleanse ')]").click()
        time.sleep(5)

        self.logger.info("***************************Replace Cleanse Validation *************************")
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        self.lp.clickPrepared()
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='ReplaceCleanse']")
        print(element.text)
        if element.text == "ReplaceCleanse":
            assert True
            self.driver.close()
            self.logger.info("*************************** Replace Cleanse Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_ReplaceCleanse.png")
            self.driver.close()
            self.logger.error("**************************Replace Cleanse Failed *************************")
            assert False

    def test_Cleanse_Substring(self, setup):
        self.logger.info("***************************Test_004_CleanseStringColumn*************************")
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
        self.logger.info("***************************Cleanse Substring *************************")

        self.cp.clickAddColumn()
        time.sleep(10)
        self.cp.setSearchColumn("Email")
        time.sleep(5)
        self.cp.clickEmail()
        self.cp.clickAdd()
        time.sleep(5)
        self.cp.clickAddfunction()
        time.sleep(5)
        self.cp.clickSubstring()
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/img").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//input[@id='startPosition']").send_keys("4")
        time.sleep(5)
        self.driver.find_element_by_id("subStringLength").send_keys("10")
        time.sleep(5)
        self.cp.clickUpdate()
        time.sleep(5)

        self.logger.info("***********************Cleanse Substring Function****************")

        self.cp.clickPreviewicon()
        time.sleep(5)
        self.logger.info("***************************Cleanse Substring  Validation *************************")
        table = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody")
        TotalRows = table.find_elements_by_tag_name("tr")

        rowCount = len(TotalRows)
        print(rowCount)
        print("Before" + "                               " + "After")
        for r in range(1, rowCount + 1):
            table = self.driver.find_element_by_xpath("//table[@role='table']")

            before = table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[1]").text
            after = before[3:13]

            #print(before, "         ", after)
            b = table.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[2]").text
            print(before, "         ", after)
            if after == b:
                assert True
                self.logger.info(
                    "***************************Substring Passed *************************")
            else:

                self.driver.save_screenshot(".\\Screenshots\\" + "test_Substring.png")
                self.logger.error(
                    "***************************Substring Failed *************************")
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

        self.logger.info("***********************Cleanse Substring Function ****************")

        self.driver.find_element_by_id("cleanseName").send_keys("CleanseSubstring")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.setSchemaName("Sandbox")
        time.sleep(2)
        self.driver.find_element_by_id("outputName").send_keys("SubstringCleanse")
        self.IG.setLoadType("Complete Refresh")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),' Cleanse ')]").click()
        time.sleep(5)

        self.logger.info("***************************Substring Cleanse Validation *************************")
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        self.lp.clickPrepared()
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='SubstringCleanse']")
        print(element.text)
        if element.text == "SubstringCleanse":
            assert True
            self.driver.close()
            self.logger.info("*************************** Substring Cleanse Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_Substring Cleanse.png")
            self.driver.close()
            self.logger.error("**************************Substring Cleanse Failed *************************")
            assert False

    def test_Cleanse_IsNull(self, setup):
        self.logger.info("***************************Test_004_CleanseStringColumn*************************")
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
        self.logger.info("***************************Cleanse IsNull *************************")

        self.cp.clickAddColumn()
        time.sleep(10)
        self.cp.setSearchColumn("Email")
        time.sleep(5)
        self.cp.clickEmail()
        self.cp.clickAdd()
        time.sleep(5)
        self.cp.clickAddfunction()
        time.sleep(5)
        self.cp.clickIsNull()
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/img").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//input[@id='replaceNullWith']").send_keys("NULL")
        time.sleep(5)
        self.cp.clickUpdate()
        time.sleep(5)

        self.logger.info("***********************Cleanse IsNull Function****************")

        self.cp.clickPreviewicon()
        time.sleep(5)
        self.logger.info("***************************Cleanse IsNull  Validation *************************")
        table = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody")
        TotalRows = table.find_elements_by_tag_name("tr")

        rowCount = len(TotalRows)
        print(rowCount)
        #print("Before" + "                               " + "After")
        for r in range(1, rowCount + 1):
            table = self.driver.find_element_by_xpath("//table[@role='table']")

            before = table.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[1]").text
            if before == "":
                print("NULL")
            else:
                print(before)
        after = table.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[2]").text
        print(before, "         ", after)
        if before==after:
            assert True
            self.logger.info(
                "***************************IsNull Passed *************************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_IsNull.png")
            self.logger.error("***************************IsNull Failed *************************")
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

        self.logger.info("***********************Cleanse IsNull Function ****************")

        self.driver.find_element_by_id("cleanseName").send_keys("CleanseIsNull")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.setSchemaName("Sandbox")
        time.sleep(2)
        self.driver.find_element_by_id("outputName").send_keys("IsNullCleanse")
        self.IG.setLoadType("Complete Refresh")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),' Cleanse ')]").click()
        time.sleep(5)

        self.logger.info("***************************IsNull Cleanse Validation *************************")
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        self.lp.clickPrepared()
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='IsNullCleanse']")
        print(element.text)
        if element.text == "IsNullCleanse":
            assert True
            self.driver.close()
            self.logger.info("*************************** IsNull Cleanse Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_IsNull Cleanse.png")
            self.driver.close()
            self.logger.error("**************************IsNull Cleanse Failed *************************")
            assert False

    def test_Cleanse_Stuff(self, setup):
        self.logger.info("***************************Test_004_CleanseStringColumn*************************")
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
        self.cp.setSearch("Cleanse")
        self.cp.clickSearch()
        assert True
        time.sleep(5)
        self.cp.clickCleanse()
        time.sleep(5)
        self.logger.info("***************************Cleanse Stuff *************************")

        self.cp.clickAddColumn()
        time.sleep(10)
        self.cp.setSearchColumn("Email")
        time.sleep(5)
        self.cp.clickEmail()
        self.cp.clickAdd()
        time.sleep(5)
        self.cp.clickAddfunction()
        time.sleep(5)
        self.cp.clickStuff()
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/img").click()
        time.sleep(5)
        self.driver.find_element_by_id("startingPosition").send_keys("4")
        time.sleep(2)
        self.driver.find_element_by_id("trimLength").send_keys("8")
        time.sleep(2)

        self.driver.find_element_by_id("replaceStringWith").send_keys("STUFF")
        time.sleep(2)
        self.cp.clickUpdate()
        time.sleep(5)

        self.logger.info("***********************Cleanse Stuff Function****************")

        self.cp.clickPreviewicon()
        time.sleep(5)
        self.logger.info("***************************Cleanse Stuff  Validation *************************")
        table = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody")
        TotalRows = table.find_elements_by_tag_name("tr")

        rowCount = len(TotalRows)
        print(rowCount)
        print("Before" + "                        " + "After")
        for r in range(1, rowCount + 1):
            table = self.driver.find_element_by_xpath("//table[@role='table']")

            before = table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[1]").text
            after = before.replace(before[3:11],"STUFF")

            #print(before, "         ", after)
            b = table.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[2]").text
            print(before, "         ", after)
            if after == b:
                assert True
                self.logger.info(
                    "***************************Stuff Passed *************************")
            else:

                self.driver.save_screenshot(".\\Screenshots\\" + "test_Stuff.png")
                self.logger.error(
                    "***************************Stuff Failed *************************")
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

        self.logger.info("***********************Cleanse Stuff Function ****************")

        self.driver.find_element_by_id("cleanseName").send_keys("CleanseStuff")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.setSchemaName("Sandbox")
        time.sleep(2)
        self.driver.find_element_by_id("outputName").send_keys("StuffCleanse")
        self.IG.setLoadType("Complete Refresh")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),' Cleanse ')]").click()
        time.sleep(5)

        self.logger.info("***************************Stuff Cleanse Validation *************************")
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        self.lp.clickPrepared()
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='StuffCleanse']")
        print(element.text)
        if element.text == "StuffCleanse":
            assert True
            self.driver.close()
            self.logger.info("*************************** Stuff Cleanse Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_StuffCleanse.png")
            self.driver.close()
            self.logger.error("**************************Stuff Cleanse Failed *************************")
            assert False

    def test_Cleanse_Translate(self, setup):
        self.logger.info("***************************Test_004_CleanseStringColumn*************************")
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
        self.logger.info("***************************Cleanse Translate *************************")

        self.cp.clickAddColumn()
        time.sleep(10)
        self.cp.setSearchColumn("Email")
        time.sleep(5)
        self.cp.clickEmail()
        self.cp.clickAdd()
        time.sleep(5)
        self.cp.clickAddfunction()
        time.sleep(5)
        self.cp.clickTranslate()
        time.sleep(5)
        self.driver.find_element_by_xpath(
            "/html/body/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/img").click()
        time.sleep(5)
        self.driver.find_element_by_id("translateString").send_keys("rahl")
        time.sleep(5)
        self.driver.find_element_by_id("translateStringWith").send_keys("1234")
        time.sleep(5)

        self.cp.clickUpdate()
        time.sleep(5)

        self.logger.info("***********************Cleanse Translate Function****************")

        self.cp.clickPreviewicon()
        time.sleep(5)
        self.logger.info("***************************Cleanse Translate  Validation *************************")
        table = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody")
        TotalRows = table.find_elements_by_tag_name("tr")

        rowCount = len(TotalRows)
        print(rowCount)
        print("Before" + "                        " + "After")
        for r in range(1, rowCount + 1):
            table = self.driver.find_element_by_xpath("//table[@role='table']")

            before = table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[1]").text
            a = before.maketrans("rahl", "1234")
            after = before.translate(a)
            b = table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[2]").text
            print(before, "         ", after)
            if after == b:
                assert True
                self.logger.info(
                    "***************************Translate Passed *************************")
            else:

                self.driver.save_screenshot(".\\Screenshots\\" + "test_Translate.png")
                self.logger.error(
                    "***************************Translate Failed *************************")
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

        self.logger.info("***********************Cleanse Translate Function ****************")

        self.driver.find_element_by_id("cleanseName").send_keys("CleanseTranslate")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.setSchemaName("Sandbox")
        time.sleep(2)
        self.driver.find_element_by_id("outputName").send_keys("TranslateCleanse")
        self.IG.setLoadType("Complete Refresh")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),' Cleanse ')]").click()
        time.sleep(5)

        self.logger.info("***************************Translate Cleanse Validation *************************")
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        self.lp.clickPrepared()
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='TranslateCleanse']")
        print(element.text)
        if element.text == "TranslateCleanse":
            assert True
            # self.driver.close()
            self.logger.info("*************************** Translate Cleanse Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_TranslateCleanse.png")
            # self.driver.close()p
            self.logger.error("**************************Translate Cleanse Failed *************************")
            assert False

    def test_Cleanse_IsNumeric(self, setup):
        self.logger.info("***************************Test_004_CleanseStringColumn*************************")
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
        self.logger.info("***************************Cleanse IsNumeric *************************")

        self.cp.clickAddColumn()
        time.sleep(10)
        self.cp.setSearchColumn("Email")
        time.sleep(5)
        self.cp.clickEmail()
        self.cp.clickAdd()
        time.sleep(5)
        self.cp.clickAddfunction()
        time.sleep(5)
        self.cp.clickIsNumeric()
        time.sleep(5)

        self.logger.info("***********************Cleanse IsNumeric Function****************")

        self.cp.clickPreviewicon()
        time.sleep(5)
        self.logger.info("***************************Cleanse IsNumeric  Validation *************************")
        table = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody")
        TotalRows = table.find_elements_by_tag_name("tr")

        rowCount = len(TotalRows)
        print(rowCount)
        print("Before" + "                        " + "After")
        for r in range(1, rowCount + 1):
            table = self.driver.find_element_by_xpath("//table[@role='table']")

            before = table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[1]").text
            b = int(table.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[2]").text)
            if before.isnumeric() == True:
                after = int(before.isnumeric())
            # print(after)

            else:
                after = int(before.isnumeric())
                # print(after)

            print(before, "         ", after)
            if after == b:
                assert True
                self.logger.info(
                    "***************************IsNumeric Passed *************************")
            else:

                self.driver.save_screenshot(".\\Screenshots\\" + "test_IsNumeric.png")
                self.logger.error(
                    "***************************IsNumeric Failed *************************")
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

        self.logger.info("***********************Cleanse IsNumeric Function ****************")

        self.driver.find_element_by_id("cleanseName").send_keys("CleanseIsNumeric")
        time.sleep(5)
        self.IG = IngestPage(self.driver)
        self.IG.setSchemaName("Sandbox")
        time.sleep(2)
        self.driver.find_element_by_id("outputName").send_keys("IsNumericCleanse")
        self.IG.setLoadType("Complete Refresh")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),' Cleanse ')]").click()
        time.sleep(5)

        self.logger.info("***************************IsNumeric Cleanse Validation *************************")
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        self.lp.clickPrepared()
        time.sleep(5)
        self.lp.clickDatsets()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@title='IsNumericCleanse']")
        print(element.text)
        if element.text == "IsNumericCleanse":
            assert True
            self.driver.close()
            self.logger.info("*************************** IsNumeric Cleanse Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_IsNumericCleanse.png")
            self.driver.close()
            self.logger.error("**************************IsNumeric Cleanse Failed *************************")
            assert False






