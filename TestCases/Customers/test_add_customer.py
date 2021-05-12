import time

import pytest

from TestData.AddCustomerData import AddCustomerData
from Configurations.readProperties import ReadConfig
from PageObjects.AddCustomerPage import AddCustomers
from PageObjects.LoginPage import LoginPage
from Utilities.BaseClass import BaseClass
from Utilities.customLogger import LogGen


class Test_Add_Customers(BaseClass):

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_add_cst(self, getData):
        logger = LogGen.getLogger()
        lp = LoginPage(self.driver)

        username = ReadConfig.getUsername()
        password = ReadConfig.getPassword()

        logger.info("******** Test003_Add_Customer *****")
        logger.info("Enter username")
        lp.enterusername(username)
        logger.info("Enter password")
        lp.enterpassword(password)
        logger.info("Click on Login button")
        lp.clickonloginbutton()
        time.sleep(3)
        act_title = self.driver.title
        print(act_title)

        if act_title == "Dashboard / nopCommerce administration":
            logger.info("Title is matched")
            assert True
        else:
            logger.error("Title is not matched")
            image_src = ReadConfig.getimagepath()

            if self.driver.save_screenshot(image_src + "test_logindemo.png") == True:
                logger.info("Screenshot saved")
            else:
                logger.error("Screenshot not saved")
            assert False

        cstpage = AddCustomers(self.driver)

        logger.info("Click on Customer option")
        cstpage.Click_On_Customers()
        logger.info("click on customer list option")
        cstpage.Click_On_Customer_List_Page()
        time.sleep(3)
        logger.info("Click on Add customer button")
        cstpage.Click_On_Add_Customer()

        logger.info("Enter the customer information")
        time.sleep(3)
        email = self.randomdata_generator() + "@mailinator.com"
        cstpage.enter_EmailID(email)
        logger.info("Enter user email id")

        cstpage.enter_Password(getData["password"])
        logger.info("Enter user password")

        cstpage.enter_firstname(getData["firstname"])
        logger.info("Enter firstname")

        cstpage.enter_lastname(getData["lastname"])
        logger.info("Enter lastname")

        cstpage.select_gender(getData["gender"])
        logger.info("Enter gender")

        cstpage.enter_dob(getData["dob"])
        logger.info("Enter dob")

        cstpage.enter_companyname(getData["compname"])
        logger.info("Enter company name")

        cstpage.click_tax_exempt_checkbox()
        logger.info("Tax exempt checkbox is checked")

        cstpage.set_newsLetter(getData["newsletter"])
        logger.info("Enter newsletter")
        time.sleep(3)

        cstpage.set_CustomerRole(getData["custrole"])
        logger.info("Enter custrole")

        # select from dropdown
        self.selectfromdropdown(cstpage.set_vendors(), getData["managerVendor"])
        logger.info("Selected vendor role")

        cstpage.click_on_savebutton()
        logger.info("clicked on the save button")
        time.sleep(2)
        print(cstpage.get_successmsg())
        if "The new customer has been added successfully." in cstpage.get_successmsg():
            assert True == True
            logger.info("Customer is added successfully")

        else:
            image_src = ReadConfig.getimagepath()

            if self.driver.save_screenshot(image_src + "test_Customer_not_added.png") == True:
                logger.info("Screenshot saved")
            else:
                logger.error("Screenshot not saved")
            assert True == False



    @pytest.fixture(params=AddCustomerData.test_add_cst_reg_data)
    def getData(self, request):
        return request.param
