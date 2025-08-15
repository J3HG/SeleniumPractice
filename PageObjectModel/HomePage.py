import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    registerBtnLocator = (By.LINK_TEXT, "Register")
    usernameLocator = (By.XPATH, "//input[@name='username']")
    passwordLocator = (By.XPATH, "//input[@name='password']")
    loginBtnLocator = (By.XPATH, "//input[@type='submit']")
    aboutUsLocator = (By.LINK_TEXT, "About Us")
    servicesLocator = (By.LINK_TEXT, "Services")
    productsLocator = (By.LINK_TEXT, "Products")
    locationsLocator = (By.LINK_TEXT, "Locations")
    adminPageLocator = (By.LINK_TEXT, "Admin Page")
    homePageLocator = (By.XPATH, "//a[text()='Home']")

    def registerBtn(self):
        return self.driver.find_element(*HomePage.registerBtnLocator)

    def usernameField(self):
        return self.driver.find_element(*HomePage.usernameLocator)

    def passwordField(self):
        return self.driver.find_element(*HomePage.passwordLocator)

    def loginBtn(self):
        return self.driver.find_element(*HomePage.loginBtnLocator).click()

    def aboutUsBtn(self):
        return self.driver.find_element(*HomePage.aboutUsLocator).click()

    def servicesBtn(self):
        return self.driver.find_element(*HomePage.servicesLocator).click()

    def productsBtn(self):
        return self.driver.find_element(*HomePage.productsLocator).click()

    def locationsBtn(self):
        return self.driver.find_element(*HomePage.locationsLocator).click()

    def adminPage(self):
        return self.driver.find_element(*HomePage.adminPageLocator).click()

    def homePageBtn(self):
        return self.driver.find_element(*HomePage.homePageLocator).click()