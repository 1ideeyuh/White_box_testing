import unittest
import Leap_Year

# 100% statement coverage (both return statements run) but not 100% condition coverage
#-b (year % 100 != 0) is never false
# -c (year % 400 == 0) is never true

class StatementCoverageTests(unittest.TestCase):
    def test_2004_leap(self):
        self.assertTrue(Leap_Year.Leap_Year(2004))
    def test_2001_not_leap(self):
        self.assertFalse(Leap_Year.Leap_Year(2001))

if __name__ == "__main__":
    unittest.main()