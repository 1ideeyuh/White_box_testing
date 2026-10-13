# 100% condition coverage: every atomic condition (year%4==0, year%100!=0, year%400==0)
# is True and False at least once, in both the outer and the inner decision.
# NOT 100% statement coverage: the 'return False' in the else of the outer decision never runs.
# NOT 100% branch coverage: the outer decision (year%4==0) | (year%100!=0) is True for
#   every test, so its False branch is never taken.
import unittest
from leap_year import Leap_Year
 
class ConditionCoverageTests(unittest.TestCase):
    def test_2004(self):  self.assertTrue(Leap_Year(2004))    # A=T B=T
    def test_1900(self):  self.assertFalse(Leap_Year(1900))   # A=T B=F C=F
    def test_2000(self):  self.assertTrue(Leap_Year(2000))    # A=T B=F C=T
    def test_2001(self):  self.assertFalse(Leap_Year(2001))   # A=F B=T C=F
 
if __name__ == "__main__":
    unittest.main()