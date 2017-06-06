'''
Created on Jun 4, 2017

@author: Sam Holden <sholden@holden.id.au>
'''
from travelleruniverse import utils
from travelleruniverse.world import world


class WorldGen_SRD(object):
    '''
    Generate worlds according to the SRD
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.size = None
        self.atmo = None
        self.temp = None
        self.hydro = None
        self.pop = None
        self.govt = None
        self.rivals = None
        self.law = None
        self.starport = None
        self.tech = None
        self.bases = None
        
    def generate(self):
        self.size = self.calcSize()
        self.atmo = self.calcAtmosphere()
        self.temp = self.calcTemperature()
        self.hydro = self.calcHydrosphere()
        self.pop = self.calcPopulation()
        self.govt = self.calcGovernment()
        self.rivals = self.calcRivals()
        self.law = self.calcLaw()
        self.starport = self.calcStarport()
        self.tech = self.calcTechnology()
        self.bases = self.calcBases()
        return world.World(self.starport, self.size, self.atmo, self.hydro, self.pop, self.govt, self.law, self.tech, bases=self.bases)
        
    
    def calcSize(self):
        return utils.rollDice(2,-2)
    
    def calcAtmosphere(self):
        return utils.rollDice(2, -7 + self.size, min_=0, max_=15)
    
    def calcTemperature(self):
        if self.atmo in (2,3):
            modifier = -2
        elif self.atmo in (4, 5, 14):
            modifier = -1
        elif self.atmo in (8, 9):
            modifier = 1
        elif self.atmo in (10, 13, 15):
            modifier = 2
        elif self.atmo in (11, 12):
            modifier = 6
        else:
            modifier = 0   
        return utils.rollDice(2, modifier)
    
    def calcHydrosphere(self):
        if self.size in (0, 1):
            return 0
        modifier = self.size - 7
        if self.atmo in (0, 1, 10, 11, 12):
            modifier = modifier -4
        if self.temp >= 12:
            modifier = modifier - 6
        elif self.temp >= 10:
            modifier = modifier - 2
        return utils.rollDice(2, modifier, min_=0, max_=10)
    
    def calcPopulation(self):
        return utils.rollDice(2, -2)
    
    def calcGovernment(self):
        return utils.rollDice(2, -7 + self.pop, min_=0, max_=13)
    
    def calcRivals(self):
        if self.pop == 0:
            return []
        number = utils.rollDice(1, 1) // 2
        if self.govt in (0, 7):
            number = number + 1
        elif self.govt >= 10:
            number = number - 1
        rivals = []
        for _ in range(number):
            rivals.append((self.calcGovernment(), utils.rollDice(2)))
        return rivals
    
    def calcLaw(self):
        if self.pop == 0:
            return 0
        return utils.rollDice(2, -7 + self.govt, min_=0)
    
    def calcStarport(self):
        return "XXXEEDDCCBBAA"[utils.rollDice(2)]
    
    def calcTechnology(self):
        if self.pop == 0:
            return 0
        
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
            
        if self.hydro in (0, 9):
            modifier = modifier + 1
        elif self.hydro == 10:
            modifier = modifier + 2
            
        if self.pop <= 5 or self.pop == 9:
            modifier = modifier + 1
        elif self.pop == 10:
            modifier = modifier + 2
        elif self.pop == 11:
            modifier = modifier + 3
        elif self.pop == 12:
            modifier = modifier + 4
            
        if self.govt in (0, 5):
            modifier = modifier + 1
        elif self.govt == 7:
            modifier = modifier + 2
        elif self.govt in (13, 14):
            modifier = modifier - 2
            
        return utils.rollDice(1, modifier)
            
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
        # Pirate
        if self.starport in ('B', 'D', 'E'):
            if utils.rollDice(2) >= 12:
                bases.append('P')
        elif self.starport in ('C',):
            if utils.rollDice(2) >= 10:
                bases.append('P')
        # Traveller's Aid
        if self.starport in ('A',):
            if utils.rollDice(2) >= 4:
                bases.append('T')
        elif self.starport in ('B',):
            if utils.rollDice(2) >= 6:
                bases.append('T')
        elif self.starport in ('C',):
            if utils.rollDice(2) >= 10:
                bases.append('T')
        return bases
    
class WorldGen_SRD_SpaceOpera(WorldGen_SRD):
    def calcAtmosphere(self):
        if self.size <= 2:
            return 0
        result = utils.rollDice(2, -7 + self.size, min_=0, max_=15)
        if self.size in (3, 4):
            if result <= 2:
                result = 0
            elif result <= 5:
                result = 1
            else:
                result = 10
        return result
    
class WorldGen_SRD_HardScience(WorldGen_SRD_SpaceOpera):
    def calcPopulation(self):
        modifier = -2
        if self.size in (0, 1, 10):
            modifier = modifier - 1
        if self.atmo in (5, 6, 8):
            modifier = modifier + 1
        else:
            modifier = modifier - 1
        return utils.rollDice(2, modifier, min_=0)

    def calcStarport(self):
        return "XXXEEDDCCBBAA"[utils.rollDice(2, -7 + self.pop, min_=2, max_=12)]
    
