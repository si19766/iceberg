import random
import numpy

# LIMITS
IcebergX_CoordLim = 1920
IcebergY_CoordLim = 1080
LowerIceberg_DimenLim = 1
UpperIceberg_DimenLim = 250

# FUNCTIONS
def IcebergGen():
    BergDimensions = DimensionGenerator()
    BergCoords = LocationGenerator()
    """if BergCoords[0]+BergDimensions[0] > IcebergX_CoordLim: # Stops icebergs going off the screen
        BergCoords[0] -= BergDimensions[0]
    if BergCoords[1]+BergDimensions[1] > IcebergY_CoordLim:
        BergCoords[1] -= BergDimensions[1]"""
    return BergDimensions, BergCoords

def ShipGen():
    ShipCoords = LocationGenerator()
    return ShipCoords

# Randomly generates iceberg dimensions
def DimensionGenerator ():
    dimension = int(numpy.random.normal(75, 12, None))
    return dimension

# Creates a point randomly of the iceberg location
def LocationGenerator (XLimit=IcebergX_CoordLim, YLimit=IcebergY_CoordLim):
    x = random.randint(0, XLimit)
    y = random.randint(0, YLimit)
    return x, y