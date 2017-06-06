'''
Created on Jun 5, 2017

@author: Sam
'''
import unittest
from travelleruniverse.world.generator import classicbook3

def rollDice(dievalue, number, modifier=0, min_=None, max_=None):
    """Roll [dievalue] for all dice"""
    result = number * dievalue
    result = result + modifier
    if max_ is not None and result > max_:
        result = max_
    if min_ is not None and result < min_:
        result = min_
    return result


class Test(unittest.TestCase):


    def setUp(self):
        self._storeRollDice = classicbook3.utils.rollDice


    def tearDown(self):
        classicbook3.utils.rollDice = self._storeRollDice


    def testClassicBook3_RollOnes(self):
        classicbook3.utils.rollDice = lambda number, modifier=0, min_=None, max_=None: rollDice(1, number, modifier, min_, max_)
        world = classicbook3.WorldGen_ClassicBook3().generate()
        self.assertEqual(world.size, 0)
        self.assertEqual(world.atmo, 0)
        self.assertEqual(world.hydro, 0)
        self.assertEqual(world.pop, 0)
        self.assertEqual(world.govt, 0)
        self.assertEqual(world.law, 0)
        self.assertEqual(world.port, 'A')
        self.assertEqual(world.tech, 11)
        self.assertEqual(world.bases, [])

    def testClassicBook3_RollFours(self):
        classicbook3.utils.rollDice = lambda number, modifier=0, min_=None, max_=None: rollDice(4, number, modifier, min_, max_)
        world = classicbook3.WorldGen_ClassicBook3().generate()
        self.assertEqual(world.size, 6)
        self.assertEqual(world.atmo, 7)
        self.assertEqual(world.hydro, 8)
        self.assertEqual(world.pop, 6)
        self.assertEqual(world.govt, 7)
        self.assertEqual(world.law, 8)
        self.assertEqual(world.port, 'C')
        self.assertEqual(world.tech, 6)
        self.assertEqual(world.bases, ['S'])

    def testClassicBook3_RollSixes(self):
        classicbook3.utils.rollDice = lambda number, modifier=0, min_=None, max_=None: rollDice(6, number, modifier, min_, max_)
        world = classicbook3.WorldGen_ClassicBook3().generate()
        self.assertEqual(world.size, 10)
        self.assertEqual(world.atmo, 12)
        self.assertEqual(world.hydro, 10)
        self.assertEqual(world.pop, 10)
        self.assertEqual(world.govt, 13)
        self.assertEqual(world.law, 18)
        self.assertEqual(world.port, 'X')
        self.assertEqual(world.tech, 7)
        self.assertEqual(world.bases, [])

             
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()