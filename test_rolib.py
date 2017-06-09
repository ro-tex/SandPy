import unittest

import rolib


class TestRoLib(unittest.TestCase):
    '''Based on https://docs.python.org/2/library/unittest.html
    '''

    def test_hello(self):
        self.assertEqual(rolib.hello(), 'Hello from RoLib!')


if __name__ == '__main__':
    unittest.main()
