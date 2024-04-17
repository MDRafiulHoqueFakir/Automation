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





login = login_Process()
login.super_login()