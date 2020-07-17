from selenium.webdriver.common.by import By

from PytestFramework.pageObjects.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR,"a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    check = (By.ID,"exampleCheck1")
    gender = (By.ID,"exampleFormControlSelect1")
    submit = (By.XPATH,"//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR,"[class*='alert-success']")




    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click() #this code is same as below line of code, the * deserialize the tuple
        #self.driver.find_element_by_css_selector("a[href*='shop']").click()
        checkoutPage = CheckOutPage(self.driver)
        return checkoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.check)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)

