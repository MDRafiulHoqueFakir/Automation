from keyboard import press
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
from selenium.webdriver import Keys
import time

class login_Process():
    def super_login(self):
        driver.get("http://192.168.20.127/UltimusFinSolutionTest/UFS.Web/")
        time.sleep(1)
        driver.maximize_window()
        # user id
        driver.find_element(By.XPATH, value="//input[@id='UserId']").send_keys('Jesan100')
        time.sleep(1)
        # password
        driver.find_element(By.XPATH, value="//input[@id='PasswordString']").send_keys('1')
        time.sleep(1)
        press("TAB")
        time.sleep(1)
        press("down")
        time.sleep(1)
        press("Enter")
        # login1
        driver.find_element(By.XPATH, value="//button[@id='btnlogin']").click()
        time.sleep(3)

class sms_path():
    def path0993(self):
        #search
        driver.find_element(By.XPATH,value="//input[@id='txtfastpath']").click()
        time.sleep(1)
        # search
        driver.find_element(By.XPATH,value="//input[@id='txtfastpath']").send_keys('0993')
        time.sleep(1)
        # search
        driver.find_element(By.XPATH,value="//span[@class='glyphicon glyphicon-circle-arrow-right']").click()
        time.sleep(5)

#Bank Office Id
        driver.find_element(By.XPATH,value="//input[@ng-model='BankOffice.frmObj.BankOfficeId']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,value="//input[@ng-model='BankOffice.frmObj.BankOfficeId']").send_keys('5987')
        time.sleep(2)
#Full Name
        driver.find_element(By.XPATH,value="//input[@ng-model='BankOffice.frmObj.BankOfficeFullName']").click()
        time.sleep(1)
        driver.find_element(By.XPATH,value="//input[@ng-model='BankOffice.frmObj.BankOfficeFullName']").send_keys("Muhammad")
        time.sleep(1)
#short name
        driver.find_element(By.XPATH,value="//input[@ng-model='BankOffice.frmObj.BankOfficeShortName']").send_keys("bank")
        time.sleep(2)
#office org type list
        driver.find_element(By.XPATH,value="//select[@ng-model='BankOffice.frmObj.BankOfficeOrgTypeId']").click()
        time.sleep(1)
        press("down")
        time.sleep(1)
        press("down")
        time.sleep(1)
        press("enter")
        time.sleep(1)
#Office Control Id
        driver.find_element(By.XPATH,value="//select[@ng-model='BankOffice.frmObj.BankOfficeControlId']").click()
        time.sleep(1)
        press("down")
        time.sleep(1)
        press("down")
        time.sleep(1)
        press("down")
        time.sleep(1)
        press("enter")
        time.sleep(1)
#Adress
        driver.find_element(By.XPATH,value="//body/main[@class='cd-main-content']/div[@class='lsngcontroller ng-scope']/form[@name='frmUserProfile']/div[@class='lspagebody']/div[@class='panel panel-info']/div[@class='panel-body ls-panel-body']/div[2]/div[1]/div[2]/div[1]/input[1]").send_keys("Dhaka")
        time.sleep(1)
        driver.find_element(By.XPATH,value="//input[@class='form-control ls-control ng-pristine ng-untouched ng-empty ng-invalid ng-invalid-required']").send_keys("Dhaka")
        time.sleep(1)
        driver.find_element(By.XPATH,value="//input[@ng-model='BankOffice.frmObj.ZipCode']").send_keys("7230")
        time.sleep(1)
        driver.find_element(By.XPATH,value="//select[@ng-model='BankOffice.frmObj.Division']").click()
        time.sleep(1)
        press("down")
        time.sleep(1)
        press("down")
        time.sleep(1)
        press("down")
        time.sleep(1)
        press("down")
        time.sleep(1)
        press("enter")
        time.sleep(1)
        driver.find_element(By.XPATH,value="//select[@ng-model='BankOffice.frmObj.District']").click()
        time.sleep(2)
        press("down")
        time.sleep(1)
        press("down")
        time.sleep(1)
        press("down")
        time.sleep(1)
        press("enter")
        time.sleep(1)
        driver.find_element(By.XPATH,value="//select[@ng-model='BankOffice.frmObj.Thana']").click()
        time.sleep(1)
        press("down")
        time.sleep(1)
        press("down")
        time.sleep(1)
        press("down")
        time.sleep(1)
        press("enter")
        time.sleep(1)
        driver.find_element(By.XPATH,value="//input[@ng-model='BankOffice.frmObj.Phone']").send_keys('01967360664')
        time.sleep(1)
        driver.find_element(By.XPATH,value="//select[@ng-model='BankOffice.frmObj.BankOfficeLocationTypeId']").click()
        time.sleep(1)
        press("down")
        time.sleep(1)
        press("enter")
        time.sleep(1)

        press("down")
        time.sleep(1)
        press("down")
        time.sleep(1)
        press("down")
        time.sleep(1)
        press("down")
        time.sleep(1)
        driver.find_element(By.XPATH,value="//input[@class='form-control ls-control ng-pristine ng-untouched ng-empty ng-valid-minlength ng-valid-maxlength ng-invalid ng-invalid-required']").send_keys("252522552")
        time.sleep(1)
        driver.find_element(By.XPATH,value="//input[@ng-model='BankOffice.frmObj.SBS']").send_keys("2525")
        time.sleep(1)
        driver.find_element(By.XPATH,value="//input[@ng-model='BankOffice.frmObj.ADFX']").send_keys("2525")
        time.sleep(1)
        driver.find_element(By.XPATH,value="//input[@ng-model='BankOffice.frmObj.CBCTR']").send_keys("2525")
        time.sleep(1)
        driver.find_element(By.XPATH,value="//select[@ng-model='BankOffice.frmObj.BranchServiceType']").click()
        press("down")
        time.sleep(1)
        press("Enter")
        time.sleep(1)
        driver.find_element(By.XPATH,value="//input[@ng-model='BankOffice.frmObj.BranchUltimusFlag']").click()
        time.sleep(1)
        press("down")
        time.sleep(1)
        press("down")
        time.sleep(1)
        press("down")
        time.sleep(1)
        press("down")
        time.sleep(1)
        press("down")
        time.sleep(1)
        press("down")
        time.sleep(1)
        driver.find_element(By.XPATH,value="//select[@ng-model='BankOffice.frmObj.BranchAuthDecPolicy']").click()
        time.sleep(1)
        press("down")
        time.sleep(1)
        press("enter")
        driver.find_element(By.XPATH,value="//select[@ng-model='BankOffice.frmObj.BranchAuthHierarchical']").click()
        time.sleep(1)
        press("down")
        time.sleep(1)
        press("enter")
        driver.find_element(By.XPATH,value="//b[@class='ng-binding']").click()
        time.sleep(5)
        print("ok")






login = login_Process()
login.super_login()

path=sms_path()
path.path0993()