import math
import unittest

from travelleruniverse.hexgrid import grid
from travelleruniverse.hexgrid import hex

class TestGrid(unittest.TestCase):
    def setUp(self):
        self.g = grid.Grid()
        
    def test_hexByAxial(self):
        """Test returning a hex by index."""
        for q in range(-5, 5):
            for r in range(-5, 5):
                h = self.g.hexByAxial(q, r)
                self.assertEqual((h.q, h.r), (q, r))

    def test_round(self):
        """Test rounding to nearest hex."""
        self.assertEqual(self.g.round(10.3, 12.1), (10,12))
        self.assertEqual(self.g.round(10.3, 12.4), (10,13))
        
    def test_hexByCoord(self):
        """Test returning a hex by coordinate."""
        # check the corners of the center hex
        # right corner is (1.0, 0.0)
        h = self.g.hexByCoord(1.0, -0.001)
        self.assertEqual((h.q, h.r), (1, -1))
        h = self.g.hexByCoord(1.0, 0.001)
        self.assertEqual((h.q, h.r), (1, 0))
        h = self.g.hexByCoord(0.999, 0)
        self.assertEqual((h.q, h.r), (0, 0))

        # bottom right corner is (0.5, sqrt(3)/2)
        h = self.g.hexByCoord(0.501, math.sqrt(3)/2)
        self.assertEqual((h.q, h.r), (1, 0))
        h = self.g.hexByCoord(0.5, math.sqrt(3)/2 + 0.001)
        self.assertEqual((h.q, h.r), (0, 1))
        h = self.g.hexByCoord(0.5, math.sqrt(3)/2 - 0.001)
        self.assertEqual((h.q, h.r), (0, 0))

        # bottom left corner is (-0.5, sqrt(3)/2)
        h = self.g.hexByCoord(-0.501, math.sqrt(3)/2)
        self.assertEqual((h.q, h.r), (-1, 1))
        h = self.g.hexByCoord(-0.5, math.sqrt(3)/2 + 0.001)
        self.assertEqual((h.q, h.r), (0, 1))
        h = self.g.hexByCoord(-0.5, math.sqrt(3)/2 - 0.001)
        self.assertEqual((h.q, h.r), (0, 0))

        # left corner is (-1.0, 0.0)
        h = self.g.hexByCoord(-1.0, -0.001)
        self.assertEqual((h.q, h.r), (-1, 0))
        h = self.g.hexByCoord(-1.0, 0.001)
        self.assertEqual((h.q, h.r), (-1, 1))
        h = self.g.hexByCoord(-0.999, 0)
        self.assertEqual((h.q, h.r), (0, 0))        

        # top left corner is (-0.5, -sqrt(3)/2)
        h = self.g.hexByCoord(-0.501, -math.sqrt(3)/2)
        self.assertEqual((h.q, h.r), (-1, 0))
        h = self.g.hexByCoord(-0.5, -math.sqrt(3)/2 - 0.001)
        self.assertEqual((h.q, h.r), (0, -1))
        h = self.g.hexByCoord(-0.5, -math.sqrt(3)/2 + 0.001)
        self.assertEqual((h.q, h.r), (0, 0))       
       
        # top right corner is (0.5, -sqrt(3)/2)
        h = self.g.hexByCoord(0.501, -math.sqrt(3)/2)
        self.assertEqual((h.q, h.r), (1, -1))
        h = self.g.hexByCoord(0.5, -math.sqrt(3)/2 - 0.001)
        self.assertEqual((h.q, h.r), (0, -1))
        h = self.g.hexByCoord(0.5, -math.sqrt(3)/2 + 0.001)
        self.assertEqual((h.q, h.r), (0, 0))
        
    def test_addHex(self):
        """Test adding a hex to the grid."""
        g = grid.Grid()
        h = hex.Hex(self.g, 1, 1)
        self.g.addHex(h)
        self.assertIs(h, self.g.hexByAxial(1, 1))
        
    def test_hexesInRectangle(self):
        """Test hexes via rectangle."""
        # rectangle around center of a hex including four neighbors.
        hexes = self.g.hexesInRectangle(-1, -0.1, 1, 0.1)
        self.assertEqual(len(hexes), 5)
        qrs = [(x.q, x.r) for x in hexes]
        qrs.sort()
        self.assertEqual(qrs, [(-1, 0), (-1, 1), (0, 0), (1, -1), (1, 0)])
        # same but reverse the rectangle - should give same result
        hexes = self.g.hexesInRectangle(1, 0.1, -1, -0.1)
        self.assertEqual(len(hexes), 5)
        qrs = [(x.q, x.r) for x in hexes]
        qrs.sort()
        self.assertEqual(qrs, [(-1, 0), (-1, 1), (0, 0), (1, -1), (1, 0)])
        # rectangle around a horizontal edge.
        hexes = self.g.hexesInRectangle(-2, -0.9, 2, -0.1)
        self.assertEqual(len(hexes), 4)
        qrs = [(x.q, x.r) for x in hexes]
        qrs.sort()
        self.assertEqual(qrs, [(-1, 0), (0, -1), (0, 0), (1, -1)])
        # a rectangle that selects a previous column from the top corner hex.
        hexes = self.g.hexesInRectangle(-0.9, 0, -0.9, 1)
        self.assertEqual(len(hexes), 2)
        qrs = [(x.q, x.r) for x in hexes]
        qrs.sort()
        self.assertEqual(qrs, [(-1, 1), (0, 0)])
              