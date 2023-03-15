from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import random


class Driver:
    
    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)

        self.__options = webdriver.FirefoxOptions()
        self.__driver = webdriver.Remote(
            options=self.__options
        )

        self.__is_operating = False

    def __set_operating_status(self, status: bool) -> None:
        self.__is_operating = status

        return

    def enter_page(self, url: str) -> None:
        self.__driver.get(url)
        self.__set_operating_status(True)

        return

    def exit(self):
        if not self.__is_operating:
            raise Exception('Driver not operating')

        self.__driver.quit()
        self.__set_operating_status(False)

        return

    def get_title(self) -> str:
        if not self.__is_operating:
            raise Exception('Driver not operating')

        return self.__driver.title

    def write_in_input(xpath: str, text: str):
        ...