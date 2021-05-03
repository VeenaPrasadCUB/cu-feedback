# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import unittest
from data_analysis import *
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(compute_sentiment('Hi example test'), 'positive')

if __name__ == '__main__':
    unittest.main()