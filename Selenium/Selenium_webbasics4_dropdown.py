import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options= chrome_options)

driver.maximize_window()
print(type(driver))
driver.get("https://www.facebook.com/")
driver.implicitly_wait(10)

# newAccount = driver.find_element(By.PARTIAL_LINK_TEXT,"Create")
newAccount = driver.find_element(By.XPATH,"//a[contains(text(),'Create')]")
newAccount.click()

month = driver.find_element(By.ID,"month")

monthDD = Select(month)

firstwebelement = monthDD.first_selected_option
print("First web element is ",firstwebelement.text)

listDD = monthDD.options
print(len(listDD))
assert 12==len(listDD)
for ele in listDD:
    print("Value is ",ele.text)
    if ele.text=="Nov":
        ele.click()
        break
driver.find_element(By.XPATH,"//label[text()='Male']").click()
driver.find_element(By.XPATH,"//button[text()='Sign Up']").click()

# monthDD.select_by_index(3)
# time.sleep(2)
# monthDD.select_by_value("6")
# time.sleep(2)
# monthDD.select_by_visible_text("Aug")