# CPE 202 Location Class Test Cases, Lab 1

import unittest
from location import *

class TestLocation(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    def test_init(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc, Location("SLO", 35.3, -120.7))

    def test_eq(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        self.assertEqual(loc1 == loc2, (False, False))

    def test_eq1(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc3 = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc1 == loc3, (True, True))



if __name__ == "__main__":
        unittest.main()
