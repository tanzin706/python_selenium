import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options= chrome_options)

driver.maximize_window()
print(type(driver))
driver.get("https://www.facebook.com/")

Email = driver.find_element(By.NAME,"email")
Password = driver.find_element(By.ID,"pass")


attrabuteData = Email.get_attribute("type")
fontSize = Email.value_of_css_property("font-size")
print(fontSize)
print(attrabuteData)

enableStatus=Email.is_enabled()
displayStatus=Email.is_displayed()
print(enableStatus)
print(displayStatus)

Email.send_keys("something@gmail.com")
Password.send_keys("123456")

Click_Button = driver.find_element(By.NAME,"login")
Click_Button.click()


mypagetitle=driver.title
print(mypagetitle)
time.sleep(3)
driver.quit()

