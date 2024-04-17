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
    def path0958(self):
        #search
        driver.find_element(By.XPATH,value="//input[@id='txtfastpath']").click()
        time.sleep(1)
        # search
        driver.find_element(By.XPATH,value="//input[@id='txtfastpath']").send_keys('0959')
        time.sleep(1)
        # search
        driver.find_element(By.XPATH,value="//span[@class='glyphicon glyphicon-circle-arrow-right']").click()
        time.sleep(5)

    def user_info(self):
        driver.find_element(By.XPATH, value="//input[@name='LoginId']").click()
        time.sleep(1)
        driver.find_element(By.XPATH,value="//input[@name='LoginId']").send_keys("e5974")
        time.sleep(2)
        driver.find_element(By.XPATH,value="//span[@id='spanUserIdList']").click()
        time.sleep(1)

        driver.find_element(By.XPATH,value="//button[normalize-space()='New']").click()
        time.sleep(2)

        driver.find_element(By.XPATH,value="//select[@name='TellerTypeId']").click()
        time.sleep(1)
        press("down")
        time.sleep(1)
        press("down")
        press("Enter")
        time.sleep(1)
        driver.find_element(By.XPATH,value="//input[@name='CashCounterLimit']").click()
        time.sleep(1)
        driver.find_element(By.XPATH,value="//input[@name='CashCounterLimit']").send_keys("9999999999")
        time.sleep(1)
        driver.find_element(By.XPATH,value="//input[@ng-model='cashTeller.frmObj.TranCashPaymentFlag']").click()
        time.sleep(1)
        driver.find_element(By.XPATH,value="//input[@ng-model='cashTeller.frmObj.TranCashReceiveFlag']").click()
        time.sleep(1)
        driver.find_element(By.XPATH,value="//input[@name='TranDrPassingLimit']").click()
        time.sleep(1)
        driver.find_element(By.XPATH,value="//input[@name='TranDrPassingLimit']").send_keys("9999999999")
        time.sleep(1)
        driver.find_element(By.XPATH,value="//input[@name='TranCrPassingLimit']").click()
        time.sleep(1)
        driver.find_element(By.XPATH,value="//input[@name='TranCrPassingLimit']").send_keys("999999999999")
        time.sleep(1)
        driver.find_element(By.XPATH,value="//a[normalize-space()='Add']").click()
        time.sleep(2)
        






login=login_Process()
login.super_login()
path=sms_path()
path.path0958()
path.user_info()
