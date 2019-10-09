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
        self.a_country_template = """//a[contains(., "{}")]"""

    def tearDown(self):
        self.driver.quit()

    def test_menu_countries(self):
        self.driver.get("http://litecart.stqa.ru/admin/?app=countries&doc=countries")
        rows = self.driver.find_elements_by_class_name("row")
        country_names = []
        excepted_country_names = []
        for row in rows:
            country_item = row.find_elements_by_tag_name("a")[0]
            country_names.append(country_item.text)
        excepted_country_names = country_names.copy()
        excepted_country_names.sort()
        self.assertEqual(excepted_country_names, country_names)

        # country_names = ["Albania", "Canada"]

        for country_name in country_names:
            self.driver.get("http://litecart.stqa.ru/admin/?app=countries&doc=countries")
            a_country = self.driver.find_element_by_xpath(self.a_country_template.format(country_name))
            a_country.click()
            self.check_zone_names()

    def test_menu_geo_zones(self):
        self.driver.get("http://litecart.stqa.ru/admin/?app=geo_zones&doc=geo_zones")
        rows = self.driver.find_elements_by_class_name("row")
        country_names = []
        excepted_country_names = []
        for row in rows:
            country_item = row.find_elements_by_tag_name("a")[0]
            country_names.append(country_item.text)
        for country_name in country_names:
            self.driver.get("http://litecart.stqa.ru/admin/?app=geo_zones&doc=geo_zones")
            a_country = self.driver.find_element_by_xpath(self.a_country_template.format(country_name))
            a_country.click()
            self.check_geo_zone_names()

    def check_zone_names(self):
        zone_names = []
        excepted_zone_names = []
        table_zones = self.driver.find_element_by_id("table-zones")
        xpath = """//input[contains(@name, "][name]")]"""
        zones = table_zones.find_elements_by_xpath(xpath)
        for item in zones:
            zone_names.append(item.get_attribute("value"))
        if len(zone_names) > 0:
            excepted_zone_names = zone_names.copy()
            excepted_zone_names.sort()
            self.assertEqual(excepted_zone_names, zone_names)

    def check_geo_zone_names(self):
        zone_names = []
        excepted_zone_names = []
        table_zones = self.driver.find_element_by_id("table-zones")
        xpath = """//select[contains(@name, "][zone_code]")]//*[contains(@selected, "selected")]"""
        zones = table_zones.find_elements_by_xpath(xpath)
        for item in zones:
            zone_names.append(item.text)
        if len(zone_names) > 0:
            excepted_zone_names = zone_names.copy()
            excepted_zone_names.sort()
            self.assertEqual(excepted_zone_names, zone_names)

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
