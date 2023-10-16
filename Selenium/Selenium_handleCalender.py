import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options= chrome_options)


driver.maximize_window()
driver.get("http://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")
#driver.implicitly_wait(20)

driver.find_element(By.XPATH,"//input[@id='datepicker']").click()

#driver.find_element(By.XPATH,"//a[text()='25']").click()

month = driver.find_element(By.XPATH,"//div[@class='ui-datepicker-title']//span[@class='ui-datepicker-month']")
print(month.text)
screen_month = month.text
datetime_object = datetime.datetime.strptime(screen_month, "%B")
screen_month_number = datetime_object.month
year = driver.find_element(By.XPATH,"//div[@class='ui-datepicker-title']//span[@class='ui-datepicker-year']")
rightButton = driver.find_element(By.XPATH,"//a[@class='ui-datepicker-next ui-corner-all']//span")
leftButton = driver.find_element(By.XPATH,"//a[@class='ui-datepicker-prev ui-corner-all']//span")
driver.implicitly_wait(20)

xoffset = 50 #your X screen offset
yoffset = 50 #your Y screen offset
action = ActionChains(driver)

if int(year.text)>2022:
    while int(year.text)>2022:
        print(123)
        driver.find_element(By.XPATH,"//a[@class='ui-datepicker-prev ui-corner-all']//span").click()
        action.move_by_offset(xoffset, yoffset).perform() #mouse move actiity, doesnt work unless it is done
        print(456)
        time.sleep(1)
        year = driver.find_element(By.XPATH,"//div[@class='ui-datepicker-title']//span[@class='ui-datepicker-year']")
        print(year.text)

        #xoffset = xoffset + 1
        #yoffset = yoffset + 1
        

if int(year.text)<2022:
    while int(year.text)<2022:
        print(123)
        driver.find_element(By.XPATH,"//a[@class='ui-datepicker-next ui-corner-all']//span").click()
        action.move_by_offset(xoffset, yoffset).perform() #mouse move actiity, doesnt work unless it is done
        print(456)
        time.sleep(1)
        year = driver.find_element(By.XPATH,"//div[@class='ui-datepicker-title']//span[@class='ui-datepicker-year']")
        print(year.text)

long_month_name = "February"
datetime_object = datetime.datetime.strptime(long_month_name, "%B")
month_number = datetime_object.month

print(month_number)
print(screen_month_number)

xoffset = 5 #your X screen offset
yoffset = 5 #your Y screen offset
action_V2 = ActionChains(driver)


if screen_month_number > month_number:
    while screen_month_number > month_number:
        print(789)
        driver.find_element(By.XPATH,"//a[@class='ui-datepicker-prev ui-corner-all']//span").click()
        action_V2.move_by_offset(xoffset, yoffset).perform() #mouse move actiity, doesnt work unless it is done
        print(126)
        time.sleep(1)
        month = driver.find_element(By.XPATH,"//div[@class='ui-datepicker-title']//span[@class='ui-datepicker-month']")
        screen_month = month.text
        datetime_object = datetime.datetime.strptime(screen_month, "%B")
        screen_month_number = datetime_object.month

        
        

if screen_month_number < month_number:
    while screen_month_number < month_number:
        print(789)
        driver.find_element(By.XPATH,"//a[@class='ui-datepicker-next ui-corner-all']//span").click()
        action_V2.move_by_offset(xoffset, yoffset).perform() #mouse move actiity, doesnt work unless it is done
        print(126)
        time.sleep(1)
        month = driver.find_element(By.XPATH,"//div[@class='ui-datepicker-title']//span[@class='ui-datepicker-month']")
        screen_month = month.text
        datetime_object = datetime.datetime.strptime(screen_month, "%B")
        screen_month_number = datetime_object.month

dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//a")


for date_element in dates:
    date = date_element.text
    print(date)
    if date=="25":
        date_element.click()
        break
