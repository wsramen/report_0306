# -*- coding: utf-8 -*-
import unittest
import leapYear

class leapYear_Test(unittest.TestCase):
    def test_leapYear(self):
        self.assertEqual(leapYear.LEAP_YEAR(1988), "윤년")
        self.assertEqual(leapYear.LEAP_YEAR(1900), "평년")
        self.assertEqual(leapYear.LEAP_YEAR(1600), "윤년")
        self.assertEqual(leapYear.LEAP_YEAR(1994), "평범한년")
         
if __name__=="__main__":
    unittest.main(verbosity=2)

