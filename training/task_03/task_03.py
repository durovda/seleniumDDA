import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_something(self):
        self.driver.get("http://litecart.stqa.ru/admin/")
        wait = WebDriverWait(self.driver, 5)  # seconds
        usr = self.driver.find_element_by_name("username")
        usr.send_keys("admin")
        psw = self.driver.find_element_by_name("password")
        psw.send_keys("0b7dba1c77df25bf0")
        btn_login = self.driver.find_element_by_name("login")
        btn_login.click()
        wait.until(EC.title_is("My store"))
        self.driver.save_screenshot("Админка.png")

if __name__ == '__main__':
    unittest.main()