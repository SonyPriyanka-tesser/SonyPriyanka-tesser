import time
import unittest
import HtmlTestRunner
from selenium import webdriver


import sys
sys.path.append("/")
from Pages.LoginPage import LoginPage

class LoginTest(unittest.TestCase):
    baseURL = "https://login.microsoftonline.com/common/oauth2/v2.0/authorize?response_type=id_token&scope=https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi%2Fapp.read.all%20https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi%2Fcapacity.read.all%20https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi%2Fcapacity.readwrite.all%20https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi%2Fcontent.create%20https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi%2Fdashboard.read.all%20https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi%2Fdashboard.readwrite.all%20https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi%2Fdata.alter_any%20https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi%2Fdataflow.read.all%20https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi%2Fdataflow.readwrite.all%20https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi%2Fdataset.read.all%20https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi%2Fdataset.readwrite.all%20https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi%2Fgateway.read.all%20https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi%2Fgateway.readwrite.all%20https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi%2Fgroup.read%20https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi%2Fgroup.read.all%20https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi%2Fmetadata.view_any%20https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi%2Freport.read.all%20https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi%2Freport.readwrite.all%20https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi%2Fstorageaccount.read.all%20https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi%2Fstorageaccount.readwrite.all%20https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi%2Ftenant.read.all%20https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi%2Ftenant.readwrite.all%20https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi%2Fworkspace.read.all%20https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi%2Fworkspace.readwrite.all%20openid%20profile&client_id=77cfc3e0-190e-4bb9-b398-a541b574e325&redirect_uri=https%3A%2F%2Ftiplatform-uat.azurewebsites.net%2FloginSuccess&state=eyJpZCI6IjcxMzdjNGRlLTlkMjItNGY0Yy05NDEwLTVmMDYzMDJkMjVhZCIsInRzIjoxNjIxMjcxNDMyLCJtZXRob2QiOiJwb3B1cEludGVyYWN0aW9uIn0%3D&nonce=a12d35f9-4b7c-4f03-9a7e-332996a5529c&client_info=1&x-client-SKU=MSAL.JS&x-client-Ver=1.4.3&client-request-id=1e180f4b-28a1-412d-a562-8f27af9520d0&response_mode=fragment&sso_reload=true"
    driver = webdriver.Chrome(executable_path="/Drivers/chromedriver.exe")
    username = "sony@tesserinsights.com"
    password = "Tesseroffice1$$"

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp=LoginPage(self.driver)
        #lp.clickSignIn()

        lp.setUserName(self.username)
        lp.clickNext()
        time.sleep(5)

        lp.setPassword(self.password)
        lp.clickPswdSignIn()
        time.sleep(5)
        lp.clickYes()
        time.sleep(5)
        self.driver.get("https://tiplatform-uat.azurewebsites.net/")
        lp.clickSignIn()
        time.sleep(10)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        self.assertEqual("Tesser Pro",self.driver.title,"not matched title")


if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\sonup\\PycharmProjects\\Project\\Reports'))



