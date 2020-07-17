import time

from selenium import webdriver
driver= webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe")
driver.get("https://login.salesforce.com/?locale=in")
time.sleep(2)
driver.find_element_by_css_selector("#username").send_keys("babu")
time.sleep(2)
driver.find_element_by_css_selector(".password").send_keys("karthik")
time.sleep(2)
driver.find_element_by_css_selector(".password").clear()
time.sleep(2)
driver.find_element_by_link_text("Forgot Your Password?").click()
time.sleep(2)
#//tagname[text()='xxx']
driver.find_element_by_xpath("//a[text()='Cancel']").click()
time.sleep(2)
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(4)").text)
driver.quit()