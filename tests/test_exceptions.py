import pytest

from page_objects.exceptions_page import ExceptionsPage


class TestExceptions:

    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)

        exceptions_page.open()
        exceptions_page.click_add_btn()

        assert exceptions_page.is_row2_visible(), "Row 2 input is not displayed"

    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)

        exceptions_page.open()
        exceptions_page.click_add_btn()
        exceptions_page.fill_row2("Hamburger")
        exceptions_page.save_row2()

        assert exceptions_page.confirmation_msg == "Row 2 was saved", "Confirmation message is wrong"

    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)

        exceptions_page.open()
        exceptions_page.click_edit_btn()
        exceptions_page.clear_row1()
        exceptions_page.fill_row1("Hamburger")
        exceptions_page.click_save_btn_row1()

        assert exceptions_page.confirmation_msg == "Row 1 was saved", "Confirmation message is wrong"


    @pytest.mark.exceptions
    def test_stale_element_reference_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)

        exceptions_page.open()

        assert exceptions_page.is_instructions_displayed(), "Instructions element is not displayed"

        exceptions_page.click_add_btn()

        assert exceptions_page.is_instructions_hidden(), "Instructions element is displays, but it should not be"

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_timeout_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)

        exceptions_page.open()
        exceptions_page.click_add_btn()
        exceptions_page.is_row2_visible()

        assert exceptions_page.is_row2_visible(), "Row 2 input is not displayed"