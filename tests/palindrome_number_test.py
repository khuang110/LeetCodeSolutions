""" src/_009_palindrome_number.py tests """
import unittest
from src import solution


class TestPalindromeNumber(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution.isPalindrome(x=121), True)


