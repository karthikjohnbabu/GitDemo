import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe")
driver.get("https://www.makemytrip.com/")
driver.find_element_by_id("fromCity").click()
driver.find_element_by_xpath("//input[@placeholder='From']").send_keys("del")
time.sleep(3)
cities= driver.find_elements_by_css_selector("p[class*='blackText']")
print(len(cities))
for city in cities:
    if city.text=="Del Rio, United States":
        city.click()
        break

driver.find_element_by_xpath("//p[text()='Delhi, India']").click()
