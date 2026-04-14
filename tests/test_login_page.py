import time

import pytest
from selenium.webdriver.common.by import By


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_login_page(self, driver):
        # Go to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")


        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")


        # Type password Password123 into Password field
        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys("Password123")


        # Push Submit button
        submit_btn_locator = driver.find_element(By.ID, "submit")
        submit_btn_locator.click()

        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        time.sleep(2)
        actual_url = driver.current_url
        assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

        # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        logged_title_locator = driver.find_element(By.TAG_NAME, "h1")
        actual_title = logged_title_locator.text
        assert actual_title == "Logged In Successfully"

        # Verify button Log out is displayed on the new page
        logout_btn_locator = driver.find_element(By.LINK_TEXT, "Log out")
        assert logout_btn_locator.is_displayed()

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
        assert red_banner.is_displayed(), "Powinien pojawić się czerwony baner!"

        # Verify error message text is Your username is invalid!
        red_banner_message = red_banner.text
        assert red_banner_message == expected_error_message, "Treść czerwonego baneru się nie zgadza."


