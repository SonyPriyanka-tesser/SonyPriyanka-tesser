import time


class DataCatalogPage:
    button_Datasets_xpath = "//div[contains(text(),' Datasets ')]"
    button_Files_xpath = "//div[contains(text(),' Files ')]"
    txtTableName_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/span/form/span[1]/div/div/input"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtSchemaName_xpath = "//span[@class='multiselect__placeholder']"
    lstitemSandbox_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/span/form/span[2]/div/div[3]/ul/li[1]/span"

    button_CopyTable_xpath = "//button[contains(text(),'Copy Table')]"

    # View all Select one
    txtselectone_xpath = "/html/body/div[2]/div[1]/div/div/header/div/div[2]/div[2]/div[2]/span"
    lstitemLogin_xpath = "/html/body/div[2]/div[1]/div/div/header/div/div[2]/div[2]/div[3]/ul/li[2]/span"
    lstitemIdentifier_xpath = "/html/body/div[2]/div[1]/div/div/header/div/div[2]/div[2]/div[3]/ul/li[3]/span"
    lstitemOnetime_xpath = "/html/body/div[2]/div[1]/div/div/header/div/div[2]/div[2]/div[3]/ul/li[4]/span"
    lstitemrecoverycode_xpath = "/html/body/div[2]/div[1]/div/div/header/div/div[2]/div[2]/div[3]/ul/li[5]/span"
    lstitemFirstName_xpath = "/html/body/div[2]/div[1]/div/div/header/div/div[2]/div[2]/div[3]/ul/li[6]/span"
    lstitemLastName_xpath = "/html/body/div[2]/div[1]/div/div/header/div/div[2]/div[2]/div[3]/ul/li[7]/span"
    lstitemDepartment_xpath = "/html/body/div[2]/div[1]/div/div/header/div/div[2]/div[2]/div[3]/ul/li[8]/span"
    lstitemLocation_xpath = "/html/body/div[2]/div[1]/div/div/header/div/div[2]/div[2]/div[3]/ul/li[9]/span"
    lstitemDate_xpath = "/html/body/div[2]/div[1]/div/div/header/div/div[2]/div[2]/div[3]/ul/li[10]/span"
    lstitemID_xpath = "/html/body/div[2]/div[1]/div/div/header/div/div[2]/div[2]/div[3]/ul/li[11]/span"

    # View all Select Operator for numbers
    txtselectoperator1_xpath= "/html/body/div[2]/div[1]/div/div/header/div/div[2]/div[1]/div[2]/span"
    lstitemisNull1_xpath= "/html/body/div[2]/div[1]/div/div/header/div/div[2]/div[1]/div[3]/ul/li[1]/span"
    lstitemisNotNull1_xpath= "/html/body/div[2]/div[1]/div/div/header/div/div[2]/div[1]/div[3]/ul/li[2]/span"
    lstitemEqual1_xpath= "/html/body/div[2]/div[1]/div/div/header/div/div[2]/div[1]/div[3]/ul/li[3]/span"
    lstitemNotEqual1_xpath= "/html/body/div[2]/div[1]/div/div/header/div/div[2]/div[1]/div[3]/ul/li[4]/span"
    lstitemGreater1_xpath       = "/html/body/div[2]/div[1]/div/div/header/div/div[2]/div[1]/div[3]/ul/li[5]/span"
    lstitemGreaterEqual1_xpath  = "/html/body/div[2]/div[1]/div/div/header/div/div[2]/div[1]/div[3]/ul/li[6]/span"
    lstitemLessthan1_xpath      = "/html/body/div[2]/div[1]/div/div/header/div/div[2]/div[1]/div[3]/ul/li[7]/span"
    lstitemLessthanEqual1_xpath = "/html/body/div[2]/div[1]/div/div/header/div/div[2]/div[1]/div[3]/ul/li[8]/span"
    lstitemBetween1_xpath       = "/html/body/div[2]/div[1]/div/div/header/div/div[2]/div[1]/div[3]/ul/li[9]/span"

    # View all Select Operator for numbers
    txtselectoperator_xpath = "/html/body/div[2]/div[1]/div/div/header/div/div[2]/div[1]/div[2]/span"
    lstitemisNull_xpath = "/html/body/div[2]/div[1]/div/div/header/div/div[2]/div[1]/div[3]/ul/li[1]/span"
    lstitemisNotNull_xpath = "/html/body/div[2]/div[1]/div/div/header/div/div[2]/div[1]/div[3]/ul/li[2]/span"
    lstitemContains_xpath = "/html/body/div[2]/div[1]/div/div/header/div/div[2]/div[1]/div[3]/ul/li[3]/span"
    lstitemNotContains_xpath = "/html/body/div[2]/div[1]/div/div/header/div/div[2]/div[1]/div[3]/ul/li[4]/span"
    lstitemEqual_xpath = "/html/body/div[2]/div[1]/div/div/header/div/div[2]/div[1]/div[3]/ul/li[5]/span"
    lstitemNotEqual_xpath = "/html/body/div[2]/div[1]/div/div/header/div/div[2]/div[1]/div[3]/ul/li[6]/span"


    #View all Search
    txtsearch_xpath = "/html/body/div[2]/div[1]/div/div/header/div/div[2]/form/div/input"

    button_SearchICON_xpath = "/html/body/div[2]/div[1]/div/div/header/div/div[2]/form/div/div/img"

    #viewall Validation
    tblSearchResults_xpath = "//table[@role='table']"
    table_xpath = "//table[@role='table']"
    tableRows_xpath = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[1]"
    tableColumns_xpath = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[1]/td[1]"

    def __init__(self,driver):
        self.driver=driver


    def setTableName(self, tablename):
        self.driver.find_element_by_xpath(self.txtTableName_xpath).send_keys(tablename)

    def setSchemaName(self, SchemaName):
        self.driver.find_element_by_xpath(self.txtSchemaName_xpath).click()
        time.sleep(3)
        if SchemaName == 'Sandbox':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemSandbox_xpath)
        time.sleep(3)
        self.listitem.click()

    def ClickCopy(self):
        self.driver.find_element_by_xpath(self.button_CopyTable_xpath).click()

    def ClickDatasets(self):
        self.driver.find_element_by_xpath(self.button_Datasets_xpath).click()

    def ClickFiles(self):
        self.driver.find_element_by_xpath(self.button_Files_xpath).click()

    def setSelectOne(self, selectone):
        self.driver.find_element_by_xpath(self.txtselectone_xpath).click()
        time.sleep(3)
        if selectone == 'Loginemail':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemLogin_xpath)
        elif selectone == 'Identifier':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemIdentifier_xpath)
        elif selectone == 'Onetimepassword':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemOnetime_xpath)
        elif selectone == 'Recoverycode':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemrecoverycode_xpath)
        elif selectone == 'Firstname':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemFirstName_xpath)
        elif selectone == 'Lastname':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemLastName_xpath)
        elif selectone == 'Department':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemLocation_xpath)
        elif selectone == 'Location':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemDepartment_xpath)
        elif selectone == 'Date':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemDate_xpath)

        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemID_xpath)
        time.sleep(3)
        self.listitem.click()

    def setSelectOperator(self, selectoperator):
            self.driver.find_element_by_xpath(self.txtselectoperator_xpath).click()
            time.sleep(3)
            if selectoperator == 'IS NULL':
                self.listitem = self.driver.find_element_by_xpath(self.lstitemisNull_xpath)
            elif selectoperator == 'IS NOT NULL':
                self.listitem = self.driver.find_element_by_xpath(self.lstitemisNotNull_xpath)
            elif selectoperator == 'CONTAINS':
                self.listitem = self.driver.find_element_by_xpath(self.lstitemContains_xpath)
            elif selectoperator == 'NOT CONTAINS':
                self.listitem = self.driver.find_element_by_xpath(self.lstitemNotContains_xpath)
            elif selectoperator == '=':
                self.listitem = self.driver.find_element_by_xpath(self.lstitemEqual_xpath)


            else:
                self.listitem = self.driver.find_element_by_xpath(self.lstitemNotEqual_xpath)
            time.sleep(3)
            self.listitem.click()

    def setSearch(self, search):
            self.driver.find_element_by_xpath(self.txtsearch_xpath).send_keys(search)

    def ClickSearchIcon(self):
        self.driver.find_element_by_xpath(self.button_SearchICON_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))

    def searchLoginEmail_Contains(self,email):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            emailid = table.find_element_by_xpath("//html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr["+str(r)+"]/td[1]").text
            if emailid == email:
                flag = True
                break
        return flag


