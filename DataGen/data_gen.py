import random

def IcebergGen():
    BergDimensions = DimensionGenerator()
    BergCoords = LocationGenerator()
    return BergDimensions,BergCoords

# Randomly generates iceberg dimensions
def DimensionGenerator (XLimit=10, YLimit=10):
    x = random.randint(0, XLimit)
    y = random.randint(0, YLimit)
    return x,y

# Creates a point randomly of the iceberg location
def LocationGenerator (XLimit=1000, YLimit=1000):
    x = random.randint(0, XLimit)
    y = random.randint(0, YLimit)
    return x,y