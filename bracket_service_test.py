#!/usr/bin/env python

import unittest

from bracket_service import BracketService


class BracketServiceTest(unittest.TestCase):
    def test_2018_brackets_simple(self):
        service = BracketService(2018)
        self.assertEqual(0, service.get_tax(0))
        self.assertEqual(952.50, service.get_tax(9525))
        self.assertEqual(4453.50, service.get_tax(38700))
        self.assertEqual(952.50 + 20 * 0.12, service.get_tax(9525 + 20))


if __name__ == '__main__':
    unittest.main()
