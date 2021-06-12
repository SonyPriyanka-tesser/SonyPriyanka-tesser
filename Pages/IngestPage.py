import time


class IngestPage:
    button_ingest_xpath = "//div[@class='object-block ingest-btn tr-8']"
    #textbox_upload_xpath="//input[@type='file']"
    txtDelimiter_xpath = "//span[@class='multiselect__placeholder']"
    lstitemComma_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div[3]/ul/li[1]/span"
    lstitemColon_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div[3]/ul/li[2]/span"
    lstitem__Tab_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div[3]/ul/li[3]/span"
    lstitem_Pipe_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div[3]/ul/li[4]/span"

    txtDelimiter1_xpath = "//span[@class='multiselect__placeholder']"
    lstitemComma1_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[3]/ul/li[1]/span"
    lstitemColon1_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[3]/ul/li[2]/span"
    lstitem__Tab1_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[3]/ul/li[3]/span"
    lstitem_Pipe1_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[3]/ul/li[4]/span"

    txtDelimiter2_xpath = "//span[@class='multiselect__placeholder']"
    lstitemComma2_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div[3]/div/div[2]/div/div[3]/ul/li[1]/span"
    lstitemColon2_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div[3]/div/div[2]/div/div[3]/ul/li[2]/span"
    lstitem__Tab2_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div[3]/div/div[2]/div/div[3]/ul/li[3]/span"
    lstitem_Pipe2_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div[3]/div/div[2]/div/div[3]/ul/li[4]/span"

    img_Notification_xpath="// img[ @ name = 'notification-bell']"

    #Existing Convert to table
    checkbox_existingtable_xpath = "//input[@name='isExistingTable']"

    #ConvertToTable Page Locators:
    txtSchemaName_xpath = "//span[@class='multiselect__placeholder']"
    lstitemSandbox_xpath = "//span[contains(text(),'Sandbox')]"
    textbox_tablename_xpath="//input[@name='tableName']"

    txtLoadtype_xpath = "//span[@class='multiselect__placeholder']"
    lstitemCompleteRefresh_xpath = "//span[contains(text(),'Complete Refresh')]"
    lstitemIncrementLoad_xpath = "//span[contains(text(),'Incremental Load')]"
    lstitemappendonly_xpath = "//span[contains(text(),'Append Only')]"

    button_review_xpath ="//button[contains(text(), 'Review and convert ')]"

    #existing Table
    txtTablename_xpath = "//span[contains(text(),'Table name')]"
    lstitemFileToTable_xpath = "//span[contains(text(),'FileToTable')]"
    lstitemAnalyze_xpath = "//span[contains(text(),'Analyze')]"

    #Databases
    txtDatabase_xpath = "//span[@class='multiselect__placeholder']"
    lstitemAzureSQLDatabase_xpath = "//span[contains(text(),'Azure SQL Database')]"
    lstitemAzureSynapseAnalytics_xpath = "//span[contains(text(),'Azure Synapse Analytics')]"

    textbox_server_id = "serverName"
    textbox_portnumber_id = "portNumber"
    textbox_Database_id = "databaseName"
    textbox_user_id = "username"
    textbox_pwd_id = "password"
    button_connect_xpath = "//button[contains(text(),' Connect ')]"

    # Connected to Database Engine
    txtsourceschema_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/span/form/div/div[2]/div/div[2]/div[1]/div/div[2]/span"
    lstitemdbo_xpath = "//div[@class='border rounded ingest-database-body']/div[2]/div/div[2]/div[1]/div/div[3]/ul/li[1]/span"
    lstitemIncorpTax_xpath = "//span[contains(text(),'IncorpTax')]"
    lstitemBrightwing_xpath = "//span[contains(text(),'Brightwing')]"
    lstitemAppAdmin_xpath = "//span[contains(text(),'AppAdmin')]"

    txtsourcetable_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/span/form/div/div[2]/div/div[2]/div[2]/div/div[2]/span"
    lstitemti_dim_accountlets_xpath = "//div[@class='border rounded ingest-database-body']/div[2]/div/div[2]/div[2]/div/div[3]/ul/li[10]/span"
    lstitemtest111_ti_ITACustomerBusiness_xpath = "//div[@class='border rounded ingest-database-body']/div[2]/div/div[2]/div[2]/div/div[3]/ul/li[7]/span"
    lstitemti_AccountingDetails_xpath = "//div[@class='border rounded ingest-database-body']/div[2]/div/div[2]/div[2]/div/div[3]/ul/li[8]/span"
    lstitemti_Dashboard_Notes_xpath = "//div[@class='border rounded ingest-database-body']/div[2]/div/div[2]/div[2]/div/div[3]/ul/li[9]/span"

    txtTargetSchema_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/span/form/div/div[2]/div/div[3]/div[1]/div/div[2]/span"
    lstitemSandbox1_xpath = "//div[@class='border rounded ingest-database-body']/div[2]/div/div[3]/div[1]/div/div[3]/ul/li[1]/span"

    #Datatype navachar to navachar Validation-1st column paths
    txtDatatype_xpath ="/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div/table/thead/tr[1]/th[1]/div/div[2]/div[2]/span"
    lstitemInt_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div/table/thead/tr[1]/th[1]/div/div[2]/div[3]/ul/li[3]/span"
    lstitembigint_xpath ="/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div/table/thead/tr[1]/th[1]/div/div[2]/div[3]/ul/li[4]/span"
    lstitemnavachar_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div/table/thead/tr[1]/th[1]/div/div[2]/div[3]/ul/li[1]/span"
    lstitemdecimal_xpath= "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div/table/thead/tr[1]/th[1]/div/div[2]/div[3]/ul/li[1]/span"
    lstitemdatetime_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div/table/thead/tr[1]/th[1]/div/div[2]/div[3]/ul/li[6]/span"

    # Datatype INT to Happy Paths -2nd column
    txtDatatype1_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div/table/thead/tr[1]/th[2]/div/div[2]/div[2]/span"
    lstitemInt1_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div/table/thead/tr[1]/th[2]/div/div[2]/div[3]/ul/li[3]/span"
    lstitembigint1_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div/table/thead/tr[1]/th[2]/div/div[2]/div[3]/ul/li[4]/span"
    lstitemnavachar1_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div/table/thead/tr[1]/th[2]/div/div[2]/div[3]/ul/li[1]/span"
    lstitemdecimal1_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div/table/thead/tr[1]/th[2]/div/div[2]/div[3]/ul/li[5]/span"
    lstitemdatetime1_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div/table/thead/tr[1]/th[2]/div/div[2]/div[3]/ul/li[6]/span"

    # Datatype Datetime -6th column
    txtDatatype2_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div/table/thead/tr[1]/th[6]/div/div[2]/div[2]/span"
    lstitemInt2_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div/table/thead/tr[1]/th[6]/div/div[2]/div[3]/ul/li[3]/span"
    lstitembigint2_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div/table/thead/tr[1]/th[6]/div/div[2]/div[3]/ul/li[4]/span"
    lstitemnavachar2_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div/table/thead/tr[1]/th[6]/div/div[2]/div[3]/ul/li[1]/span"
    lstitemdecimal2_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div/table/thead/tr[1]/th[]/div/div[2]/div[3]/ul/li[5]/span"
    lstitembit2_xpath = "/html/body/div[2]/div[1]/div/div/div/div/div/div/div/div/table/thead/tr[1]/th[6]/div/div[2]/div[3]/ul/li[2]/span"

    def __init__(self,driver):
        self.driver=driver

    def clickIngest(self):
        self.driver.find_element_by_xpath(self.button_ingest_xpath).click()

    def setDelimiter(self, Delimiter):
        self.driver.find_element_by_xpath(self.txtDelimiter_xpath).click()
        time.sleep(3)
        if Delimiter == 'Comma':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemComma_xpath)
        elif Delimiter == 'Semi Colon':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemColon_xpath)
        elif Delimiter == 'Tab':

            self.listitem = self.driver.find_element_by_xpath(self.lstitem__Tab_xpath)

        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitem_Pipe_xpath)
        time.sleep(3)
        self.listitem.click()
        #self.driver.execute_script("arguments[0].click();", self.listitem)

    def setDelimiter1(self, Delimiter1):
        self.driver.find_element_by_xpath(self.txtDelimiter1_xpath).click()
        time.sleep(3)
        if Delimiter1 == 'Comma':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemComma1_xpath)
        elif Delimiter1 == 'Semi Colon':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemColon1_xpath)
        elif Delimiter1 == 'Tab':

            self.listitem = self.driver.find_element_by_xpath(self.lstitem__Tab1_xpath)

        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitem_Pipe1_xpath)
        time.sleep(3)
        self.listitem.click()
        #self.driver.execute_script("arguments[0].click();", self.listitem)

    def setDelimiter2(self, Delimiter2):
        self.driver.find_element_by_xpath(self.txtDelimiter2_xpath).click()
        time.sleep(3)
        if Delimiter2 == 'Comma':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemComma2_xpath)
        elif Delimiter2 == 'Semi Colon':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemColon2_xpath)
        elif Delimiter2 == 'Tab':

            self.listitem = self.driver.find_element_by_xpath(self.lstitem__Tab2_xpath)

        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitem_Pipe2_xpath)
        time.sleep(3)
        self.listitem.click()
        #self.driver.execute_script("arguments[0].click();", self.listitem)

    def clickNotificationBell(self):
        self.driver.find_element_by_xpath(self.img_Notification_xpath).click()

    def setSchemaName(self, SchemaName):
        self.driver.find_element_by_xpath(self.txtSchemaName_xpath).click()
        time.sleep(3)
        if SchemaName == 'Sandbox':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemSandbox_xpath)
        time.sleep(3)
        self.listitem.click()
        # self.driver.execute_script("arguments[0].click();", self.listitem)

    def setLoadType(self, LoadType):
        self.driver.find_element_by_xpath(self.txtLoadtype_xpath).click()
        time.sleep(3)
        if LoadType == 'Complete Refresh':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemCompleteRefresh_xpath)
        elif LoadType == 'Incremental Load':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemIncrementLoad_xpath)

        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemappendonly_xpath)
        time.sleep(3)
        self.listitem.click()
        #self.driver.execute_script("arguments[0].click();", self.listitem)

    def clickReviewandConvert(self):
        self.driver.find_element_by_xpath(self.button_review_xpath).click()



    def setTableName(self, Tablename):
        self.driver.find_element_by_xpath(self.txtSchemaName_xpath).click()
        time.sleep(3)
        if Tablename == 'FileToTable':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemFileToTable_xpath)

            time.sleep(3)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemAnalyze_xpath)
        time.sleep(3)
        self.listitem.click()
            # self.driver.execute_script("arguments[0].click();", self.listitem)

    def setDatabases(self, Databasetype):
        self.driver.find_element_by_xpath(self.txtDatabase_xpath).click()
        time.sleep(3)
        if Databasetype == 'Azure SQL Database':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemAzureSQLDatabase_xpath)
            time.sleep(3)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemAzureSynapseAnalytics_xpath)
        time.sleep(3)
        self.listitem.click()
            # self.driver.execute_script("arguments[0].click();", self.listitem)

    def setServer(self, server):
        self.driver.find_element_by_id(self.textbox_server_id).send_keys(server)

    def setPortNumber(self, portnumber):
        self.driver.find_element_by_id(self.textbox_portnumber_id).send_keys(portnumber)

    def setDatabaseName(self, Database):
        self.driver.find_element_by_id(self.textbox_Database_id).send_keys(Database)

    def setUser(self, user):
        self.driver.find_element_by_id(self.textbox_user_id).send_keys(user)

    def setPwd(self, pwd):
        self.driver.find_element_by_id(self.textbox_pwd_id).send_keys(pwd)

    def clickConnect(self):
        self.driver.find_element_by_xpath(self.button_connect_xpath).click()

    def setSourceSchema(self, sourceschema):
        self.driver.find_element_by_xpath(self.txtsourceschema_xpath).click()
        time.sleep(3)
        if sourceschema == 'dbo':
            self.driver.find_element_by_xpath(self.lstitemdbo_xpath)
        elif sourceschema == 'IncorpTax':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemIncorpTax_xpath)
        elif sourceschema == 'Brightwing':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemBrightwing_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemAppAdmin_xpath)
        time.sleep(3)
        self.listitem.click()



    def setSourceTable(self, sourcetable):
        self.driver.find_element_by_xpath(self.txtsourcetable_xpath).click()
        time.sleep(3)
        if sourcetable == 'ti_dim_accountlets':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemti_dim_accountlets_xpath)
        elif sourcetable == 'ti_AccountingDetails':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemti_AccountingDetails_xpath)
        elif sourcetable == 'ti_AccountingDetails':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemti_AccountingDetails_xpath)

        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemtest111_ti_ITACustomerBusiness_xpath)
        time.sleep(3)
        self.listitem.click()

    def setTargetSchema(self, targetschema):
        self.driver.find_element_by_xpath(self.txtTargetSchema_xpath).click()
        time.sleep(3)
        if targetschema == 'Sandbox':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemSandbox1_xpath)
        time.sleep(3)
        self.listitem.click()
        # self.driver.execute_script("arguments[0].click();", self.listitem)

    def setDatatypenvarchar(self, Datatype):
        self.driver.find_element_by_xpath(self.txtDatatype_xpath).click()
        time.sleep(3)
        if Datatype == 'int':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemInt_xpath)
        elif Datatype == 'decimal':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemdecimal_xpath)
        elif Datatype == 'nvarchar':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemnavachar_xpath)
        elif Datatype == 'datetime':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemdatetime_xpath)


        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitembigint_xpath)
        time.sleep(3)
        self.listitem.click()

    def setDatatypeInt_decimal(self, Datatype1):
        self.driver.find_element_by_xpath(self.txtDatatype1_xpath).click()
        time.sleep(3)
        if Datatype1 == 'int':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemInt1_xpath)
        elif Datatype1 == 'decimal':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemdecimal1_xpath)
        elif Datatype1 == 'nvarchar':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemnavachar1_xpath)
        elif Datatype1 == 'datetime':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemdatetime1_xpath)


        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitembigint1_xpath)
        time.sleep(3)
        self.listitem.click()

    def setDatatypeDateTime(self, Datatype2):
        self.driver.find_element_by_xpath(self.txtDatatype2_xpath).click()
        time.sleep(3)
        if Datatype2 == 'int':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemInt2_xpath)
        elif Datatype2 == 'decimal':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemdecimal2_xpath)
        elif Datatype2 == 'nvarchar':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemnavachar2_xpath)
        elif Datatype2 == 'bit':
            self.listitem = self.driver.find_element_by_xpath(self.lstitembit2_xpath)


        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitembigint2_xpath)
        time.sleep(3)
        self.listitem.click()