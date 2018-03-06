# -*- coding: utf-8 -*-
import unittest
import Tax

class TaxTestCase(unittest.TestCase):
    def test_Tax(self):
        self.assertEqual(Tax.Tax(),"소득의 50% 15000.0달러를 납세하셔야 합니다.")
if __name__=="__main__":
    unittest.main(verbosity=2)
