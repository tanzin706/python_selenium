import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options= chrome_options)

driver.maximize_window()
print(type(driver))
driver.get("https://icehrm-open.gamonoid.com/login.php")

# forgotLink = driver.find_element(By.PARTIAL_LINK_TEXT,"Reset")
# forgotLink.click()

mylinks = driver.find_element(By.TAG_NAME,"a")
print(mylinks.get_attribute("outerHTML"))

time.sleep(5)
driver.quit()