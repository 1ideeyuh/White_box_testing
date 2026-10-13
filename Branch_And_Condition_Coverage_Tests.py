import unittest
from Leap_Year import Leap_Year

# (A, B, C each True and False) with only three tests, but NOT 100% MC/DC:
#   - A is shown independent: 2004 (T,T,F)->True vs 2001 (F,T,F)->False.
#   - B has no independence pair: B is False only together with C=True (2000), where C
#    masks it. The pair needs 1900 (A=T,B=F,C=F), which is missing.
#   - C has no independence pair for the same reason (needs 1900 to pair with 2000).
 
class BranchAndConditionCoverageTests(unittest.TestCase):
    def test_2004(self):  self.assertTrue(Leap_Year(2004))    # A=T B=T
    def test_2000(self):  self.assertTrue(Leap_Year(2000))    # A=T B=F C=T
    def test_2001(self):  self.assertFalse(Leap_Year(2001))   # A=F C=F
 
if __name__ == "__main__":
    unittest.main()