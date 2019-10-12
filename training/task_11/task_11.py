import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)  # seconds
        self.driver.get("http://localhost/litecart/en/")

    def tearDown(self):
        self.driver.quit()

    def test_one(self):
        xpath_new_customer = """//a[contains(., 'New customers click here')]"""
        self.driver.find_element_by_xpath(xpath_new_customer).click()

        self.prefix = datetime.strftime(datetime.now(), "%m_%d_%H%M%S")
        print("current_user = " + self.prefix + "@email.com")

        self.fill_input_box("firstname", self.prefix)
        self.fill_input_box("lastname", "last_" + self.prefix)
        self.fill_input_box("address1", "Address1")
        self.fill_input_box("postcode", "12345")
        self.fill_input_box("city", "City")
        self.fill_input_box("email", self.prefix + "@email.com")
        self.fill_input_box("phone", "+1234567")
        self.fill_input_box("password", self.prefix)
        self.fill_input_box("confirmed_password", self.prefix)
        self.select_country()
        self.select_zone()
        xpath_btn = """//button[contains(@name, "create_account")]"""
        self.driver.find_element_by_xpath(xpath_btn).click()

        xpath_logout = """//a[contains(., 'Logout')]"""
        self.driver.find_element_by_xpath(xpath_logout).click()

        self.login(self.prefix + "@email.com", self.prefix)
        self.driver.save_screenshot("after_login.png")

    def select_country(self):
        xpath_combo = """//select[contains(@name, "country_code")]"""
        combo = self.driver.find_element_by_xpath(xpath_combo)
        Select(combo).select_by_value("US")

    def select_zone(self):
        xpath_option_ak = """//select[contains(@name, 'zone_code')]//option[contains(@value, 'AK')]"""
        self.wait.until(EC.presence_of_element_located((By.XPATH, xpath_option_ak)))
        xpath_combo = """//select[contains(@name, "zone_code")]"""
        combo = self.driver.find_element_by_xpath(xpath_combo)
        Select(combo).select_by_value("AK")

    def fill_input_box(self, name, value):
        xpath_input_box = """//input[contains(@name, "{}")]""".format(name)
        self.driver.find_element_by_xpath(xpath_input_box).send_keys(value)

    def login(self, email, psw):
        xpath_email = """//input[contains(@name, 'email')]"""
        xpath_psw = """//input[contains(@name, 'password')]"""
        xpath_btn_login = """//button[contains(@name, 'login')]"""
        self.driver.find_element_by_xpath(xpath_email).send_keys(email)
        self.driver.find_element_by_xpath(xpath_psw).send_keys(psw)
        self.driver.find_element_by_xpath(xpath_btn_login).click()


if __name__ == '__main__':
    unittest.main()