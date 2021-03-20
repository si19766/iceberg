import pygame
from DataGen.data_gen import IcebergGen
from tools import Loadify, TransformImage

# Randomly spawns Icebergs
def SpawnIcebergs(NumIcebergs):
    IcebergList = []
    for i in range(NumIcebergs):
        BergDimensions, BergCoords = IcebergGen()  # from data_gen
        image = "IcebergPics/image0.png"
        Berg = Iceberg(BergDimensions[0], BergDimensions[1], BergCoords[0], BergCoords[1], image)
        IcebergList.append(Berg)
    return IcebergList


class Iceberg(object):
    def __init__(self, x_dimen, y_dimen, x_coord, y_coord, image):
        self.iceberg_colour = (255, 255, 255)
        self.x_dimen, self.y_dimen = x_dimen, y_dimen
        self.x_coord, self.y_coord = x_coord, y_coord
        self.image = Loadify(image)
        self.image = TransformImage(self.image, x_dimen, y_dimen)

