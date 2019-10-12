import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
import time


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 3)  # seconds
        self.driver.implicitly_wait(0)  # seconds

    def tearDown(self):
        self.driver.quit()

    def test_one(self):
        for i in range(3):
            self.select_product()
            self.add_cart_product()

        xpath = """//a[contains(text(), 'Checkout »')]"""
        self.driver.find_element_by_xpath(xpath).click()

        self.xpath_remove_item_button = """//button[contains(@name, 'remove_cart_item')]"""
        count = len(self.driver.find_elements_by_xpath(self.xpath_remove_item_button))
        for i in range(count):
            self.remove_cart_item()

        xpath = """//*[contains(@id, 'checkout-cart-wrapper')]//em"""
        text_no_items = "There are no items in your cart."
        self.wait.until(EC.text_to_be_present_in_element((By.XPATH, xpath), text_no_items))

        # time.sleep(1)

    def remove_cart_item(self):
        xpath = """//table[contains(@class, 'dataTable rounded-corners')]"""
        e_table = self.driver.find_element_by_xpath(xpath)
        self.driver.find_elements_by_xpath(self.xpath_remove_item_button)[0].click()
        self.wait.until(EC.staleness_of(e_table))

    def select_product(self):
        self.driver.get("http://localhost/litecart/en/")
        xpath = """//*[contains(@class, 'product column')]//a[contains(@class, 'link')]"""
        self.driver.find_elements_by_xpath(xpath)[0].click()

    def add_cart_product(self):
        self.additional_actions()
        xpath = """//*[contains(@name, 'add_cart_product')]"""
        self.driver.find_elements_by_xpath(xpath)[0].click()
        xpath = """//*[contains(@id, 'cart')]//*[contains(@class, 'quantity')]"""
        count = self.driver.find_element_by_xpath(xpath).text
        new_count = str(int(count) + 1)
        self.wait.until(EC.text_to_be_present_in_element((By.XPATH, xpath), new_count))

    def additional_actions(self):
        xpath = """//select[contains(@name, 'options[Size]')]"""
        is_different_size = len(self.driver.find_elements_by_xpath(xpath))
        if is_different_size:
            combo = self.driver.find_element_by_xpath(xpath)
            Select(combo).select_by_value("Small")


if __name__ == '__main__':
    unittest.main()