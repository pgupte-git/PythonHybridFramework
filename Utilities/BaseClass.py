import datetime
import random
import string
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")  # This we can use in all testcases as a baseclass
class BaseClass:

    def verifypagetitle(self,titletext):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.title_is(titletext))

    def waitfortextbox(self,textbox):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(textbox))

    def selectfromdropdown(self, locator, textvalue):
        sel = Select(locator)
        return sel.select_by_visible_text(textvalue)

    def randomdata_generator(self,size=8, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def random_string(self,size=6, chars=string.ascii_letters):
        return ''.join(random.choice(chars) for _ in range(size))
