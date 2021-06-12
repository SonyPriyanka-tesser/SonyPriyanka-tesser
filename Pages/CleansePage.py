import time


class CleansePage:
    txtsearch_xpath ="//input[@placeholder='Type a keyword or press search']"
    button_search_Xpath="/html/body/div/div[1]/div[1]/nav/div/form/div/div/button/span"

    txtDatatype_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div[1]/span/form/div[2]/div[1]/span/div[1]/div[2]/span"
    lstitembigint_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div[1]/span/form/div[2]/div[1]/span/div[1]/div[3]/ul/li[1]/span"
    lstitembit_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div[1]/span/form/div[2]/div[1]/span/div[1]/div[3]/ul/li[2]/span"
    lstitemdatetime_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div[1]/span/form/div[2]/div[1]/span/div[1]/div[3]/ul/li[3]/span"
    lstitemnvarchar_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div[1]/span/form/div[2]/div[1]/span/div[1]/div[3]/ul/li[4]/span"

    txtDataFormat_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div[1]/span/form/div[2]/div[2]/span/div/div[2]/span"
    lstitemDMY_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div[1]/span/form/div[2]/div[2]/span/div/div[3]/ul/li[3]/span"
    lstitemMDY_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div[1]/span/form/div[2]/div[2]/span/div/div[3]/ul/li[4]/span"
    lstitemYMDHMS_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div[1]/span/form/div[2]/div[2]/span/div/div[3]/ul/li[5]/span"

    button_File2Table_xpath="//div[@title='File2Table']"
    button_Cleansefile_xpath="//div[@title='Cleanse']"
    button_Cleanse_xpath="//img[@alt='Cleanse']"
    button_addcolumn_xpath="//span[contains(text(),'Add column')]"
    txt_searchcolumn_xpath="/html/body/div[2]/div[1]/div/div/div/div/div/div/div[1]/form/div/input"
    button_Prepexam1_xpath="//div[@title='Prepexam1']"
    button_Email_xpath="//div[@title='Email']"
    button_Add_xpath="/html/body/div[2]/div[1]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div[3]/button"
    button_Addfunction_xpath="//span[contains(text(),'Click here to add function')]"

    #Arithmatic
    button_Arithmatic_xpath="//img[@alt='ARITHMETIC']"
    button_Operator_xpath="//div[contains(text(),'OPERATOR')]"
    button_ADD_xpath="//img[@alt='add']"
    txt_operatorvalue_id="mathOperatorValue"
    button_update_xpath="//button[contains(text(),' Update ')]"

    #Convert
    button_Convert_xpath="//img[@alt='CONVERT']"
    button_previewicon_xpath="//img[@alt='Preview Function Output']"
    button_previewclose_xpath="//img[@alt='Close cleanse function preview popup']"

    #LTRIM
    button_LTRIM_xpath="//img[@alt='LTRIM']"
    #RTRIM
    button_RTRIM_xpath="//img[@alt='LTRIM']"
    #Length
    button_Length_xpath="//img[@alt='LENGTH']"
    #Right
    button_RIGHT_xpath = "//img[@alt='RIGHT']"
    #Left
    button_Left_xpath = "//img[@alt='LEFT']"
    #Lower
    button_Lower_xpath = "//img[@alt='LOWER']"
    #Upper
    button_Upper_xpath = "//img[@alt='UPPER']"
    # Reverse
    button_Reverse_xpath = "//img[@alt='REVERSE']"
    #Replace
    button_Replace_xpath = "//img[@alt='REPLACE']"
    #Substring
    button_Substring_xpath = "//img[@alt='SUBSTRING']"
    # Stuff
    button_Stuff_xpath = "//img[@alt='STUFF']"
    #IsNull
    button_Isnull_xpath="//img[@alt='ISNULL']"
    #Translate
    button_Translate_xpath="//img[@alt='TRANSLATE']"
    #IsNumeric
    button_IsNumeric_xpath = "//img[@alt='ISNUMERIC']"

    #FormQuery
    button_FormQuery_Xpath="//img[@alt='Form Query']"
    button_CopyFormquery_xpath="//button[contains(text(),' Copy ')]"
    button_CloseformQuery_xpath="//img[@alt='Close column select popup']"

    # Paginatiom Validation
    tblSearchResults_xpath = "//table[@role='table']"
    table_xpath = "//table[@role='table']"
    tableRows_xpath = "/html/body/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/div/div[1]/table/tbody/tr"
    tableColumns_xpath = "/html/body/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/div/div[1]/table/tbody/tr/td"

    def __init__(self,driver):
        self.driver=driver

    def setDatatype(self, datatype):
        self.driver.find_element_by_xpath(self.txtDatatype_xpath).click()
        time.sleep(3)
        if datatype == 'BIGINT':
            self.listitem = self.driver.find_element_by_xpath(self.lstitembigint_xpath)
        elif datatype == 'BIT':
            self.listitem = self.driver.find_element_by_xpath(self.lstitembit_xpath)
        elif datatype == 'NVARCHAR':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemnvarchar_xpath)

        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemdatetime_xpath)

        time.sleep(3)
        self.listitem.click()
        #self.driver.execute_script("arguments[0].click();", self.listitem)

    def setDataFormat(self, dataformat):
        self.driver.find_element_by_xpath(self.txtDataFormat_xpath).click()
        time.sleep(3)
        if dataformat == 'dd-mm-yyyy':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemDMY_xpath)
        elif dataformat == 'mm-dd-yyyy':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemMDY_xpath)


        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemYMDHMS_xpath)

        time.sleep(3)
        self.listitem.click()
        #self.driver.execute_script("arguments[0].click();", self.listitem)

    def clickFile2Table(self):
        self.driver.find_element_by_xpath(self.button_File2Table_xpath).click()

    def clickCleanseFile(self):
        self.driver.find_element_by_xpath(self.button_Cleansefile_xpath).click()

    def clickCleanse(self):
        self.driver.find_element_by_xpath(self.button_Cleanse_xpath).click()

    def clickAddColumn(self):
        self.driver.find_element_by_xpath(self.button_addcolumn_xpath).click()

    def setSearchColumn(self, search):
        self.driver.find_element_by_xpath(self.txt_searchcolumn_xpath).send_keys(search)

    def clickPrepexam1(self):
        self.driver.find_element_by_xpath(self.button_Prepexam1_xpath).click()

    def clickEmail(self):
        self.driver.find_element_by_xpath(self.button_Email_xpath).click()


    def clickAdd(self):
        self.driver.find_element_by_xpath(self.button_Add_xpath).click()

    def clickAddfunction(self):
        self.driver.find_element_by_xpath(self.button_Addfunction_xpath).click()

    def clickArithmatic(self):
        self.driver.find_element_by_xpath(self.button_Arithmatic_xpath).click()

    def clickConvert(self):
        self.driver.find_element_by_xpath(self.button_Convert_xpath).click()

    def clickOperator(self):
        self.driver.find_element_by_xpath(self.button_Operator_xpath).click()

    def clickADD(self):
        self.driver.find_element_by_xpath(self.button_ADD_xpath).click()

    def clickUpdate(self):
        self.driver.find_element_by_xpath(self.button_update_xpath).click()

    def clickPreviewicon(self):
        self.driver.find_element_by_xpath(self.button_previewicon_xpath).click()

    def clickPreviewclose(self):
        self.driver.find_element_by_xpath(self.button_previewclose_xpath).click()

    def clickLTRIM(self):
        self.driver.find_element_by_xpath(self.button_LTRIM_xpath).click()

    def clickRTRIM(self):
        self.driver.find_element_by_xpath(self.button_RTRIM_xpath).click()

    def clickRight(self):
        self.driver.find_element_by_xpath(self.button_RIGHT_xpath).click()

    def clickLeft(self):
        self.driver.find_element_by_xpath(self.button_Left_xpath).click()

    def clickLower(self):
        self.driver.find_element_by_xpath(self.button_Lower_xpath).click()

    def clickLength(self):
        self.driver.find_element_by_xpath(self.button_Length_xpath).click()

    def clickReverse(self):
        self.driver.find_element_by_xpath(self.button_Reverse_xpath).click()

    def clickUpper(self):
        self.driver.find_element_by_xpath(self.button_Upper_xpath).click()

    def clickTranslate(self):
        self.driver.find_element_by_xpath(self.button_Translate_xpath).click()

    def clickReplace(self):
        self.driver.find_element_by_xpath(self.button_Replace_xpath).click()

    def clickSubstring(self):
        self.driver.find_element_by_xpath(self.button_Substring_xpath).click()

    def clickStuff(self):
        self.driver.find_element_by_xpath(self.button_Stuff_xpath).click()

    def clickIsNull(self):
        self.driver.find_element_by_xpath(self.button_Isnull_xpath).click()

    def clickIsNumeric(self):
        self.driver.find_element_by_xpath(self.button_IsNumeric_xpath).click()

    def clickFormQuery(self):
        self.driver.find_element_by_xpath(self.button_FormQuery_Xpath).click()

    def clickCopyFormQuery(self):
        self.driver.find_element_by_xpath(self.button_CopyFormquery_xpath).click()

    def clickCloseFormQuery(self):
        self.driver.find_element_by_xpath(self.button_CloseformQuery_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))

    def searchByDataset(self,Dataset):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            Tablename = table.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/div/div[1]/table/tbody/tr["+str(r)+"]/td[1]").text
            if Tablename == Dataset:
                flag = True
                break
        return flag


    def searchLoginEmail_Contains(self,email):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            emailid = table.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/div/div[1]/table/tbody/tr["+str(r)+"]/td[1]").text
            if emailid == email:
                flag = True
                break
        return flag

    def setSearch(self,search):
        self.driver.find_element_by_xpath(self.txtsearch_xpath).send_keys(search)

    def clickSearch(self):
        self.driver.find_element_by_xpath(self.button_search_Xpath).click()