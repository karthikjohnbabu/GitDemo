from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe")
driver.get("https://www.familysearch.org/en/")

#ActionChains
action= ActionChains(driver)
action.move_to_element(driver.find_element_by_id("search")).perform()
action.move_to_element(driver.find_element_by_link_text("Genelogies")).click().perform()
