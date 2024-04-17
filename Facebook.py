import time
from keyboard import press
from keyboard.mouse import (click)
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.find_element(By.XPATH,value="//input[@id='email']").send_keys("omuktomuk")
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='pass']").send_keys("omuktomuk")
time.sleep(1)
press('enter')
time.sleep(5)
driver.find_element(By.XPATH,value="//button[@id='u_0_5_O9']").click()
time.sleep(5)
