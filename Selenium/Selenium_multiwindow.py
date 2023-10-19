import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options= chrome_options)


driver.maximize_window()
driver.get("https://technometrics.net/")
parent_window = driver.current_window_handle
print(parent_window)
print(type(parent_window))
driver.find_element(By.XPATH,"//div[contains(@class,'wgl-infobox_subtitle')]").click()
all_windows = driver.window_handles
print(type(all_windows))

for child in all_windows:
    print(child)
    if parent_window!=child:
        print("Switching to new window/tab")
        driver.switch_to.window(child)
        print("Title is "+driver.title)
        driver.find_element(By.XPATH,"//div[@class='etWJQ jym1ob kdfrQc pChizd bWQG4d ']//span[@class='Cw1rxd google-symbols G47vBd']").click()
        time.sleep(3)
        driver.close()
driver.switch_to.window(parent_window)
time.sleep(3)

driver.close()