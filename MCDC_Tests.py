import unittest
from Leap_Year import Leap_Year

# NOT 100% multiple condition coverage: MCC needs all 2^3 = 8 combinations of (A,B,C),
# this suite exercises only 4. The untested ones are (T,T,T), (F,T,T), (F,F,T), (F,F,F).
# (All four are impossible for an integer year, e.g. a multiple of 400 is always a multiple of 100, so MCC cannot be reached for this decision as written.)
 
class MCDCTests(unittest.TestCase):
    def test_2004(self):  self.assertTrue(Leap_Year(2004))    # T,T,F
    def test_1900(self):  self.assertFalse(Leap_Year(1900))   # T,F,F
    def test_2000(self):  self.assertTrue(Leap_Year(2000))    # T,F,T
    def test_2001(self):  self.assertFalse(Leap_Year(2001))   # F,T,F
 
if __name__ == "__main__":
    unittest.main()