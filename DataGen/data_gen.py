import random
import numpy

# LIMITS
X_CoordLim = 1920
Y_CoordLim = 1080
LowerIceberg_DimenLim = 1
UpperIceberg_DimenLim = 250

# FUNCTIONS
#Generate an iceberg
def IcebergGen():
    BergDimensions = DimensionGenerator()
    BergCoords = LocationGenerator()
    return BergDimensions, BergCoords

#Generate ship co-ordinates
def ShipGen():
    ShipCoords = LocationGenerator()
    return ShipCoords

# Randomly generates iceberg dimensions
def DimensionGenerator ():
    dimension = int(numpy.random.normal(75, 12, None))
    return dimension

# Creates a point randomly
def LocationGenerator (XLimit=X_CoordLim, YLimit=Y_CoordLim):
    x = random.randint(0, XLimit)
    y = random.randint(0, YLimit)
    return x, y