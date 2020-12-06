import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/litecart/en/")
        self.wait = WebDriverWait(self.driver, 5)  # seconds

    def test_check_stickers(self):
        products = self.driver.find_elements_by_xpath("//*[contains(@class, 'product column')]")
        for item in products:
            stickers = item.find_elements_by_xpath(".//*[contains(@class, 'sticker')]")
            self.assertEqual(1, len(stickers))

    def tearDown(self):
        self.driver.quit()
        pass


if __name__ == '__main__':
    unittest.main()
