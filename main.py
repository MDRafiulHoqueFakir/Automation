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
time.sleep(2)
#login
driver.find_element(By.XPATH,value="//input[@id='txtMenuSearch']").send_keys('3111')
#search bar
time.sleep(2)
press('enter')
time.sleep(2)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtForwardingRefNo']").send_keys('10')
#forwarding Ref NO
time.sleep(2)
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlCreditDept']").click()
#Financing Department
press('down')
time.sleep(1)
press('down')
time.sleep(1)
press('down')
time.sleep(1)
press('enter')
time.sleep(2)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtCustomerID']").send_keys('0000875270')
#Customer
time.sleep(1)
press('enter')
time.sleep(5)
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlMailingAddressType']").click()
press('down')
time.sleep(1)
press('enter')
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtCustomerName']").click()
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
#Mailing Address Type
#press('down')
#press('enter')
#time.sleep(1)
#driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtEconomicPurposeCodeSBS']").send_keys('10000207')
#time.sleep(1)
#driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
#Economic Purpose

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtSecurityCode']").send_keys('02')
press('enter')
time.sleep(1)
#Security/Collateral Code
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlLendingConcentration']").click()
press('down')
press('enter')
time.sleep(1)
#Credit Concentration
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlExportSector']").click()
press('down')
press('enter')
time.sleep(1)
press('enter')
time.sleep(1)
#Export Non Export
press('tab')
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlLendingPurpose']").click()
press('down')
time.sleep(1)
press('down')
time.sleep(1)
press('down')
time.sleep(1)
press('down')
time.sleep(1)
press('down')
time.sleep(1)
press('down')
time.sleep(1)
press('down')
time.sleep(1)
press('down')
time.sleep(1)
press('down')
time.sleep(1)
press('enter')
time.sleep(1)

#Credit Purpose

#/driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlExposureType']").click()
#press('down')
#press('enter')
#time.sleep(1)
#Exposure Type Base

driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlProduct']").send_keys('711')
time.sleep(1)
#Product
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlApprovalAuthority']").click()
press('down')
time.sleep(1)
press('enter')
time.sleep(1)
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlCreditLineID']").click()
time.sleep(1)
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
#Authority Approval
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtLimitAmount']").send_keys(100000)
press('enter')
time.sleep(1)
#Limit Amount
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtLimitValidity']").send_keys(12)
press('enter')
time.sleep(1)
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlLimitValidity']").click()
press('down')
time.sleep(1)
press('down')
time.sleep(1)
#Limit Validity
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtACValidity']").click()
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtACValidity']").send_keys(12)
press('enter')
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlACValidity']").click()
press('down')
time.sleep(1)
press('down')
time.sleep(1)
press('enter')
time.sleep(1)
press('tab')
#Account Duration
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlEnvironCategory']").click()
press('down')
time.sleep(1)
press('enter')
time.sleep(1)
#Environment Category
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlRiskCategory']").click()
press('down')
time.sleep(1)
press('enter')
time.sleep(1)
#Risk Category
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlInterestRateType']").click()
press('down')
time.sleep(1)
press('enter')
time.sleep(1)
press('tab')
#Interest Rate type
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlPurposeName']").click()
time.sleep(1)
press('down')
time.sleep(1)
press('enter')
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_btnAddPurpose']").click()
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
#Purpose Name
driver.find_element(By.XPATH,value="//textarea[@id='ctl00_contPlcHdrMasterHolder_LstxtDepositNote']").send_keys("Ready")
time.sleep(1)
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)

#Remarks

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_btnOk']").click()
time.sleep(2)
#OK
driver.find_element(By.XPATH,value="//span[normalize-space()='Yes']").click()
time.sleep(1)
#Yes
driver.find_element(By.XPATH,value="//span[@class='ui-button-text']").click()
time.sleep(2)
#Loan Proposal OK

#Logout
driver.find_element(By.XPATH,value="//i[@id='imgLogOut']").click()
time.sleep(2)
driver.find_element(By.XPATH,value="//span[normalize-space()='Yes']").click()
time.sleep(2)