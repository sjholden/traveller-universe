'''
Created on May 30, 2017

@author: shold
'''

class Person(object):
    '''
    classdocs
    '''


    def __init__(self, str_, dex, end, int_, edu, soc, age, skills):
        '''
        Constructor
        '''
        self._str = str_
        self._dex = dex
        self._end = end
        self._int = int_
        self._edu = edu
        self._soc = soc
        self._age = age
        self._skills = skills
        
    @property
    def str(self): return self._str
    @property
    def dex(self): return self._dex
    @property
    def end(self): return self._end
    @property
    def int(self): return self._int
    @property
    def edu(self): return self._edu
    @property
    def soc(self): return self._soc
    @property
    def age(self): return self._age

        
        