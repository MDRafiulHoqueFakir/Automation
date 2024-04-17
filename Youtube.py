import time

from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.youtube.com/")
time.sleep(5)