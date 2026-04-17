import pytest

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
        login_page = LoginPage(driver)

        login_page.open()
        login_page.execute_login(username, password)

        assert login_page.red_banner_msg == expected_error_message, "Red Banner message is not the same as expected message!"


