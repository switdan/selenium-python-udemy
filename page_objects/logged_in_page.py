from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoggedInPage:
    __url = "https://practicetestautomation.com/logged-in-successfully/"
    __logged_title = (By.TAG_NAME, "h1")
    __logout_btn = (By.LINK_TEXT, "Log out")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    @property
    def expected_url(self) -> str:
        return self.__url

    @property
    def header(self) -> str:
        return self._driver.find_element(self.__logged_title).text

    @property
    def log_out_btn_displayed(self) -> bool:
        return self._driver.find_element(self. __logout_btn).is_displayed()