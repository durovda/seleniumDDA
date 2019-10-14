from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from .main_page import MainPage
from .item_page import ItemPage
from .cart_page import CartPage


class Session:
    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.implicitly_wait(0)  # seconds
        self._wait = WebDriverWait(self._driver, 3)  # seconds
        self._main_page = None
        self._item_page = None
        self._cart_page = None

    def close(self):
        self._driver.quit()

    def get_driver(self):
        return self._driver

    def get_wait(self):
        return self._wait

    def get_main_page(self):
        if self._main_page is None:
            self._main_page = MainPage(self)
        return self._main_page

    def get_item_page(self):
        if self._item_page is None:
            self._item_page = ItemPage(self)
        return self._item_page

    def get_cart_page(self):
        if self._cart_page is None:
            self._cart_page = CartPage(self)
        return self._cart_page

