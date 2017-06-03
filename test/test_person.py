'''
Created on May 30, 2017

@author: shold
'''
import unittest
from travelleruniverse import person


class Test(unittest.TestCase):


    def testProperties(self):
        p = person.Person(1,2,3,4,5,6,7,[])
        self.assertEqual(p.str, 1)
        self.assertEqual(p.dex, 2)
        self.assertEqual(p.end, 3)
        self.assertEqual(p.int, 4)
        self.assertEqual(p.edu, 5)
        self.assertEqual(p.soc, 6)
        self.assertEqual(p.age, 7)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testProperties']
    unittest.main()