import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/litecart/en/")
        self.wait = WebDriverWait(self.driver, 5)  # seconds

    def tearDown(self):
        self.driver.quit()

    def test_one(self):
        self.wait.until(EC.title_is("Online Store | My Store"))


if __name__ == '__main__':
    unittest.main()