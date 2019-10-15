from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, session):
        self._session = session
        self._driver = self._session.get_driver()
        self._wait = self._session.get_wait()

    def clean(self):
        item_count = self._get_items_count()
        for _ in range(item_count):
            self._remove_any_item()
        self._wait_cart_cleaned()

    def _get_items_count(self):
        xpath_remove_item_button = """//button[contains(@name, 'remove_cart_item')]"""
        return len(self._driver.find_elements_by_xpath(xpath_remove_item_button))

    def _remove_any_item(self):
        table_element = self._get_table_element()
        self._push_any_btn_remove_item()
        self._wait_table_redrawn(table_element)

    def _get_table_element(self):
        xpath = """//table[contains(@class, 'dataTable rounded-corners')]"""
        return self._driver.find_element_by_xpath(xpath)

    def _push_any_btn_remove_item(self):
        xpath_remove_item_button = """//button[contains(@name, 'remove_cart_item')]"""
        self._driver.find_elements_by_xpath(xpath_remove_item_button)[0].click()

    def _wait_table_redrawn(self, table_element):
        self._wait.until(EC.staleness_of(table_element))

    def _wait_cart_cleaned(self):
        xpath = """//*[contains(@id, 'checkout-cart-wrapper')]//em"""
        text_no_items = "There are no items in your cart."
        self._wait.until(EC.text_to_be_present_in_element((By.XPATH, xpath), text_no_items))

