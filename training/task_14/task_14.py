import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://litecart.stqa.ru/admin/")
        self.wait = WebDriverWait(self.driver, 5)  # seconds
        self.login_to_admin()

    def tearDown(self):
        self.driver.quit()

    def test_one(self):
        self.driver.get("http://litecart.stqa.ru/admin/?app=countries&doc=edit_country")
        main_window_handle = self.driver.current_window_handle
        xpath = """//a[.//*[contains(@class, 'fa fa-external-link')]]"""
        refs = self.driver.find_elements_by_xpath(xpath)
        for element in refs:
            old_handles = self.driver.window_handles
            element.click()
            self.wait.until(EC.new_window_is_opened(old_handles))
            new_handles = self.driver.window_handles
            new_window_handle = self._get_new_window_handle(old_handles, new_handles)
            self.driver.switch_to.window(new_window_handle)
            self.driver.close()
            self.driver.switch_to.window(main_window_handle)

    @staticmethod
    def _get_new_window_handle(old_handles, new_handles):
        for handle in new_handles:
            if old_handles.count(handle) == 0:
                return handle

    def login_to_admin(self):
        usr = self.driver.find_element_by_name("username")
        usr.send_keys("admin")
        psw = self.driver.find_element_by_name("password")
        psw.send_keys("0b7dba1c77df25bf0")
        btn_login = self.driver.find_element_by_name("login")
        btn_login.click()
        self.wait.until(EC.title_is("My store"))


if __name__ == '__main__':
    unittest.main()
