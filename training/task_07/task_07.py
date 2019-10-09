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

        self.a_menu_template = """//a[.//*[contains(., '{}')]]"""
        self.a_submenu_template = """//*[contains(@class, 'docs')]//a[.//*[contains(., '{}')]]"""

    def tearDown(self):
        self.driver.quit()

    def test_menu_click(self):
        menu_names = self.get_menu_names()
        for name in menu_names:
            menu_item = self.driver.find_element_by_xpath(self.a_menu_template.format(name))
            menu_item.click()
            submenu_names = self.get_submenu_names()
            if len(submenu_names) == 0:
                self.driver.find_element_by_tag_name("h1")
                self.driver.save_screenshot(name + ".png")
            else:
                for subname in submenu_names:
                    submenu_item = self.driver.find_element_by_xpath(self.a_submenu_template.format(subname))
                    submenu_item.click()
                    self.driver.find_element_by_tag_name("h1")
                    self.driver.save_screenshot(name + " - " + subname + ".png")

    def get_menu_names(self):
        menu_box = self.driver.find_element_by_id("box-apps-menu")
        m_items = menu_box.find_elements_by_tag_name("a")
        menu_names = []
        for item in m_items:
            menu_names.append(item.find_element_by_class_name("name").text)
        return menu_names

    def get_submenu_names(self):
        m_items = self.driver.find_elements_by_xpath("//*[contains(@class, 'docs')]//a//*[contains(@class, 'name')]")
        submenu_names = []
        for item in m_items:
            submenu_names.append(item.text)
        return submenu_names

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
