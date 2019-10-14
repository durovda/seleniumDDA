from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC


class ItemPage:
    def __init__(self, session):
        self._session = session
        self._driver = self._session.get_driver()
        self._wait = self._session.get_wait()

    def add_item_to_cart(self):
        self._additional_steps()
        counter_value = self._get_counter_value()
        self._push_btn_add_to_cart()
        self._wait_cart_counter_changed(counter_value + 1)

    def _additional_steps(self):
        xpath = """//select[contains(@name, 'options[Size]')]"""
        if len(self._driver.find_elements_by_xpath(xpath)) > 0:
            combo = self._driver.find_element_by_xpath(xpath)
            Select(combo).select_by_value("Small")

    def _get_counter_value(self):
        xpath = """//*[contains(@id, 'cart')]//*[contains(@class, 'quantity')]"""
        return int(self._driver.find_element_by_xpath(xpath).text)

    def _push_btn_add_to_cart(self):
        xpath = """//*[contains(@name, 'add_cart_product')]"""
        self._driver.find_elements_by_xpath(xpath)[0].click()

    def _wait_cart_counter_changed(self, new_value):
        xpath = """//*[contains(@id, 'cart')]//*[contains(@class, 'quantity')]"""
        self._wait.until(EC.text_to_be_present_in_element((By.XPATH, xpath), str(new_value)))
