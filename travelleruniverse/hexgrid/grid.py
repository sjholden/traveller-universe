import math

from . import hex

SQRT_3 = math.sqrt(3)

class Orientation:
    def __init__(self, f0, f1, f2, f3, b0, b1, b2, b3, angle):
        self.f0 = f0
        self.f1 = f1
        self.f2 = f2
        self.f3 = f3
        self.b0 = b0
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.angle= angle
        
ORIENT_POINTY = Orientation(SQRT_3, SQRT_3 / 2.0, 0.0, 3.0 / 2.0,
                            SQRT_3 / 3.0, -1.0 / 3.0, 0.0, 2.0 / 3.0,
                            0.5)

ORIENT_FLAT = Orientation(3.0 / 2.0, 0.0, SQRT_3 / 2.0, SQRT_3,
                          2.0 / 3.0, 0.0, -1.0 / 3.0, SQRT_3 / 3.0,
                          0.0)

class Grid:
    def __init__(self, orientation=ORIENT_FLAT):
        """Construct Hex Grid."""
        self.hexes = {}
        self.orientation = orientation

    def hexByAxial(self, q, r):
        """Return (creating if necessary) the hex at (q,r)."""
        if (q, r) not in self.hexes:
            self.hexes[(q, r)] = hex.Hex(self, q, r)
        return self.hexes[(q, r)]

    def round(self, q, r):
        "Given floating point q and r, find the axial coords of the hex."""
        x = q
        z = r
        y = -x-z
        
        rx = int(round(x))
        ry = int(round(y))
        rz = int(round(z))

        x_diff = abs(rx - x)
        y_diff = abs(ry - y)
        z_diff = abs(rz - z)

        if x_diff > y_diff and x_diff > z_diff:
            rx = -ry - rz
        elif y_diff > z_diff:
            ry = -rx - rz
        else:
            rz = -rx - ry

        return (rx, rz)
    
    def hexByCoord(self, x, y, size=1):
        """Return (creating if necessary) the hex containing the coord (x,y)"""
        x = float(x) / size;
        y = float(y) / size
        #q = ORIENT_FLAT.b0 * x + ORIENT_FLAT.b1 * y;
        #r = ORIENT_FLAT.b2 * x + ORIENT_FLAT.b3 * y;
        q = self.orientation.b0 * x + self.orientation.b1 * y;
        r = self.orientation.b2 * x + self.orientation.b3 * y;
        
        q, r = self.round(q, r)
        return self.hexByAxial(q, r)
    
    def addHex(self, hexx):
        """Add hex to grid."""
        self.hexes[(hexx.q, hexx.r)] = hexx
        
    def delHexByAxial(self, q, r):
        """Delete hex from grid."""
        if self.hasHexByAxial(q, r):
            hex = self.hexes[(q, r)]
            hex.grid = None
            del self.hexes[(q, r)]
            
    def hasHexByAxial(self, q, r):
        """Does hex exist?"""
        return (q, r) in self.hexes
    
    def hexesInRectangle(self, topx, topy, bottomx, bottomy, size=1):
        """Determine the hexes within the specified rectangle."""
        if topx > bottomx:
            topx, bottomx = bottomx, topx
        if topy > bottomy:
            topy, bottomy = bottomy, topy
            
        resultSet = []
            
        topLeft = self.hexByCoord(topx, topy, size)
        topRight = self.hexByCoord(bottomx, topy, size)
        bottomLeft = self.hexByCoord(topx, bottomy, size)
        bottomRight = self.hexByCoord(bottomx, bottomy, size)
        topLeftCenter = topLeft.center(height=SQRT_3 * size)
        
        bottomLeftCenter = bottomLeft.center(height=SQRT_3 * size)
        bottomRightCenter = bottomRight.center(height=SQRT_3 * size)
                
        if topx - topLeftCenter[0] < -0.5 * size:
            # we include some of the prior column...
            for r in range(topLeft.r, bottomLeft.r):
                resultSet.append(self.hexByAxial(topLeft.q - 1, r + 1))
                
        if topy < topLeftCenter[1]:
            topUpFirst = True
        else:
            topUpFirst = False
        if bottomy < bottomLeftCenter[1]:
            bottomUpFirst = True
        else:
            bottomUpFirst = False

        rStart = topLeft.r
        rEnd = bottomLeft.r
        for q in range(topLeft.q, bottomRight.q+1):
            if (q - topLeft.q) % 2:
                if topUpFirst:
                    rStart += -1
                if bottomUpFirst:
                    rEnd += -1
            elif  q != topLeft.q:
                if not topUpFirst:
                    rStart += -1
                if not bottomUpFirst:
                    rEnd += -1
            for r in range(rStart, rEnd + 1):
                resultSet.append(self.hexByAxial(q, r))

                                 
        if bottomx - bottomRightCenter[0] > 0.5 * size:
            # need to include the next column...
            for r in range(topRight.r, bottomRight.r):
                resultSet.append(self.hexByAxial(bottomRight.q + 1, r))
                
        return resultSet 
           
    def existingHexesInRectangle(self, topx, topy, bottomx, bottomy, size=1):
        """Determine the hexes within the specified rectangle."""
        if topx > bottomx:
            topx, bottomx = bottomx, topx
        if topy > bottomy:
            topy, bottomy = bottomy, topy
            
        resultSet = []
            
        topLeft = self.hexByCoord(topx, topy, size)
        topRight = self.hexByCoord(bottomx, topy, size)
        bottomLeft = self.hexByCoord(topx, bottomy, size)
        bottomRight = self.hexByCoord(bottomx, bottomy, size)
        topLeftCenter = topLeft.center(height=SQRT_3 * size)
        
        bottomLeftCenter = bottomLeft.center(height=SQRT_3 * size)
        bottomRightCenter = bottomRight.center(height=SQRT_3 * size)
                
        if topx - topLeftCenter[0] < -0.5 * size:
            # we include some of the prior column...
            for r in range(topLeft.r, bottomLeft.r):
                if self.hasHexByAxial(topLeft.q - 1, r + 1):
                    resultSet.append(self.hexByAxial(topLeft.q - 1, r + 1))
                
        if topy < topLeftCenter[1]:
            topUpFirst = True
        else:
            topUpFirst = False
        if bottomy < bottomLeftCenter[1]:
            bottomUpFirst = True
        else:
            bottomUpFirst = False

        rStart = topLeft.r
        rEnd = bottomLeft.r
        for q in range(topLeft.q, bottomRight.q+1):
            if (q - topLeft.q) % 2:
                if topUpFirst:
                    rStart += -1
                if bottomUpFirst:
                    rEnd += -1
            elif  q != topLeft.q:
                if not topUpFirst:
                    rStart += -1
                if not bottomUpFirst:
                    rEnd += -1
            for r in range(rStart, rEnd + 1):
                if self.hasHexByAxial(q, r):
                    resultSet.append(self.hexByAxial(q, r))

                                 
        if bottomx - bottomRightCenter[0] > 0.5 * size:
            # need to include the next column...
            for r in range(topRight.r, bottomRight.r):
                if self.hasHexByAxial(bottomRight.q + 1, r):
                    resultSet.append(self.hexByAxial(bottomRight.q + 1, r))
                
        return resultSet
    
    def allHexes(self):
        """Return all hexes defined."""
        return self.hexes.values()
        
        