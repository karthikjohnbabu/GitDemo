from selenium import webdriver
from selenium.webdriver.support.select import Select
chrome_Options= webdriver.ChromeOptions()
chrome_Options.add_argument("--start-maximized")
chrome_Options.add_argument("headless")
chrome_Options.add_argument("--ignore-certificate-errors")
driver= webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe",options=chrome_Options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
