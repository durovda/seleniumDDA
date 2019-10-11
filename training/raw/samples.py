import unittest
from datetime import datetime


class MyTestCase(unittest.TestCase):
    @staticmethod
    def test_something():
        print(datetime.strftime(datetime.now(), "%Y_%m_%d_%H_%M_%S"))


if __name__ == '__main__':
    unittest.main()
