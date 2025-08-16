from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker

from PageObjectModel.ForgotInfoPage import ForgotInfoPage
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
        fake = Faker()
        registerPage = RegisterPage(self.driver)
        self.test_registerBtn()
        registerPage.firstName(fake.first_name())
        registerPage.lastName(fake.last_name())
        registerPage.address(fake.address())
        registerPage.city(fake.city())
        registerPage.state(fake.state())
        registerPage.zipcode(fake.zipcode())
        registerPage.phone(fake.phone_number())
        registerPage.ssn(fake.ssn())

        registerPage.userName(fake.user_name())
        registerPage.password("passcode01")
        registerPage.confirmPassword("passcode01")
        registerPage.registerBtn()

    def test_signUp(self):
        homePage = HomePage(self.driver)
        homePage.usernameField().send_keys("username1600")
        homePage.passwordField().send_keys("username1600")
        homePage.loginBtn()

    def test_billPay(self):
        homePage = HomePage(self.driver)
        forgotInfoPage = ForgotInfoPage(self.driver)
        homePage.forgotLoginInfoBtn()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.driver.find_element(By.XPATH, "//input[@value='Find My Login Info']")))

        forgotInfoPage.firstName()
        forgotInfoPage.lastName()
        forgotInfoPage.address()
        forgotInfoPage.city()
        forgotInfoPage.state()
        forgotInfoPage.zipCode()
        forgotInfoPage.ssn()
        forgotInfoPage.findMyInfoBtn()