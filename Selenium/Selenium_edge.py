import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://learn-automation.com/")
print(driver.title)
print(driver.current_url)
print(type(driver))
driver.quit()