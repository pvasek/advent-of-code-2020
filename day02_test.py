import unittest
from day02 import is_valid, is_valid2, parse_line, parse_password_policy


class Day2Tests(unittest.TestCase):
    def test_parse_password_policy(self):
        self.assertEqual((10, 12, "a"), parse_password_policy("10-12 a"))
        self.assertEqual((1, 12, "a"), parse_password_policy("1-12 a"))

    def test_parse_line(self):
        policy1, psw1 = parse_line("10-12 a: abbaac")
        self.assertEqual((10, 12, "a"), policy1)
        self.assertEqual("abbaac", psw1)

    def test_is_valid(self):
        self.assertTrue(is_valid((4, 10, "a"), "abacadaef"))
        self.assertFalse(is_valid((4, 10, "a"), "abacaddef"))

    def test_is_valid2(self):
        self.assertTrue(is_valid2((1, 3, "a"), "abc"))
        self.assertFalse(is_valid2((1, 3, "a"), "aba"))