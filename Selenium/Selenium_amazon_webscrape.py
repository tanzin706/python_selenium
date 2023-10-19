import smtplib
from email.message import EmailMessage
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options= chrome_options)


driver.maximize_window()
driver.get("https://www.amazon.in/")
driver.implicitly_wait(20)

driver.find_element(By.XPATH,"//input[contains(@id,'searchtextbox')]").send_keys("Samsung phones")
ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
driver.find_element(By.XPATH,"//span[text()='Samsung']").click()
Phone_list = driver.find_elements(By.XPATH,"//span[contains(@class,'a-color-base a-text-normal')]")
Phone_price_list = driver.find_elements(By.XPATH,"//span[contains(@data-a-size,'xl')]")
cellvalue = 0
myphone = []
myprice = []
for phone in Phone_list:
    myphone.append(phone.text)
    myprice.append(Phone_price_list[cellvalue].text)
    cellvalue = cellvalue+1

Final_list = zip(myphone,myprice)

driver.quit()

wb = Workbook()
wb['Sheet'].title='Amazon Samsung Data'

sh1=wb.active

sh1.append(['Name','Price'])

for x in list(Final_list):
    sh1.append(x)

print(type(Final_list))

wb.save("FinalRecords.xlsx")

msg=EmailMessage()
msg['Subject']='Samsung Phone Data'
msg['From']='Tanzin Training Team'
msg['To']='tanzin@technometrics.net,tanzin706@gmail.com'

with open('EmailTemplate.txt') as myfile:
    data=myfile.read()
    msg.set_content(data)

with open('FinalRecords.xlsx','rb') as amazonfile:
    file_data = amazonfile.read()
    print("File data in binary",file_data)
    file_name = amazonfile.name
    print("File name is ",file_name)
    msg.add_attachment(file_data,maintype="application",subtype="xlsx",filename=file_name)

with smtplib.SMTP_SSL('smtp@gmail.com',456) as server:
    server.login("tanzin707@gmail.com","Thegunner726")
    server.send_message(msg)