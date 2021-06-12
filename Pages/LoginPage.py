import logging

class LoginPage:
    button_signin_xpath = "//button[@type='button']"
    textbox_username_xpath="// input[ @ type = 'email']"
    button_next_xpath="//input[@value='Next']"
    textbox_password_xpath="// input[ @ name = 'passwd']"
    button_pwdsignin_xpath="//input[@type='submit']"
    button_yes_xpath = "//input[@type='submit']"
    button_search_xpath="//button[@type='submit']"

    button_Datasets_xpath="//div[contains(text(),' Datasets ')]"
    button_Files_xpath="//div[contains(text(),' Files ')]"
    button_Prepared_xpath="//div[contains(text(),' Prepared ')]"



    def __init__(self,driver):
        self.driver=driver

    def clickSignIn(self):
        self.driver.find_element_by_xpath(self.button_signin_xpath).click()

    def setUserName(self, username):
        self.driver.find_element_by_xpath(self.textbox_username_xpath).send_keys(username)

    def clickNext(self):
        self.driver.find_element_by_xpath(self.button_next_xpath).click()

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def clickPswdSignIn(self):
        self.driver.find_element_by_xpath(self.button_pwdsignin_xpath).click()

    def clickYes(self):
        self.driver.find_element_by_xpath(self.button_yes_xpath).click()

    def ClickSearch(self):
        self.driver.find_element_by_xpath(self.button_search_xpath).click()

    def clickDatsets(self):
        self.driver.find_element_by_xpath(self.button_Datasets_xpath).click()

    def clickPrepared(self):
        self.driver.find_element_by_xpath(self.button_Prepared_xpath).click()

    def clickFiles(self):
        self.driver.find_element_by_xpath(self.button_Files_xpath).click()

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger