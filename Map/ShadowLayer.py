from tools import Loadify, TransformImage
import random
import pygame

class FogOfWar():
    def __init__(self, x_coord, y_coord, opacity=200):
        self.image = Loadify("Map/cloud.png")
        self.x_coord = x_coord + random.randint(-100,100)
        self.y_coord = y_coord + random.randint(-20,20)
        self.image = TransformImage(self.image, 200,200)
        self.opacity = opacity

