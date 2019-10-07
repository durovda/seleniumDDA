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
        self.driver.get("http://www.google.com/")
        wait = WebDriverWait(self.driver, 10)  # seconds
        search = self.driver.find_element_by_name("q")
        search.send_keys("webdriver")
        search.submit()
        wait.until(EC.title_is("webdriver - Поиск в Google"))


if __name__ == '__main__':
    unittest.main()
