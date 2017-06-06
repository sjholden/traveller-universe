'''
Created on Jun 4, 2017

@author: Sam Holden <sholden@holden.id.au>
'''
import random

def rollDice(number, modifier=0, min_=None, max_=None):
    """Return the result of [number]d6+[modifier] limited between min and max."""
    result = 0
    for _ in range(number):
        result = result + random.randint(1,6)
    result = result + modifier
    if max_ is not None and result > max_:
        result = max_
    if min_ is not None and result < min_:
        result = min_
    return result

