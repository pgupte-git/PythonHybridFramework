import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import Utilities


class AddCustomers:

    # locators for customer page
    customer_option = (By.XPATH, "//a[@href='#']/p[contains(text(),'Customers')]")
    customerpage_option = (By.XPATH, "//a[@href='/Admin/Customer/List']/p[contains(text(),'Customers')]")
    add_new_cst = (By.CSS_SELECTOR, "a[class='btn btn-primary']")
    successmessage = (By.CSS_SELECTOR, "div[class*='alert-success']")

    # form fields locators
    email_input = (By.XPATH, "//input[@id='Email']")
    password_input = (By.XPATH, "//input[@id='Password']")
    firstname_input = (By.XPATH, "//input[@id='FirstName']")
    lastname_input = (By.XPATH, "//input[@id='LastName']")
    radio_button_male = (By.XPATH, "//input[@id='Gender_Male']")
    radio_button_female = (By.XPATH, "//input[@id='Gender_Female']")
    dob_input = (By.XPATH, "//input[@id='DateOfBirth']")
    companyname = (By.XPATH, "//input[@id='Company']")
    tax_exempt_checkbox = (By.XPATH, "//input[@id='IsTaxExempt']")

    newsletter_input = (By.XPATH, "//div[@class='input-group-append']//input[@role='listbox']")
    newslett_your_store = (By.XPATH, "//li[normalize-space()='Your store name']")
    newslett_test_store = (By.XPATH, "//li[normalize-space()='Test store 2']")

    customer_roles = (By.XPATH, "//div[@class='input-group-append input-group-required']//input[@role='listbox']")
    customer_administrator_option = (By.XPATH, "//li[normalize-space()='Administrators']")
    customer_moderator_option = (By.XPATH, "//li[normalize-space()='Forum Moderators']")
    customer_guest_option = (By.XPATH, "//li[normalize-space()='Guests']")
    customer_register_option = (By.XPATH, "//li[normalize-space()='Registered']")
    customer_vendors_option = (By.XPATH, "//li[normalize-space()='Vendors']")
    customer_role_only_one_option = (By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li[1]//span[2]")

    manager_of_vendor_selectdropdown = (By.XPATH, "//select[@id='VendorId']")
    active_checkbox = (By.XPATH, "//input[@id='Active']")
    admin_comment_input = (By.XPATH, "//input[@id='AdminComment']")
    savebutton = (By.XPATH, "//button[@name='save']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # methods to perform actions
    def Click_On_Customers(self):
        return self.driver.find_element(*AddCustomers.customer_option).click()

    def Click_On_Customer_List_Page(self):
        return self.driver.find_element(*AddCustomers.customerpage_option).click()


    def Click_On_Add_Customer(self):
        return self.driver.find_element(*AddCustomers.add_new_cst).click()

    def enter_EmailID(self, email):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='Email']")))
        return self.driver.find_element(*AddCustomers.email_input).send_keys(email)

    def enter_Password(self, password):
        return self.driver.find_element(*AddCustomers.password_input).send_keys(password)

    def enter_firstname(self, fname):
        return self.driver.find_element(*AddCustomers.firstname_input).send_keys(fname)

    def enter_lastname(self, lname):
        return self.driver.find_element(*AddCustomers.lastname_input).send_keys(lname)

    def select_gender(self, gender):
        if gender == "Male":
            return self.driver.find_element(*AddCustomers.radio_button_male).click()
        elif gender == "Female":
            return self.driver.find_element(*AddCustomers.radio_button_female).click()
        else:
            return self.driver.find_element(*AddCustomers.radio_button_male).click()

    def enter_dob(self, dob):
        return self.driver.find_element(*AddCustomers.dob_input).send_keys(dob)

    def enter_companyname(self, cmpyname):
        return self.driver.find_element(*AddCustomers.companyname).send_keys(cmpyname)

    def click_tax_exempt_checkbox(self):
        return self.driver.find_element(*AddCustomers.tax_exempt_checkbox).click()

    def set_CustomerRole(self, role):
        self.driver.find_element(*AddCustomers.customer_roles).click()
        time.sleep(3)

        if role == "Registered":
            self.listitem = self.driver.find_element(*AddCustomers.customer_register_option)

        elif role == "Administrators":
            self.listitem = self.driver.find_element(*AddCustomers.customer_administrator_option)

        elif role == "Forum Moderators":
            self.listitem = self.driver.find_element(*AddCustomers.customer_moderator_option)

        elif role == "Guests":
            time.sleep(3)
            # here user can be register as Guest or Registered user, so we have to select one option
            self.driver.find_element(*AddCustomers.customer_role_only_one_option).click()
            self.listitem = self.driver.find_element(*AddCustomers.customer_guest_option)

        elif role == "Vendors":
            self.listitem = self.driver.find_element(*AddCustomers.customer_vendors_option)

        else:
            self.listitem = self.driver.find_element(*AddCustomers.customer_guest_option)

        time.sleep(4)
        return self.driver.execute_script("arguments[0].click();", self.listitem)

    def set_newsLetter(self, newsletter):

        self.newsoption = self.driver.find_element(*AddCustomers.newsletter_input).click()
        time.sleep(3)

        if newsletter == "Your store name":
            self.newsoption = self.driver.find_element(*AddCustomers.newslett_your_store)

        elif newsletter == "Test store 2":
            self.newsoption = self.driver.find_element(*AddCustomers.newslett_test_store)

        time.sleep(2)
        return self.driver.execute_script("arguments[0].click();", self.newsoption)

    def set_vendors(self):
        return self.driver.find_element(*AddCustomers.manager_of_vendor_selectdropdown)

    def click_on_savebutton(self):
        return self.driver.find_element(*AddCustomers.savebutton).click()

    def get_successmsg(self):
        return self.driver.find_element(*AddCustomers.successmessage).text


