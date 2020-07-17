import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

#@pytest.mark.usefixtures("setup")
from PytestFramework.pageObjects.CheckoutPage import CheckOutPage
from PytestFramework.pageObjects.HomePage import HomePage
from PytestFramework.utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self): #pytest method wrapped inside a class. This self keyword is used only when the method is inside the class.
        log = self.getLogger()
        homePage =HomePage(self. driver)
        checkoutPage= homePage.shopItems()
        log.info("Getting all the card titles")
        cards = checkoutPage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutPage.getCardFooter()[i].click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        confirmPage = checkoutPage.checkOutItems()
        log.info("Entering country name as India")
        self.driver.find_element_by_id("country").send_keys("ind")
        self.verifyLinkPresence("India")
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        successText = self.driver.find_element_by_class_name("alert-success").text
        log.info("Text received from application is "+ successText )
        assert "Success! Thank you! " in successText
