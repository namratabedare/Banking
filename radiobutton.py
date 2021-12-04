import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Edge("../resources/msedgedriver.exe")
url = "http://cookbook.seleniumacademy.com/Config.html"
driver.get(url)

expression = " input[value='petrol']"
element_petrol=driver.find_element_by_css_selector("input[value='Diesel']")
element_diesel=driver.find_element_by_css_selector("input[value='Petrol']")

if not element_petrol.is_selected():
    element_petrol.click()
else:
    element_diesel.click()
time.sleep(5)

