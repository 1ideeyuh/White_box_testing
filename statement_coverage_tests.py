import unittest
import leap_year

# 100% statement coverage (both return statements run) but not 100% condition coverage
#-b (year % 100 != 0) is never false
# -c (year % 400 == 0) is never true

class StatementCoverageTests(unittest.TestCase):
    def test_2004_leap(self):
        self.assertTrue(leap_year.leap_year(2004))
    def test_2001_not_leap(self):
        self.assertFalse(leap_year.leap_year(2001))

if __name__ == "__main__":
    unittest.main()