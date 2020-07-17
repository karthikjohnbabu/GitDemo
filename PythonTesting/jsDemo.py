#JS DOM can access any elements on web page just like how selenium does.
#selenium have a method to execute javascrit code in it.
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
driver= webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("hello")
print(driver.find_element_by_name("name").text) # this will not work in selenium.
print(driver.find_element_by_name("name").get_attribute("value"))
#purely using Javascript.
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

shopButton= driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();", shopButton)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")