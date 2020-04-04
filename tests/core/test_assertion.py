import unittest

from core.assertion import check_positive_value

class AssertionTest(unittest.TestCase):
    def test_check_positive_value(self):
        self.assertIsNone(check_positive_value(2))
        self.assertRaises(AssertionError, check_positive_value, -1)
        self.assertRaises(AssertionError, check_positive_value, 0)

if __name__ == "__main__":
    unittest.main()
