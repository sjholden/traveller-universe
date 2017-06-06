'''
Created on Jun 5, 2017

@author: Sam
'''
import unittest
from travelleruniverse.world.generator import srd

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
        self._storeRollDice = srd.utils.rollDice


    def tearDown(self):
        srd.utils.rollDice = self._storeRollDice


    def testSRD_RollOnes(self):
        srd.utils.rollDice = lambda number, modifier=0, min_=None, max_=None: rollDice(1, number, modifier, min_, max_)
        world = srd.WorldGen_SRD().generate()
        self.assertEqual(world.size, 0)
        self.assertEqual(world.atmo, 0)
        self.assertEqual(world.hydro, 0)
        self.assertEqual(world.pop, 0)
        self.assertEqual(world.govt, 0)
        self.assertEqual(world.law, 0)
        self.assertEqual(world.port, 'X')
        self.assertEqual(world.tech, 0)
        self.assertEqual(world.bases, [])

    def testSRD_RollFours(self):
        srd.utils.rollDice = lambda number, modifier=0, min_=None, max_=None: rollDice(4, number, modifier, min_, max_)
        world = srd.WorldGen_SRD().generate()
        self.assertEqual(world.size, 6)
        self.assertEqual(world.atmo, 7)
        self.assertEqual(world.hydro, 7)
        self.assertEqual(world.pop, 6)
        self.assertEqual(world.govt, 7)
        self.assertEqual(world.law, 8)
        self.assertEqual(world.port, 'C')
        self.assertEqual(world.tech, 8)
        self.assertEqual(world.bases, ['S'])

    def testSRD_RollSixes(self):
        srd.utils.rollDice = lambda number, modifier=0, min_=None, max_=None: rollDice(6, number, modifier, min_, max_)
        world = srd.WorldGen_SRD().generate()
        self.assertEqual(world.size, 10)
        self.assertEqual(world.atmo, 15)
        self.assertEqual(world.hydro, 9)
        self.assertEqual(world.pop, 10)
        self.assertEqual(world.govt, 13)
        self.assertEqual(world.law, 18)
        self.assertEqual(world.port, 'A')
        self.assertEqual(world.tech, 14)
        self.assertEqual(world.bases, ['N', 'S', 'T'])

    def testSRD_HardScience_RollOnes(self):
        srd.utils.rollDice = lambda number, modifier=0, min_=None, max_=None: rollDice(1, number, modifier, min_, max_)
        world = srd.WorldGen_SRD_HardScience().generate()
        self.assertEqual(world.size, 0)
        self.assertEqual(world.atmo, 0)
        self.assertEqual(world.hydro, 0)
        self.assertEqual(world.pop, 0)
        self.assertEqual(world.govt, 0)
        self.assertEqual(world.law, 0)
        self.assertEqual(world.port, 'X')
        self.assertEqual(world.tech, 0)
        self.assertEqual(world.bases, [])

    def testSRD_HardScience_RollFours(self):
        srd.utils.rollDice = lambda number, modifier=0, min_=None, max_=None: rollDice(4, number, modifier, min_, max_)
        world = srd.WorldGen_SRD_HardScience().generate()
        self.assertEqual(world.size, 6)
        self.assertEqual(world.atmo, 7)
        self.assertEqual(world.hydro, 7)
        self.assertEqual(world.pop, 5)
        self.assertEqual(world.govt, 6)
        self.assertEqual(world.law, 7)
        self.assertEqual(world.port, 'D')
        self.assertEqual(world.tech, 5)
        self.assertEqual(world.bases, ['S'])

    def testSRD_HardScience_RollSixes(self):
        srd.utils.rollDice = lambda number, modifier=0, min_=None, max_=None: rollDice(6, number, modifier, min_, max_)
        world = srd.WorldGen_SRD_HardScience().generate()
        self.assertEqual(world.size, 10)
        self.assertEqual(world.atmo, 15)
        self.assertEqual(world.hydro, 9)
        self.assertEqual(world.pop, 8)
        self.assertEqual(world.govt, 13)
        self.assertEqual(world.law, 18)
        self.assertEqual(world.port, 'A')
        self.assertEqual(world.tech, 12)   
        self.assertEqual(world.bases, ['N', 'S', 'T'])
             
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()