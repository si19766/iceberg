import pygame
from DataGen.data_gen import IcebergGen
from tools import Loadify, TransformImage
import random

def LoadImages():
    """Function to speed up the loading of images
    Loads all images before they are assigned to their classes"""
    image_list = []
    for num in range(6):
        image_list.append(Loadify("Map/IcebergPics/image" + str(num) + ".png"))
    return image_list

# Randomly spawns Icebergs
def SpawnIcebergs(NumIcebergs, ShipList):
    ImageList = LoadImages()
    IcebergList = []
    for i in range(NumIcebergs):
        BergDimensions, BergCoords = IcebergGen()  # from data_gen
        image = RandomImage(ImageList)
        Berg = Iceberg(BergDimensions, BergDimensions, BergCoords[0], BergCoords[1], image)
        IcebergList.append(Berg)
        for ship in ShipList:
            if Berg.y_coord - 200 <= ship.y_coord <= Berg.y_coord + 200:
                if Berg.x_coord - 200 <= ship.x_coord <= Berg.x_coord + 200:
                    if Berg in IcebergList:
                        IcebergList.remove(Berg)

    return IcebergList


def RandomImage(ImageList):
    """chooses a random image from the list"""
    randomint = random.randint(0, 5)
    image = ImageList[randomint]
    return image


class Iceberg(object):
    def __init__(self, x_dimen, y_dimen, x_coord, y_coord, image):
        self.iceberg_colour = (255, 255, 255)
        self.x_dimen, self.y_dimen = x_dimen, y_dimen
        self.x_coord, self.y_coord = x_coord, y_coord
        self.image = TransformImage(image, x_dimen, y_dimen)
        self.rect = pygame.Rect(x_coord, y_coord, x_dimen, y_dimen)


