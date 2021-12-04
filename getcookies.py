from selenium import webdriver
driver = webdriver.Edge("../resources/msedgedriver.exe")
driver.get("http://cookbook.seleniumacademy.com/Config.html")

print("ALL COOKIES",driver.get_cookies())
driver.delete_all_cookies()
print("ALL COOKIES",driver.get_cookies())
print("Page source(length)",len(driver.page_source))
driver.close()
