class MainPage:
    def __init__(self, session):
        self._session = session
        self._driver = self._session.get_driver()

    def open(self):
        self._driver.get("http://localhost/litecart/en/")
        return self

    def open_first_item(self):
        xpath = """//*[contains(@class, 'product column')]//a[contains(@class, 'link')]"""
        self._driver.find_elements_by_xpath(xpath)[0].click()
        return self._session.get_item_page()

    def open_cart_page(self):
        xpath = """//a[contains(text(), 'Checkout »')]"""
        self._driver.find_element_by_xpath(xpath).click()
        return self._session.get_cart_page()
