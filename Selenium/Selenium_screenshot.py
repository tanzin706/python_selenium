import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options= chrome_options)


driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.get_screenshot_as_file("screenshots/Selenium"+datetime.datetime.now().strftime("%H_%M_%S_%d_%m_%Y")+".png")
driver.get("https://www.youtube.com/")
driver.get_screenshot_as_file("Selenium"+datetime.datetime.now().strftime("%H_%M_%S_%d_%m_%Y")+".png")
driver.quit()