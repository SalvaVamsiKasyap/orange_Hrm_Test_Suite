import pytest
from time import sleep

from _pytest.config import Config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



def pytest_addoption(parser):
    parser.addoption(
        "--browser_Name", action="store", default="chrome")




@pytest.fixture(scope="class")

def setup(request):
    browser_Name = request.config.getoption("browser_Name")
    if browser_Name == "chrome":
        service_obj = Service(r"C:\Users\Lenovo\PycharmProjects\SeleniumTest\Browsers\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        #driver.get("https://rahulshettyacademy.com/angularpractice/")
        #driver.get("https://www.myntra.com/")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
    elif browser_Name == "firefox":
        #service_obj = Service(r"C:\Users\Lenovo\PycharmProjects\SeleniumTest\Browsers\geckodriver.exe")
        driver = webdriver.Firefox()
        #driver.get("https://rahulshettyacademy.com/angularpractice/")
        #driver.get("https://www.myntra.com/")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
    elif browser_Name == "edge":
        service_obj = Service(r"C:\Users\Lenovo\PycharmProjects\SeleniumTest\Browsers\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
        #driver.get("https://rahulshettyacademy.com/angularpractice/")
        #driver.get("https://www.myntra.com/")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()

