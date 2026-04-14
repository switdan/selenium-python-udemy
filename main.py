import time

from selenium import webdriver

# Open browser
driver = webdriver.Chrome()


# Go to webpage
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(5)