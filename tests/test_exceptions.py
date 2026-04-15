import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestExceptions:

    @pytest.mark.exceptions
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
        row2_input_locator.send_keys("Hamburger")

        # Push Save button using locator By.name(“Save”)
        save_btn_locator = driver.find_element(By.XPATH, "//div[@id='row2']/button[@id='save_btn']")
        save_btn_locator.click()

        # Verify text saved
        confirmation_element = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        assert confirmation_element.text == "Row 2 was saved", "Confirmation message is wrong"

    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Clear input field
        edit_btn_locator = driver.find_element(By.ID, "edit_btn")
        edit_btn_locator.click()
        row1_input_locator = driver.find_element(By.XPATH, "//div[@id='row1']/input")
        row1_input_locator.clear()

        # Type text into the input field
        row1_input_locator.send_keys("Hamburger")
        save_btn_locator = driver.find_element(By.XPATH, "//div[@id='row1']/button[@id='save_btn']")
        save_btn_locator.click()


        # Verify text changed
        wait = WebDriverWait(driver, 10)
        confirmation_element = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        assert confirmation_element.text == "Row 1 was saved", "Confirmation message is wrong"

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_stale_element_reference_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Find the instructions text element
        instructions_locator = driver.find_element(By.ID, "instructions")

        # Push add button
        add_btn_locator = driver.find_element(By.ID, "add_btn")
        add_btn_locator.click()


        # Verify instruction text element is no longer displayed
        wait = WebDriverWait(driver, 3)
        assert wait.until(ec.invisibility_of_element_located((By.ID, "instructions"))), "Instructions element is displays, but it should not be"