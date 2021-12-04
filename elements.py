from selenium import webdriver
url="http://cookbook.seleniumacademy.com/Config.html"
driver = webdriver.Edge("../resources/msedgedriver.exe")
driver.maximize_window()
driver.get(url)

if element_airbags.is_selected():
    elelment_airbags.click()



driver.find_element_by_name()
driver.find_element_by_id()
driver.find_element_by_class_name()
driver.find_element_by_link_text()
driver.find_element_by_css_selector()
driver.find_element_by_xpath()
driver.find_element_by_tag_name()
driver.find_element_by_partial_link_text()
driver.find_elements_by_tag_name()
