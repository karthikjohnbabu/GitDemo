import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
validateText= "Option3"
driver= webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_css_selector("#name").send_keys("Option3")
driver.find_element_by_id("alertbtn").click()
alert= driver.switch_to.alert
alertText = alert.text
assert validateText in alertText
print(alert.text)
alert.accept() # used to handle the pop ups for postive test cases like yes, ok , confirm
alert.dismiss()# used to handle the pop ups for negative test cases like no, cancel, dismiss.
