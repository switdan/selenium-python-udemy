import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestExceptions:

    # @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_btn_locator = driver.find_element(By.ID, "add_btn")
        add_btn_locator.click()


        # Verify Row 2 input field is displayed
        wait = WebDriverWait(driver, 10)
        row2_input_locator = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))
        assert row2_input_locator.is_displayed(), "Row 2 input is not displayed"

    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_btn_locator = driver.find_element(By.ID, "add_btn")
        add_btn_locator.click()

        # Wait for the second row to load
        wait = WebDriverWait(driver, 10)
        row2_input_locator = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        # Type text into the second input field
        row2_text = "Hamburger"
        row2_input_locator.send_keys(row2_text)

        # Push Save button using locator By.name(“Save”)
        save_btn_locator = driver.find_element(By.NAME, "Save")
        save_btn_locator.click()

        # Verify text saved
        assert row2_input_locator.get_attribute("value") == row2_text, "In Row 2 is incorrect text"