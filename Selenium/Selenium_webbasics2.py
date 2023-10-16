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

userName = driver.find_element(By.XPATH,"//input[@id='username']").send_keys("admin")
passWord = driver.find_element(By.CSS_SELECTOR,"input[name='password']").send_keys("admin")
Click_Button = driver.find_element(By.XPATH,"//button[contains(text(),'Log in')]").click()
assert "dashboard" in driver.current_url
Click_Button = driver.find_element(By.XPATH,"//i[@class='caret']").click()
Click_Button = driver.find_element(By.XPATH,"//a[contains(text(),'Sign out')]").click()
assert "login" in driver.current_url

time.sleep(3)
driver.quit()