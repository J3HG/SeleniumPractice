import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class HomeInternetPage():
    def __init__(self, driver):
        self.driver = driver

    #We define the locators
    abTestingBtnLocator = (By.LINK_TEXT, "A/B Testing")
    addDeleteBtnLocator = (By.LINK_TEXT, "Add/Remove Elements")

    #We define the methods
    def ABBtn(self):
        return self.driver.find_element(*self.abTestingBtnLocator)

    def addDeleteBtn(self):
        return self.driver.find_element(*self.addDeleteBtnLocator).click()