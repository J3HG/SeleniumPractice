import pytest
from selenium.webdriver.common.by import By

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    firstNameLocator = (By.ID, 'customer.firstName')
    lastNameLocator = (By.ID, 'customer.lastName')
    addressLocator = (By.ID, 'customer.address.street')
    cityLocator = (By.ID, 'customer.address.city')
    stateLocator = (By.ID, 'customer.address.state')
    zipcodeLocator = (By.ID, 'customer.address.zipCode')
    phoneLocator = (By.ID, 'customer.phoneNumber')
    ssnLocator = (By.ID, 'customer.ssn')
    userNameLocator = (By.ID, 'customer.username')
    passwordLocator = (By.ID, 'customer.password')
    confirmPasswordLocator = (By.ID, 'repeatedPassword')
    registerBtnLocator = (By.XPATH, "//input[@value='Register']")

    def firstName(self, name):
        return self.driver.find_element(*self.firstNameLocator).send_keys(name)

    def lastName(self, lastName):
        return self.driver.find_element(*self.lastNameLocator).send_keys(lastName)

    def address(self, address):
        return self.driver.find_element(*self.addressLocator).send_keys(address)

    def city(self, city):
        return self.driver.find_element(*self.cityLocator).send_keys(city)

    def state(self, state):
        return self.driver.find_element(*self.stateLocator).send_keys(state)

    def zipcode(self, zipcode):
        return self.driver.find_element(*self.zipcodeLocator).send_keys(zipcode)

    def phone(self, phone):
        return self.driver.find_element(*self.phoneLocator).send_keys(phone)

    def ssn(self, ssn):
        return self.driver.find_element(*self.ssnLocator).send_keys(ssn)

    def userName(self, userName):
        return self.driver.find_element(*self.userNameLocator).send_keys(userName)

    def password(self, password):
        return self.driver.find_element(*self.passwordLocator).send_keys(password)

    def confirmPassword(self, repeatedPassword):
        return self.driver.find_element(*self.confirmPasswordLocator).send_keys(repeatedPassword)

    def registerBtn(self):
        return self.driver.find_element(*self.registerBtnLocator).click()