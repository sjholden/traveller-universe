'''
Created on Jun 5, 2017

@author: Sam Holden <sholden@holden.id.au>
'''
from travelleruniverse import utils
from travelleruniverse.world import world

from . import srd

class WorldGen_ClassicBook3(srd.WorldGen_SRD):
    '''
    classdocs
    '''

    def generate(self):
        self.size = self.calcSize()
        self.atmo = self.calcAtmosphere()
        self.hydro = self.calcHydrosphere()
        self.pop = self.calcPopulation()
        self.govt = self.calcGovernment()
        self.rivals = self.calcRivals()
        self.law = self.calcLaw()
        self.starport = self.calcStarport()
        self.tech = self.calcTechnology()
        self.bases = self.calcBases()
        return world.World(self.starport, self.size, self.atmo, self.hydro, self.pop, self.govt, self.law, self.tech, self.bases)
    
    def calcAtmosphere(self):
        if self.size == 0:
            return 0
        return utils.rollDice(2, -7 + self.size, min_=0, max_=12)    

    def calcHydrosphere(self):
        if self.size == 0:
            return 0
        modifier = self.atmo - 7
        if self.atmo in (0, 1) or self.atmo >= 10:
            modifier = modifier -4
        return utils.rollDice(2, modifier, min_=0, max_=10)
    
    def calcTechnology(self):
        modifier = 0
        
        if self.starport == 'A':
            modifier = modifier + 6
        elif self.starport == 'B':
            modifier = modifier + 4
        elif self.starport == 'C':
            modifier = modifier + 2
        elif self.starport == 'X':
            modifier = modifier - 4
            
        if self.size <= 1:
            modifier = modifier + 2
        elif self.size <= 4:
            modifier = modifier + 1
            
        if self.atmo <= 3 or self.atmo >= 10:
            modifier = modifier + 1
            
        if self.hydro == 9:
            modifier = modifier + 1
        elif self.hydro == 10:
            modifier = modifier + 2
            
        if (self.pop >= 1 and self.pop <= 5):
            modifier = modifier + 1
        elif self.pop == 9:
            modifier = modifier + 2
        elif self.pop == 10:
            modifier = modifier + 4

            
        if self.govt in (0, 5):
            modifier = modifier + 1
        elif self.govt == 13:
            modifier = modifier - 2
            
        return utils.rollDice(1, modifier)
    
    def calcStarport(self):
        return "AAAAABBCCDEEX"[utils.rollDice(2)]
    
    def calcBases(self):
        bases = []
        # Naval
        if self.starport in ('A', 'B'):
            if utils.rollDice(2) >= 8:
                bases.append('N')
        # Scout
        if self.starport in ('A',):
            if utils.rollDice(2) >= 10:
                bases.append('S')
        elif self.starport in ('B', 'C'):
            if utils.rollDice(2) >= 8:
                bases.append('S')
        elif self.starport in ('D',):
            if utils.rollDice(2) >= 7:
                bases.append('S')
                
        return bases