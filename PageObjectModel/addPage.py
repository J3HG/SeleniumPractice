from selenium.webdriver.common.by import By

class addPage():
    def __init__(self, driver):
        self.driver = driver

    #We define the locators
    addBtnLocator = (By.XPATH, "//button[@onclick='addElement()']")

    #We define methods
    def addElementBtn(self):
        return self.driver.find_element(*self.addBtnLocator).click()