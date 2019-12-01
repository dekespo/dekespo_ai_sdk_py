import unittest

from core.utils import check_positive_value

class UtilsTest(unittest.TestCase):
    def test_check_positive_value(self):
        self.assertIsNone(check_positive_value(2))
        self.assertRaises(ArithmeticError, check_positive_value, -1)
        self.assertRaises(ArithmeticError, check_positive_value, 0)

if __name__ == "__main__":
    unittest.main()
