import pytest
import time
from selenium import webdriver
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
@pytest.fixture(scope= "class")
def setup(request):
    global driver
    browser_name= request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\work\geckodriver-v0.26.0-win64\geckodriver.exe")
    elif browser_name == "IE":
        driver = webdriver.Ie(executable_path="C:\work\IEDriverServer_x64_3.150.1\IEDriverServer.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

