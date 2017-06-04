'''
Created on Jun 4, 2017

@author: Sam Holden <sholden@holden.id.au>
'''
import random
from idlelib.MultiCall import _modifier_masks

def rollDice(number, modifier=0, max=None, min=None):
    """Return the result of [number]d6+[modifier] limited between min and max."""
    result = 0
    for _ in range(number):
        result = result + random.randint(1,6)
    result = result + modifier
    if max is not None and result > max:
        result = max
    if min is not None and result < min:
        result = min
    return result

