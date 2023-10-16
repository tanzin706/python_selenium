import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options= chrome_options)

print(type(driver))
driver.get("https://www.google.com")
mypagetitle=driver.title
print(mypagetitle)
assert "Google" in mypagetitle
search_box=driver.find_element(By.ID,value="APjFqb")
search_box.send_keys("pycharm")
time.sleep(3)
driver.quit()


