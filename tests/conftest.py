import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    print("Creating Chrome driver...")
    my_driver = webdriver.Chrome()
    yield my_driver
    print("Closing Chrome driver.")
    my_driver.quit()