import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Open browser
driver = webdriver.Chrome()


# Go to webpage
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(5)


# Type username student into Username field
username_locator = driver.find_element(By.ID, "username")


# Type password Password123 into Password field
password_locator = driver.find_element(By.ID, "password")


# Push Submit button
submit_btn_locator = driver.find_element(By.ID, "submit")


# Verify new page URL contains practicetestautomation.com/logged-in-successfully/


# Verify new page URL contains practicetestautomation.com/logged-in-successfully/
logged_title_locator = driver.find_element(By.TAG_NAME, "h1")


# Verify new page contains expected text ('Congratulations' or 'successfully logged in')
logged_message_locator = driver.find_element(By.XPATH, "//p[@class='has-text-align-center']")


# Verify button Log out is displayed on the new page
logout_btn_locator = driver.find_element(By.LINK_TEXT, "Log out")