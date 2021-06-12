import time
import logging
import pytest
from selenium import webdriver

from Pages.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()



    def test_signinPageTitle(self, setup):
        self.logger.info("***************************Test_001_Login*************************")
        self.logger.info("***************************Sign In Page Title Validation *************************")
        self.driver = setup
        self.driver.get(self.baseURL)

        act_title = self.driver.title

        if act_title == "Sign in to your account":
            assert True
            self.driver.close()
            self.logger.info("***************************Sign In Page Title Passed *************************")


        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("***************************Sign In Page Title Failed *************************")
            assert False




    def test_login(self,setup):
        self.logger.info("***************************Login Validation *************************")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp= LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.clickNext()
        time.sleep(5)
        self.lp.setPassword(self.password)
        self.lp.clickPswdSignIn()
        time.sleep(5)
        self.lp.clickYes()
        time.sleep(5)
        self.driver.get("https://tiplatform-uat.azurewebsites.net/")
        self.lp.clickSignIn()
        time.sleep(7)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        act_title=self.driver.title
        if act_title=="Tesser Pro":
            self.driver.close()
            assert True
            self.logger.info("***************************Login Passed *************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("***************************Login Failed *************************")
            assert False

