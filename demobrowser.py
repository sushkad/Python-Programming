import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.worldmonitor.app/")

driver.maximize_window()

print(driver.title)

time.sleep(2)