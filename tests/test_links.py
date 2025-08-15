from selenium.webdriver.support.wait import WebDriverWait

from PageObjectModel.HomePage import HomePage
import pytest
from selenium.webdriver.common.by import By
from PageObjectModel.RegisterPage import RegisterPage
from tests.conftest import setUpDriver
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setUpDriver2")
class TestLinks():
    def test_aboutUs(self):
        homePage = HomePage(self.driver)
        homePage.aboutUsBtn()
        assert self.driver.find_element(By.XPATH, "//h1[@class='title']").text == "ParaSoft Demo Website"

    def test_services(self):
        homePage = HomePage(self.driver)
        homePage.servicesBtn()
        titles = self.driver.find_elements(By.XPATH, "//span[@class='heading']")
        for title in titles:
            titleName = title.text
            if titleName == "Available Bookstore SOAP services:":
                assert titleName == "Available Bookstore SOAP services:"
            else:
                pass
    def test_products(self):
        homePage = HomePage(self.driver)
        homePage.productsBtn()
        self.driver.back()

    def test_locations(self):
        homePage = HomePage(self.driver)
        homePage.locationsBtn()
        self.driver.back()

    def test_adminPage(self):
        homePage = HomePage(self.driver)
        homePage.adminPage()