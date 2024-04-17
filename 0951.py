from keyboard import press
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
from selenium.webdriver.support.ui import Select
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
    def path0951(self):
        #search
        driver.find_element(By.XPATH,value="//input[@id='txtfastpath']").click()
        time.sleep(1)
        # search
        driver.find_element(By.XPATH,value="//input[@id='txtfastpath']").send_keys('0951')
        time.sleep(1)
        # search
        driver.find_element(By.XPATH,value="//span[@class='glyphicon glyphicon-circle-arrow-right']").click()
        time.sleep(5)

    def userprofile(self):
        #user id
        driver.find_element(By.XPATH,value="//input[@id='LoginId']").send_keys("f5974")
        time.sleep(1)
        driver.find_element(By.XPATH,value="//input[@name='userProfileName']").click()
        time.sleep(2)
        #USER NAME
        driver.find_element(By.XPATH,value="//input[@name='userProfileName']").send_keys("asan")
        time.sleep(3)
        driver.find_element(By.XPATH,value="//input[@id='BankStaff']").click()
        time.sleep(1)
        #EMAIL
        driver.find_element(By.XPATH,value="//input[@id='UserEmailId']").send_keys("zim@leads-bd.com")
        time.sleep(1)
        #Mobile
        driver.find_element(By.XPATH,value="//input[@id='MobileNumber']").send_keys('01967360664')
        time.sleep(2)
        #Branch Office
        dropdown = driver.find_element(By.XPATH, "//select[@name='HomeBranchId']")
        levelname = 'MSZ Bank (5974)'

        for option in dropdown.find_elements(By.TAG_NAME, "option"):
            if option.text == levelname:
                option.click()
                time.sleep(2)
        driver.find_element(By.XPATH,value="//textarea[@class='form-control ls-control lstextarea ng-pristine ng-untouched ng-empty ng-invalid ng-invalid-required']").send_keys('zim')
        time.sleep(2)

        driver.find_element(By.XPATH,value="//input[@id='AnyBranchReportAccess']").click()
        time.sleep(1)
        for _ in range(3):
            press('Down')
            time.sleep(1)

       # driver.find_element(By.XPATH,value="//input[@id='AnyBranchReportAccess']").click()
        for _ in range(3):
            press('Down')
            time.sleep(1)
        driver.find_element(By.XPATH,value="//button[@id='addAllRows']").click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(2)
        driver.find_element(By.XPATH,value="//b[@class='ng-binding']").click()
        time.sleep(2)






login=login_Process()
login.super_login()

path=sms_path()
path.path0951()
path.userprofile()