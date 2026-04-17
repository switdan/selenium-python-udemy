import time

import pytest
from selenium.webdriver.common.by import By

from page_objects.logged_in_page import LoggedInPage
from page_objects.login_page import LoginPage


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_login_page(self, driver):
        login_page = LoginPage(driver)

        login_page.open()
        login_page.execute_login("student", "Password123")

        logged_in_page = LoggedInPage(driver)

        assert logged_in_page.current_url == logged_in_page.expected_url, "Actual URL is not the same as expected URL!"
        assert logged_in_page.header == "Logged In Successfully", "Header is not the same as expected header!"
        assert logged_in_page.log_out_btn_displayed, "Logout button is not displayed!"

class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                            [("incorrectUser", "Password123", "Your username is invalid!"),
                            ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        # Go to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys(password)

        # Push Submit button
        submit_btn_locator = driver.find_element(By.ID, "submit")
        submit_btn_locator.click()

        # Verify error message is displayed
        time.sleep(2)
        red_banner = driver.find_element(By.ID, "error")
        assert red_banner._is_displayed(), "Powinien pojawić się czerwony baner!"

        # Verify error message text is Your username is invalid!
        red_banner_message = red_banner.text
        assert red_banner_message == expected_error_message, "Treść czerwonego baneru się nie zgadza."


