'''
Created on May 30, 2017

@author: shold
'''
import unittest
from travelleruniverse.world import world


class Test(unittest.TestCase):


    def testProperties(self):
        w = world.World(1,2,3,4,5,6,7,8)
        self.assertEqual(w.port, 1)
        self.assertEqual(w.size, 2)
        self.assertEqual(w.atmo, 3)
        self.assertEqual(w.hydro, 4)
        self.assertEqual(w.pop, 5)
        self.assertEqual(w.govt, 6)
        self.assertEqual(w.law, 7)
        self.assertEqual(w.tech, 8)
        self.assertEqual(w.extra, {})
        w = world.World(1,2,3,4,5,6,7,8, {'extra':2})
        self.assertEqual(w.extra, {'extra':2})
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testProperties']
    unittest.main()