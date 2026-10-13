import unittest
from Leap_Year import Leap_Year
 
class MCDCTests(unittest.TestCase):
    def test_2004(self):  self.assertTrue(Leap_Year(2004))    # T,T,F
    def test_1900(self):  self.assertFalse(Leap_Year(1900))   # T,F,F
    def test_2000(self):  self.assertTrue(Leap_Year(2000))    # T,F,T
    def test_2001(self):  self.assertFalse(Leap_Year(2001))   # F,T,F
 
if __name__ == "__main__":
    unittest.main()