import math
import unittest

from travelleruniverse.hexgrid import grid
from travelleruniverse.hexgrid import hex

class TestHex(unittest.TestCase):

    def test_str(self):
        """Test __str__ of Hex."""
        h = hex.Hex(None, 1, -2)
        self.assertEqual(str(h), "(1,-2)")
        
    def test_repr(self):
        """Test __repr__ of Hex."""
        h = hex.Hex(None, 1, -2)
        self.assertEqual(repr(h), str(h))
        
    def test_center(self):
        """Test center() method."""

        # Test the center hex and the second ring.
        # center
        g = grid.Grid()
        h = hex.Hex(g, 0, 0)
        self.assertEqual(h.center(), (0.0, 0.0))

        # second ring
        ring = ((0, -2, 0, -2*hex.FLAT_HEIGHT),
                (1, -2, 1.5*hex.SIZE, -1.5*hex.FLAT_HEIGHT),
                (2, -2, 3*hex.SIZE, -hex.FLAT_HEIGHT),
                (2, -1, 3*hex.SIZE, 0),
                (2, 0, 3*hex.SIZE, hex.FLAT_HEIGHT),
                (1, 1, 1.5*hex.SIZE, 1.5*hex.FLAT_HEIGHT),
                (0, 2, 0, 2*hex.FLAT_HEIGHT),
                (-1, 2, -1.5*hex.SIZE, 1.5*hex.FLAT_HEIGHT),
                (-2, 2, -3*hex.SIZE, hex.FLAT_HEIGHT),
                (-2, 1, -3*hex.SIZE, 0),
                (-2, 0, -3*hex.SIZE, -hex.FLAT_HEIGHT),
                (-1, -1, -1.5*hex.SIZE, -1.5*hex.FLAT_HEIGHT))
        for q, r, x, y in ring:
            h = hex.Hex(g, q, r)
            hx, hy = h.center()
            x = round(x, 2)
            y = round(y, 2)
            hx = round(hx, 2)
            hy = round(hy, 2)
            self.assertEqual((hx, hy), (x, y))
        for q, r, x, y in ring:
            h = hex.Hex(g, q, r)
            hx, hy = h.center(height=hex.FLAT_HEIGHT * 2)
            x = round(x * 2, 2)
            y = round(y * 2, 2)
            hx = round(hx, 2)
            hy = round(hy, 2)
            self.assertEqual((hx, hy), (x, y))
            
    def test_center_PointyTop(self):
        """Test center() method."""
        # Test the center hex and the second ring.
        # center
        g = grid.Grid(orientation=grid.ORIENT_POINTY)
        h = hex.Hex(g, 0, 0)
        self.assertEqual(h.center(), (0.0, 0.0))

        # second ring
        ring = ((0, -2, -hex.POINTY_WIDTH, -1.5*hex.POINTY_HEIGHT),
                (1, -2, 0, -1.5*hex.POINTY_HEIGHT),
                (2, -2, hex.POINTY_WIDTH, -1.5*hex.POINTY_HEIGHT),
                (2, -1, 1.5*hex.POINTY_WIDTH, -0.75*hex.POINTY_HEIGHT),
                (2, 0, 2*hex.POINTY_WIDTH, 0),
                (1, 1, 1.5*hex.POINTY_WIDTH, 0.75*hex.POINTY_HEIGHT),
                (0, 2, hex.POINTY_WIDTH, 1.5*hex.POINTY_HEIGHT),
                (-1, 2, 0, 1.5*hex.POINTY_HEIGHT),
                (-2, 2, -hex.POINTY_WIDTH, 1.5*hex.POINTY_HEIGHT),
                (-2, 1, -1.5*hex.POINTY_WIDTH, 0.75*hex.POINTY_HEIGHT),
                (-2, 0, -2*hex.POINTY_WIDTH, 0),
                (-1, -1, -1.5*hex.POINTY_WIDTH, -0.75*hex.POINTY_HEIGHT))
        for q, r, x, y in ring:
            h = hex.Hex(g, q, r)
            hx, hy = h.center()
            x = round(x, 2)
            y = round(y, 2)
            hx = round(hx, 2)
            hy = round(hy, 2)
            self.assertEqual((hx, hy), (x, y))
        for q, r, x, y in ring:
            h = hex.Hex(g, q, r)
            hx, hy = h.center(height=hex.POINTY_HEIGHT * 2)
            x = round(x * 2, 2)
            y = round(y * 2, 2)
            hx = round(hx, 2)
            hy = round(hy, 2)
            self.assertEqual((hx, hy), (x, y))

    def test_neighbor(self):
        """Test neighbor() method."""
        g = grid.Grid()
        h = g.hexByAxial(2, 0)
        for direction, loc in ((0, (2, -1)), (1, (3, -1)), (2, (3, 0)),
                               (3, (2, 1)), (4, (1, 1)), (5, (1, 0))):
            h2 = h.neighbor(direction)
            self.assertEqual((h2.q, h2.r), loc)

    def test_neighbors(self):
        """Test neighbors() method."""
        g = grid.Grid()
        h = g.hexByAxial(2, 0)
        expectedNeighbors = [(2, -1), (3, -1), (3, 0), (2, 1), (1, 1), (1, 0)]
        neighbors = [(x.q, x.r) for x in h.neighbors()]
        expectedNeighbors.sort()    
        neighbors.sort()
        self.assertEqual(expectedNeighbors, neighbors)
        

    def test_attributes(self):
        """Test the attribute setting/getting/deleting/hasing functions."""
        h = hex.Hex(None, 0, 0)
        self.assertFalse(h.hasAttribute('key'))
        h.setAttribute('key', 1)
        self.assertTrue(h.hasAttribute('key'))
        self.assertEqual(h.getAttribute('key'), 1)
        h.delAttribute('key')
        self.assertFalse(h.hasAttribute('key'))
    
    def test_distance(self):
        """Test the distance method."""
        h1 = hex.Hex(None, -2, 3)
        h2 = hex.Hex(None, 3, -1)
        h3 = hex.Hex(None, 0, -3)
        self.assertEqual(h1.distance(h2), 5)
        self.assertEqual(h1.distance(h3), 6)
        self.assertEqual(h2.distance(h1), 5)
        self.assertEqual(h2.distance(h3), 5)
        self.assertEqual(h3.distance(h1), 6)
        self.assertEqual(h3.distance(h2), 5)

    def test_ring(self):
        """Test ring method."""
        g = grid.Grid()
        h = g.hexByAxial(-2, 2)
        ring = h.ring(0)
        self.assertEqual(ring, [h])
        h = g.hexByAxial(0, 0)
        ring = h.ring(1)
        ering = [g.hexByAxial(*x) for x in ((-1, 1), (-1, 0), (0, -1), (1, -1),
                                           (1, 0), (0, 1))]
        self.assertEqual(ring, ering)
        h = g.hexByAxial(1, 0)
        ring = h.ring(2)
        ering = [g.hexByAxial(*x) for x in ((-1, 2), (-1, 1), (-1, 0), (0, -1),
                                           (1, -2), (2, -2), (3, -2), (3, -1),
                                           (3, 0), (2, 1), (1, 2), (0, 2))]
        self.assertEqual(ring, ering)
        
    def test_spiral(self):
        """Test spiral method."""
        g = grid.Grid()
        h = g.hexByAxial(-1, 1)
        spiral = h.spiral(2)
        espiral = [g.hexByAxial(*x) for x in ((-1, 1), (-2, 2), (-2, 1),
                                              (-1, 0), (0, 0), (0, 1),
                                              (-1, 2), (-3, 3), (-3, 2),
                                              (-3, 1), (-2, 0), (-1, -1),
                                              (0, -1), (1, -1), (1, 0),
                                              (1, 1), (0, 2), (-1, 3),
                                              (-2, 3))]
        self.assertEqual(spiral, espiral)

    def test_hasHexByAxial(self):
        """test hasHexByAxial method."""
        g = grid.Grid()
        g.hexByAxial(0, 0)
        self.assertTrue(g.hasHexByAxial(0, 0))
        self.assertFalse(g.hasHexByAxial(1, 1))
        
    def test_delHexByAxial(self):
        """test delHexByAxial method."""
        g = grid.Grid()
        g.hexByAxial(0, 0)
        g.delHexByAxial(0, 0)
        self.assertFalse((0, 0) in g.hexes)
