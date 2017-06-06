'''
Created on May 30, 2017

@author: Sam Holden <sholden@holden.id.au>
'''

class World(object):
    '''
    classdocs
    '''


    def __init__(self, port, size, atmo, hydro, pop, govt, law, tech, bases=None, extra=None):
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
        if bases:
            self._bases = bases
        else:
            self._bases = []
        if extra:
            self._extra = extra
        else:
            self._extra = {}
        
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
    @property
    def bases(self): return self._bases
    @property
    def extra(self): return self._extra
    
        