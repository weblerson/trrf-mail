import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from .driver_enum import Using
from .elements import Elements


class Driver:

    def __init__(self, elements: Elements) -> None:
        self.__dict__.update(elements())

        self.__options = webdriver.FirefoxOptions()
        self.__driver = webdriver.Remote(
            options=self.__options
        )

        self.__is_operating = False

    def __set_operating_status(self, status: bool) -> None:
        self.__is_operating = status

        return

    def __verify_status(self):
        if not self.__is_operating:
            raise Exception('Driver not operating')

    def enter_page(self, url: str) -> None:
        self.__driver.get(url)
        self.__set_operating_status(True)

        return

    def exit(self) -> None:
        self.__verify_status()

        self.__driver.quit()
        self.__set_operating_status(False)

        return

    def get_title(self) -> str:
        self.__verify_status()

        return self.__driver.title

    def write_in_element(self, using: Using, **kwargs) -> None:
        self.__verify_status()
        element = self.__dict__[kwargs['element']]

        match using:
            case Using.XPATH:
                self.__driver \
                    .find_element(By.XPATH, element) \
                    .send_keys(kwargs['text'])

            case Using.CLASS:
                self.__driver \
                    .find_element(By.CLASS_NAME, element) \
                    .send_keys(kwargs['text'])

            case Using.ID:
                self.__driver \
                    .find_element(By.ID, element) \
                    .send_keys(kwargs['text'])

        return

    def get_element_value(self, using: Using, **kwargs) -> str:
        self.__verify_status()
        element = self.__dict__[kwargs['element']]

        print(element)

        match using:
            case Using.XPATH:
                return self.__driver \
                    .find_element(By.XPATH, element) \
                    .get_attribute('value')

            case Using.CLASS:
                return self.__driver \
                    .find_element(By.CLASS_NAME, element) \
                    .get_attribute('value')

            case Using.ID:
                return self.__driver \
                    .find_element(By.ID, element) \
                    .get_attribute('value')
