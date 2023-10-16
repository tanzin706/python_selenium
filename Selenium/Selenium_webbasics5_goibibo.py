import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options= chrome_options)

driver.maximize_window()
driver.get("https://www.goibibo.com")
driver.implicitly_wait(20)
driver.find_element(By.XPATH,"//span[@role='presentation']").click()
driver.find_element(By.XPATH,"//p[@class='sc-12foipm-20 bhnHeQ']").click()
driver.find_element(By.XPATH,"//div[@class='sc-12foipm-38 dAUhfz']//input").send_keys("Be")
listElements = driver.find_elements(By.XPATH,"//li[@role='presentation']//span[@class='autoCompleteTitle ']")
driver.find_element(By.XPATH,"//p[@class='sc-jlwm9r-1 ewETUe']").click()

print("Total number of suggestions ",len(listElements))

for ele in listElements:
    if ele.text.__contains__("Bengaluru"):
        print(ele.text)
        print("record found")
        ele.click()
        break