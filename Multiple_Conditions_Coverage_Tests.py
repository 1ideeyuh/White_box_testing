import unittest
from Leap_Year import Leap_Year
 
class MultipleConditionsCoverageTests(unittest.TestCase):
    def test_2001(self):  self.assertFalse(Leap_Year(2001))   # year%4 False
    def test_2004(self):  self.assertTrue(Leap_Year(2004))    # %4 True, %100 True
    def test_2000(self):  self.assertTrue(Leap_Year(2000))    # %4 T, %100 F, %400 True
    def test_1900(self):  self.assertFalse(Leap_Year(1900))   # %4 T, %100 F, %400 False
 
if __name__ == "__main__":
    unittest.main()