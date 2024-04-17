import time
from keyboard import press
from keyboard.mouse import click
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.com/")
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='nav-bb-search']").send_keys("Mobile")
click('enter')
time.sleep(5)