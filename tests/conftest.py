import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setUpDriver(request):
    service_obj = Service("C:\\Users\\mari_\\Downloads\\chromedriver-win64_current\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture(scope="class")
def setUpDriver2(request):
    service_obj = Service("C:\\Users\\mari_\\Downloads\\chromedriver-win64_current\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture()
def setUpDriverInternet(request):
    service_obj = Service("C:\\Users\\mari_\\Downloads\\chromedriver-win64_current\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://the-internet.herokuapp.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()