import math
import weakref

"""
Hex representation.

Coordinates are Axial with the center hex being at position (0,0).
Hexes are radius (from center to corner) of 1.0.
"""

SIZE = 1.0
SQRT_3 = math.sqrt(3)
FLAT_WIDTH = 2* SIZE
FLAT_HEIGHT = SQRT_3 / 2 * FLAT_WIDTH
POINTY_HEIGHT = 2* SIZE
POINTY_WIDTH = SQRT_3 / 2 * POINTY_HEIGHT

NEIGHBORS = [(0, -1), (1, -1), (1, 0), (0, 1), (-1, 1), (-1, 0)]

class Hex(object):
    def __init__(self, grid, q, r):
        """Construct Hex (q,r) in grid."""
        if grid is not None:
            self.grid = weakref.proxy(grid)
        else:
            self.grid = None
        self.q = q
        self.r = r
        self.attributes = {}

    def __str__(self):
        return "(%d,%d)" % (self.q, self.r)
    
    def __repr__(self):
        return str(self)
    
    def center_orig(self, flatTop=True, height=None):
        """Return the coordinate "pixel" of the hex."""
        if flatTop:
            if height:
                size = height / SQRT_3
            else:
                size = SIZE
            x = size * 1.5 * self.q
            y = size * SQRT_3 * (self.r + self.q / 2.0)
        else:
            if height:
                size = height / 2.0
            else:
                size = SIZE
            x = size * SQRT_3 * (self.q + self.r / 2.0)
            y = size * 1.5 * self.r
        print (self, size, x, y)
        return (x, y)
    
    def center(self, height=None):
        """Return the coordinate "pixel" of the hex."""
        if height:
            size = height / 3.0 /  self.grid.orientation.b3
        else:
            size = SIZE
        x = (self.grid.orientation.f0 * self.q + self.grid.orientation.f1 * self.r) * size
        y = (self.grid.orientation.f2 * self.q + self.grid.orientation.f3 * self.r) * size
        return (x, y)

    def neighbor(self, direction):
        """Return the neighboring hex in direction direction.

        direction - 0 is upper we move clockwise around to 5 being upper left.
        """
        n = NEIGHBORS[direction]
        return self.grid.hexByAxial(self.q + n[0], self.r + n[1])

    def neighbors(self):
        """Return all neightbors."""
        q = self.q
        r = self.r
        return [self.grid.hexByAxial(q + x[0], r + x[1]) for x in NEIGHBORS]

    def setAttribute(self, name, value):
        """Set an attribute value."""
        self.attributes[name] = value

    def getAttribute(self, name):
        """Return a previously set attibute."""
        return self.attributes[name]

    def hasAttribute(self, name):
        """Is there a value for the attribute name."""
        return name in self.attributes

    def delAttribute(self, name):
        """Delete the attribute name if it exists."""
        if name in self.attributes:
            del self.attributes[name]

    def distance(self, other):
        """Distance between self and other hexes."""
        x1 = self.q
        z1 = self.r
        x2 = other.q
        z2 = other.r
        y1 = -(x1 + z1)
        y2 = -(x2 + z2)
        return (abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)) / 2

    def ring(self, radius):
        """Return sequence of hexes making up ring centered on this hex."""
        if radius == 0:
            return [self]
        rhex = self
        for _ in range(radius):
            rhex = rhex.neighbor(4)
        results = []
        for i in range(6):
            for _ in range(radius):
                results.append(rhex)
                rhex = rhex.neighbor(i)
        return results

    def spiral(self, radius):
        """Return sequence of hexes within a ring centered on this hex."""
        results = [self]
        rhex = self
        for tradius in range(radius):
            rhex = rhex.neighbor(4)
            for i in range(6):
                for _ in range(tradius+1):
                    results.append(rhex)
                    rhex = rhex.neighbor(i)
        return results
