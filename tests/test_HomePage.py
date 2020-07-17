import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from PytestFramework.TestData.HomePageData import HomePageData
from PytestFramework.pageObjects.HomePage import HomePage
from PytestFramework.utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

     def test_formSubmussion(self,getData):
         log = self.getLogger()
         homepage = HomePage(self.driver)
         log.info("First name is"+getData["firstname"])
         homepage.getName().send_keys(getData["firstname"])
         homepage.getEmail().send_keys(getData["lastname"])
         homepage.getCheckBox().click()
         self.selectOptionByText(homepage.getGender(),getData["gender"])
         homepage.submitForm().click()
         alertText = homepage.getSuccessMessage().text
         assert ("Success"in alertText)
         self.driver.refresh()

     @pytest.fixture(params= HomePageData.getTestData("Testcase2"))
     def getData(self, request):
         return request.param