# 100% branch coverage: the decision is True (2000) and False (2001).
# NOT 100% condition coverage (so not branch & condition coverage):
# - B (year % 100 != 0) is only ever evaluated once (2000) and is False there;
# it is never True.
# (A: True/False and C: True/False are both covered.)
import unittest
from Leap_Year import Leap_Year 

class BranchCoverageTests(unittest.TestCase):
    def test_2000_leap(self):
        self.assertTrue(Leap_Year(2000))
    def test_2001_not_leap(self):
        self.assertFalse(Leap_Year(2001))

if __name__ == "__main__":
    unittest.main()