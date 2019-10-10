import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.isFirefox = False

    def tearDown(self):
        self.driver.quit()

    def test_for_chrome(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/litecart/en/")
        self.wait = WebDriverWait(self.driver, 5)  # seconds
        self.check_product_page()

    def test_for_firefox(self):
        self.isFirefox = True
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost/litecart/en/")
        self.wait = WebDriverWait(self.driver, 5)  # seconds
        self.check_product_page()

    def check_product_page(self):
        xpath_products = """//*[contains(@id, "box-campaigns")]//*[contains(@class, "product column")]"""
        e_main_product = self.driver.find_elements_by_xpath(xpath_products)[0]
        e_main_name, e_main_r_price, e_main_c_price = self.get_main_elements(e_main_product)
        main_name = e_main_name.text
        main_r_price = e_main_r_price.text
        main_c_price = e_main_c_price.text
        self.check_r_price_color(e_main_r_price)
        self.check_r_price_text_decoration(e_main_r_price)
        self.check_c_price_color(e_main_c_price)
        self.check_c_price_font_weight(e_main_c_price)
        self.compare_price_font_size(e_main_c_price, e_main_r_price)
        e_main_product.find_element_by_xpath(""".//a[contains(@class, 'link')]""").click()
        e_detail_product = self.driver.find_element_by_id("box-product")
        e_detail_name, e_detail_r_price, e_detail_c_price = self.get_detail_elements(e_detail_product)
        detail_name = e_detail_name.text
        detail_r_price = e_detail_r_price.text
        detail_c_price = e_detail_c_price.text
        self.check_r_price_color(e_detail_r_price)
        self.check_r_price_text_decoration(e_detail_r_price)
        self.check_c_price_color(e_detail_c_price)
        self.check_c_price_font_weight(e_detail_c_price)
        self.compare_price_font_size(e_detail_c_price, e_detail_r_price)
        self.assertEqual(main_name, detail_name)
        self.assertEqual(main_r_price, detail_r_price)
        self.assertEqual(main_c_price, detail_c_price)

    def check_c_price_font_weight(self, c_price_element):
        font_weight = int(c_price_element.value_of_css_property("font-weight"))
        self.assertTrue(font_weight >= 700)

    def compare_price_font_size(self, c_price_element, r_price_element):
        r_price_font_size = float(r_price_element.value_of_css_property("font-size")[:-2])
        c_price_font_size = float(c_price_element.value_of_css_property("font-size")[:-2])
        self.assertTrue(r_price_font_size < c_price_font_size)

    def check_r_price_text_decoration(self, r_price_element):
        _r_price_text_decoration = r_price_element.value_of_css_property("text-decoration")
        self.assertTrue(_r_price_text_decoration.find("line-through") > -1)

    def check_c_price_color(self, c_price_element):
        color_as_text = c_price_element.value_of_css_property("color")
        if self.isFirefox:
            color_as_text = color_as_text[4:-1]
        else:
            color_as_text = color_as_text[5:-1]
        colors = tuple(color_as_text.split(", "))
        self.assertTrue((colors[1] == colors[2] == "0") and (colors[0] != "0"))

    def check_r_price_color(self, r_price_element):
        color_as_text = r_price_element.value_of_css_property("color")
        if self.isFirefox:
            color_as_text = color_as_text[4:-1]
        else:
            color_as_text = color_as_text[5:-1]
        colors = tuple(color_as_text.split(", "))
        self.assertTrue(colors[0] == colors[1] == colors[2])

    @staticmethod
    def get_main_elements(e_main_product):
        e_main_name = e_main_product.find_element_by_class_name("name")
        e_main_r_price = e_main_product.find_element_by_class_name("regular-price")
        e_main_c_price = e_main_product.find_element_by_class_name("campaign-price")
        return e_main_name, e_main_r_price, e_main_c_price

    @staticmethod
    def get_detail_elements(e_detail_product):
        e_detail_name = e_detail_product.find_element_by_tag_name("h1")
        e_detail_r_price = e_detail_product.find_element_by_class_name("regular-price")
        e_detail_c_price = e_detail_product.find_element_by_class_name("campaign-price")
        return e_detail_name, e_detail_r_price, e_detail_c_price


if __name__ == '__main__':
    unittest.main()