from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
from PageObjectModel.HomeInternetPage import HomeInternetPage
from PageObjectModel.HomePage import HomePage
import pytest
from selenium.webdriver.common.by import By
from PageObjectModel.RegisterPage import RegisterPage
from tests.conftest import setUpDriverInternet
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setUpDriverInternet")
class TestAB():
    faker = Faker()
    def test_ABBtn(self):
        homeInternetPage = HomeInternetPage(self.driver)
        homeInternetPage.ABBtn().click()

    def test_addDeleteBtn(self):
        homeInternetPage = HomeInternetPage(self.driver)
        addPage = homeInternetPage.addDeleteBtn()
