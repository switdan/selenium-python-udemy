from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from page_objects.base_page import BasePage


class ExceptionsPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_btn = (By.ID, "add_btn")
    __row1_input = (By.XPATH, "//div[@id='row1']/input")
    __row2_input = (By.XPATH, "//div[@id='row2']/input")
    __save_btn_row1 = (By.XPATH, "//div[@id='row1']/button[@id='save_btn']")
    __save_btn_row2 = (By.XPATH, "//div[@id='row2']/button[@id='save_btn']")
    __confirmation_element = (By.ID, "confirmation")
    __edit_btn = (By.ID, "edit_btn")
    __instructions_locator = (By.ID, "instructions")


    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def click_add_btn(self):
        super()._click(self.__add_btn)

    def is_row2_visible(self) -> bool:
        return self._is_displayed(self.__row2_input)

    def fill_row2(self, text):
        self._type(self.__row2_input, text)

    def save_row2(self):
        super()._click(self.__save_btn_row2)

    @property
    def confirmation_msg(self) -> str:
        return self._get_text(self.__confirmation_element)

    def click_edit_btn(self):
        super()._click(self.__edit_btn)

    def clear_row1(self):
        self._clear(self.__row1_input)

    def fill_row1(self, text):
        self._type(self.__row1_input, text)

    def click_save_btn_row1(self):
        super()._click(self.__save_btn_row1)

    def is_instructions_displayed(self) -> bool:
        return self._is_displayed(self.__instructions_locator)

    def is_instructions_hidden(self) -> bool:
        return self._element_hidden(self.__instructions_locator)
