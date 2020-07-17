from selenium import webdriver
#every browser exposes an executable file
#through selenium test we need to invoke the executable file which will then invoke actual browser.
#driver= webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe")
driver= webdriver.Firefox(executable_path="C:\work\geckodriver-v0.26.0-win64\geckodriver.exe")
#driver= webdriver.Ie(executable_path="C:\work\IEDriverServer_x64_3.150.1\IEDriverServer.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/#/index")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.back()
driver.refresh()
driver.close() # only the current window will be closed
driver.quit() #all the w
# indows will be closed