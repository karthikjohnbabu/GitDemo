from selenium import webdriver
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Karthik Babu")
driver.find_element_by_name("email").send_keys("karthik.babu@gmail.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("Passw0rd")
driver.find_element_by_id("exampleCheck1").click()
#select class provides the methods to handle the options in dropdown.
dropdown= Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
driver.find_element_by_xpath("//input[@type='submit']").click()
message= driver.find_element_by_class_name("alert-success").text
#assertions are nothing but which will look for expected values or it expects always true.
assert"success" in message # checking the substring present in the main string or not.
