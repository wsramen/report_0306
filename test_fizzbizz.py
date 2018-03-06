# -*- coding: utf-8 -*-
import unittest
import fizzbizz

class FizzbizzTestCase(unittest.TestCase):
    def test_fizzbizz(self):
        self.assertEqual(fizzbizz.fizzbizz(100),[1, 2, 'fizz', 4, 'bizz', 'fizz', 7, 8, 'fizz', 'bizz', 11, 'fizz', 13, 14, 'fizzbizz', 16, 17, 'fizz', 19, 'bizz', 'fizz', 22, 23, 'fizz', 'bizz', 26, 'fizz', 28, 29, 'fizzbizz', 31, 32, 'fizz', 34, 'bizz', 'fizz', 37, 38, 'fizz', 'bizz', 41, 'fizz', 43, 44, 'fizzbizz', 46, 47, 'fizz', 49, 'bizz', 'fizz', 52, 53, 'fizz', 'bizz', 56, 'fizz', 58, 59, 'fizzbizz', 61, 62, 'fizz', 64, 'bizz', 'fizz', 67, 68, 'fizz', 'bizz', 71, 'fizz', 73, 74, 'fizzbizz', 76, 77, 'fizz', 79, 'bizz', 'fizz', 82, 83, 'fizz', 'bizz', 86, 'fizz', 88, 89, 'fizzbizz', 91, 92, 'fizz', 94, 'bizz', 'fizz', 97, 98, 'fizz', 'bizz'])

if __name__=="__main__":
    unittest.main(verbosity=2)
