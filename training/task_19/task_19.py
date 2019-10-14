import time
import unittest
from .session import Session


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.session = Session()

    def tearDown(self):
        self.session.close()

    def test_one(self):
        main_page = self.session.get_main_page()
        for _ in range(3):
            main_page.open().open_first_item().add_item_to_cart()
        main_page.open().open_cart_page().clean()


if __name__ == '__main__':
    unittest.main()