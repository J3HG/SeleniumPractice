from selenium.webdriver.support.wait import WebDriverWait

from PageObjectModel.HomePage import HomePage
import pytest
from selenium.webdriver.common.by import By
from PageObjectModel.RegisterPage import RegisterPage
from tests.conftest import setUpDriver
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setUpDriver")
class TestRegistration():
    def test_registerBtn(self):
        homePage = HomePage(self.driver)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(homePage.registerBtnLocator))
        homePage.registerBtn().click()

    def test_registerNewUser(self):
        registerPage = RegisterPage(self.driver)
        self.test_registerBtn()
        registerPage.firstName("Juan")
        registerPage.lastName("Pérez")
        registerPage.address("Noname St 26")
        registerPage.city("NoNameCity")
        registerPage.state("NoState")
        registerPage.zipcode("35682")
        registerPage.phone("5818638420")
        registerPage.ssn("225157856")

        registerPage.userName("userName01")
        registerPage.password("passcode01")
        registerPage.confirmPassword("passcode01")
        registerPage.registerBtn()

    def test_signUp(self):
        homePage = HomePage(self.driver)
        homePage.usernameField().send_keys("userName01")
        homePage.passwordField().send_keys("passcode01")
        homePage.loginBtn()