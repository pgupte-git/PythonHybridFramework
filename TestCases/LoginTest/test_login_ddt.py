import time

import pytest

from TestData.ReadLoginData import ReadLoginData
from Utilities.BaseClass import BaseClass
from PageObjects.LoginPage import LoginPage
from Configurations.readProperties import ReadConfig
from Utilities import XlsUtil
from Utilities.customLogger import LogGen


class Test_login_ddt(BaseClass):
    logger = LogGen.getLogger()
    # xls_path = "D://Udmey//Python-Workspace//PythonHybridFramework//TestData//Test_Input_data.xlsx"

    @pytest.mark.regression
    def test_login_data_driven(self):

        lp = LoginPage(self.driver)
        xls_path = ReadConfig.get_xls_file()
        list_data = []

        self.logger.info("#### Test case DDT 002 #####")
        self.logger.info("#### Verify the login with data driven test ##########")
        rows = XlsUtil.getrowcount(xls_path, 'LoginData')
        columns = XlsUtil.getcolumncount(xls_path, 'LoginData')
        print("Number of rows in a active sheet are", rows)
        print("Number of columns in a active sheet are", columns)

        # Logic to read the data from excel sheet we need to use two for loops one for row and one for column
        for r in range(2, rows + 1):
            username = XlsUtil.readData(xls_path,r,1,'LoginData')
            password = XlsUtil.readData(xls_path,r,2,'LoginData')
            result = XlsUtil.readData(xls_path,r,3,'LoginData')

            self.logger.info("Enter Username")
            lp.enterusername(username)
            self.logger.info("Enter Password")
            lp.enterpassword(password)

            self.logger.info("Click on login button")
            lp.clickonloginbutton()
            self.verifypagetitle(self.driver.title)

            act_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"

            if act_title == expected_title:
                if result == "Pass":
                    self.logger.info("Title is matched")
                    assert True
                    self.logger.info("Click on logout button")
                    lp.clickonlogoutbutton()
                    list_data.append("Pass")

                elif result == "Fail":
                    self.logger.error("Title is not matched")
                    self.logger.info("Click on logout button")
                    lp.clickonlogoutbutton()
                    list_data.append("Fail")
                    image_src = ReadConfig.getimagepath()
                    if self.driver.save_screenshot(image_src + "test_login_data_driven.png"):
                        self.logger.info("Screenshot saved")
                    else:
                        self.logger.error("Screenshot not saved")
                        assert False
            elif act_title != expected_title:
                if result == "Pass":
                    self.logger.error("Testcase failed")
                    self.logger.info("Click on logout button")
                    lp.clickonlogoutbutton()
                    list_data.append("Fail")
                elif result == "Fail":
                    self.logger.error("Testcase Passed")
                    list_data.append("Pass")

        if "Fail" not in list_data:
            self.logger.info("###### Login Test Data testcase is Passed")
            assert True
        else:
            self.logger.info("### Login Test Data testcase is failed")
            assert False

        self.logger.info("########### End of Login Testcase###############")






'''
@pytest.fixture(params=ReadLoginData.getlogindata())
def getData(request):
    return request.param
'''

