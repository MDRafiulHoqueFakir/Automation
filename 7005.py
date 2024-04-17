import time
from keyboard import press
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://192.168.20.127/UltimusFinSolutionTest/UFS.Web/")
driver.find_element(By.XPATH,value="//input[@id='UserId']").send_keys('M5007')
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='PasswordString']").send_keys('a1')
time.sleep(1)
driver.find_element(By.XPATH,value="//button[@id='btnlogin']").click()
time.sleep(1)
#login
driver.find_element(By.XPATH,value="//input[@id='txtMenuSearch']").send_keys('7005')
press('enter')
time.sleep(2)
#search bar
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtAccountNo']").send_keys(7114)
time.sleep(1)
press('enter')
time.sleep(1)
#Account Number
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtAmountCcy']").send_keys(1000)
time.sleep(1)
press('enter')
time.sleep(1)
#Amount CCY
driver.find_element(By.XPATH,value="//textarea[@id='ctl00_contPlcHdrMasterHolder_LstxtNarration']").send_keys(1000)
time.sleep(1)
press('enter')
time.sleep(1)
#Narration
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_lsddlDepositorBeareType']").click()
time.sleep(1)
press('down')
time.sleep(1)
press('enter')
time.sleep(1)
#Depositor/Bearer Type
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtAmtCcyCr']").send_keys(10000)
time.sleep(1)
press('enter')
time.sleep(5)
press('scroll_down')
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(5)
#Amount
#driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_btnOk']").click()
#time.sleep(5)
#OK
#driver.find_element(By.XPATH,value="//span[normalize-space()='Yes']").click()
#time.sleep(1)
#Yes
#driver.find_element(By.XPATH,value="//span[@class='ui-button-text']").click()
#time.sleep(1)
#OK
#driver.find_element(By.XPATH,value="//i[@id='imgLogOut']").click()
#time.sleep(1)
#driver.find_element(By.XPATH,value="//span[normalize-space()='Yes']").click()
#time.sleep(1)
#Logout