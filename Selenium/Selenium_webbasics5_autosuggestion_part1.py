import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options= chrome_options)

driver.maximize_window()
driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-autocomplete-feature-in.html")
driver.implicitly_wait(20)
driver.find_element(By.ID,"tags").send_keys("S")
listElements = driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']//div")

print("Total number of list elements",len(listElements))

for ele in listElements:
    print(ele.text)
    if ele.text=="Selenium":
        ele.click()
        print("Record Found")
        break