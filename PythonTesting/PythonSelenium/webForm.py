import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe")
driver.get("https://formy-project.herokuapp.com/form")
driver.find_element_by_id("first-name").send_keys("Karthik")
driver.find_element_by_id("last-name").send_keys("Babu")
driver.find_element_by_id("job-title").send_keys("Automation Engineer")
driver.find_element_by_id("radio-button-3").click()
driver.find_element_by_id("checkbox-1").click()
dropdown=Select(driver.find_element_by_id("select-menu"))
dropdown.select_by_index(3)
datebox= driver.find_element_by_id("datepicker")
datebox.send_keys("06222020")
datebox.send_keys(Keys.TAB)
driver.find_element_by_link_text("Submit").click()
time.sleep(3)
message =driver.find_element_by_xpath("//*[@role='alert']").text
#assertions are nothing but which will look for expected values or it expects always true.
assert"success" in message # checking the substring present in the main string or not.

