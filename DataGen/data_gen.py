import random

def IcebergGen(IcebergNo):
    BergDimensions = DimensionGenerator()
    BergCoords = LocationGenerator()
    return BergDimensions,BergCoords

# Randomly generates iceberg dimensions
def DimensionGenerator (XLimit=10, YLimit=10):
    X = random.randint(0, XLimit)
    Y = random.randint(0, YLimit)
    return X,Y

# Creates a point randomly of the iceberg location
def LocationGenerator (XLimit=1000, YLimit=1000):
    X = random.randint(0, XLimit)
    Y = random.randint(0, YLimit)
    return X,Y