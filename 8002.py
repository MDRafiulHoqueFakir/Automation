import time

from keyboard import press
from selenium import webdriver
from selenium.webdriver import Keys

from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://192.168.20.127/UltimusFinSolutionTest/UFS.Web/")
driver.find_element(By.XPATH,value="//input[@id='UserId']").send_keys('N6959')
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='PasswordString']").send_keys('a1')
time.sleep(1)
driver.find_element(By.XPATH,value="//button[@id='btnlogin']").click()
time.sleep(2)
#login
driver.find_element(By.XPATH,value="//input[@id='txtMenuSearch']").send_keys('8002')
time.sleep(1)
press('enter')
time.sleep(1)
#search bar
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlAuthFunction']").click()
press('down')
time.sleep(1)
press('enter')
time.sleep(10)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_btnAuthSearch']").click()
time.sleep(2)
#Selecting Authorization item
driver.find_element(By.XPATH,value="//a[@id='ctl00_contPlcHdrMasterHolder_gvUTQ_ctl02_LinkButton']").click()
time.sleep(2)
#Select 1st items
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_btnExit']").click()
time.sleep(1)
#Exit Button
driver.find_element(By.XPATH,value="//span[normalize-space()='Yes']").click()
time.sleep(1)
#Yes Button
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_btnAuth']").click()
time.sleep(1)
#Authorize Button
driver.find_element(By.XPATH,value="//span[@class='ui-button-text']").click()
time.sleep(1)
#OK Button
#Logout
driver.find_element(By.XPATH,value="//i[@id='imgLogOut']").click()
time.sleep(2)
driver.find_element(By.XPATH,value="//span[normalize-space()='Yes']").click()
time.sleep(1)