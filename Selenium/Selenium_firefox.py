import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.facebook.com/")
Email = driver.find_element(By.NAME,"email")

print(driver.title)
print(driver.current_url)
print(type(driver))
driver.quit()