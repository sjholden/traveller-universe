'''
Created on May 30, 2017

@author: shold
'''

class World(object):
    '''
    classdocs
    '''


    def __init__(self, port, size, atmo, hydro, pop, govt, law, tech):
        '''
        Constructor
        '''
        self._port = port
        self._size = size
        self._atmo = atmo
        self._hydro = hydro
        self._pop = pop
        self._govt = govt
        self._law = law
        self._tech = tech
        
    @property
    def port(self): return self._port
    @property
    def size(self): return self._size
    @property
    def atmo(self): return self._atmo
    @property
    def hydro(self): return self._hydro
    @property
    def pop(self): return self._pop
    @property
    def govt(self): return self._govt
    @property
    def law(self): return self._law
    @property
    def tech(self): return self._tech
    
    
        