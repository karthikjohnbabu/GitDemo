from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/iframe")
#frameID or FrameName or Index value
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("I am able to automate")
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)