'''
Created on Jun 4, 2017

@author: Sam Holden <sholden@holden.id.au>
'''
import unittest
from travelleruniverse import utils


class Test(unittest.TestCase):


    def testRollDice(self):
        # check rolls stay within ranges
        for _ in range(10):
            result = utils.rollDice(1)
            self.assertGreaterEqual(result, 1) and self.assertLessEqual(result, 6)
        for _ in range(10):
            result = utils.rollDice(3,5)
            self.assertGreaterEqual(result, 8) and self.assertLessEqual(result, 23)
        for _ in range(10):
            result= utils.rollDice(3, 5, min=14, max=16)
            self.assertGreaterEqual(result, 14) and self.assertLessEqual(result, 16)
            
            


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()