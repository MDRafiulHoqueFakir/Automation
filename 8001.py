import time

from keyboard import press
from selenium import webdriver
from selenium.webdriver import Keys

from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://192.168.20.127/UltimusFinSolutionTest/UFS.Web/")
driver.find_element(By.XPATH,value="//input[@id='UserId']").send_keys('N5007')#User May Change M5007 or N5007
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='PasswordString']").send_keys('a1')
time.sleep(1)
driver.find_element(By.XPATH,value="//button[@id='btnlogin']").click()
time.sleep(2)
#login
driver.find_element(By.XPATH,value="//input[@id='txtMenuSearch']").send_keys('8001')
time.sleep(1)
press('enter')
time.sleep(1)
#search bar
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_btnFind']").click()
time.sleep(2)
#Find
driver.find_element(By.XPATH,value="//a[normalize-space()='Select']").click()
time.sleep(1)
#Select
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtBStartNo']").click()
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
#Ok
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_btnOk']").click()
time.sleep(1)
#Authorize
driver.find_element(By.XPATH,value="//span[normalize-space()='Yes']").click()
time.sleep(1)
#Yes
driver.find_element(By.XPATH,value="//span[@class='ui-button-text']").click()
time.sleep(1)
#OK
#Logout
driver.find_element(By.XPATH,value="//i[@id='imgLogOut']").click()
time.sleep(2)
driver.find_element(By.XPATH,value="//span[normalize-space()='Yes']").click()
time.sleep(1)