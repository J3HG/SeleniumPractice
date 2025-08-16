import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ForgotInfoPage:
    def __init__(self, driver):
        self.driver = driver

    #We define locators
    firstNameLtr = (By.ID, "firstName")
    lastNameLtr = (By.ID, "lastName")
    addressLtr = (By.ID, "address.street")
    cityLtr = (By.ID, "address.city")
    stateLtr = (By.ID, "address.state")
    zipCodeLtr = (By.ID, "address.zipCode")
    ssnLtr = (By.ID, "ssn")
    FindMyInfoBtnLtr = (By.XPATH, "//input[@value='Find My Login Info']")

    def firstName(self):
        return self.driver.find_element(*ForgotInfoPage.firstNameLtr).send_keys("noName")

    def lastName(self):
        return self.driver.find_element(*ForgotInfoPage.lastNameLtr).send_keys("noLastName")

    def address(self):
        return self.driver.find_element(*ForgotInfoPage.addressLtr).send_keys("noAddress")

    def city(self):
        return self.driver.find_element(*ForgotInfoPage.cityLtr).send_keys("noCity")

    def state(self):
        return self.driver.find_element(*ForgotInfoPage.stateLtr).send_keys("noState")

    def zipCode(self):
        return self.driver.find_element(*ForgotInfoPage.zipCodeLtr).send_keys("noZipCode")

    def ssn(self):
        return self.driver.find_element(*ForgotInfoPage.ssnLtr).send_keys("noSSN")

    def findMyInfoBtn(self):
        return self.driver.find_element(*ForgotInfoPage.FindMyInfoBtnLtr).click()