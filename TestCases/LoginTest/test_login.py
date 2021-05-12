import os

import pytest

from Utilities.BaseClass import BaseClass
from PageObjects.LoginPage import LoginPage
from Configurations.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class Test_Login(BaseClass):

    @pytest.mark.regression
    def test_homepageTitle(self):
        logger = LogGen.getLogger()
        logger.info("******** Test001Login *****")
        logger.info("********* Started *********")
        logger.info("Get the title")
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
        else:
            image_src = ReadConfig.getimagepath()
            self.driver.save_screenshot(image_src + "test_homepage.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_logindemo(self):
        lp = LoginPage(self.driver)
        logger = LogGen.getLogger()

        username = ReadConfig.getUsername()
        password = ReadConfig.getPassword()

        logger.info("Enter Username")
        lp.enterusername(username)
        logger.info("Enter Password")
        lp.enterpassword(password)
        logger.info("Click on login button")
        lp.clickonloginbutton()
        act_title = self.driver.title
        lp.clickonlogoutbutton()
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
