import pygame
import math
from DataGen.data_gen import ShipGen
from tools import Loadify, TransformImage

def SpawnShips(NumShips):
    ShipList = []
    for i in range(NumShips):
        ShipCoords = ShipGen()
        Frequency = i+1
        ShipColour = ((255/NumShips)*(i+1),(255/(NumShips*2))*(i),(255/(NumShips*6))*(i))
        Boat = Ship(ShipCoords[0], ShipCoords[1], Frequency, "Map/Ship.png", ShipColour)
        ShipList.append(Boat)
    return ShipList

class Ship(object):
    def __init__(self, x_coord, y_coord, frequency, image, colour):
        self.x_dimen, self.y_dimen = 50,50
        self.x_coord, self.y_coord = x_coord, y_coord
        self.image = Loadify(image)
        self.image = TransformImage(self.image, self.x_dimen, self.y_dimen)
        # Ships unique frequency
        self.frequency = frequency
        self.colour = colour
        self.sonar_list = []

    def scan(self):
        # Generate a ring of lasers around the ship which are moving away from the ship at a certain angle.
        for i in range(1800):
            shoot_angle = i/5
            self.sonar_list.append(sonar(self.x_coord, self.y_coord, shoot_angle, self.frequency))


class sonar(object):

    def __init__(self, x, y, angle, frequency):
        self.angle = angle
        self.x_speed = math.cos(self.angle)*5
        self.y_speed = math.sin(self.angle)*5
        self.spawn_x = x
        self.spawn_y = y
        # Passed in Location
        self.rect_x = x
        self.rect_y = y

        # Speed vector
        self.change_x = self.x_speed
        self.change_y = self.y_speed

        # Frequency
        self.freq = frequency

    def Update(self, Iceberg_List):
        # New position for bullet
        for bergs in Iceberg_List:
            if bergs.rect.collidepoint(self.rect_x, self.rect_y):
                self.change_x = self.x_speed * -1
                self.change_y = self.y_speed * -1
        if self.change_x == (self.x_speed * -1) and (self.spawn_x + 10) >= self.rect_x >= (self.spawn_x - 10):
            if self.change_y == (self.y_speed * -1) and (self.spawn_y + 10) >= self.rect_y >= (self.spawn_y - 10):
                self.change_x = 0
                self.change_y = 0
        self.rect_x -= self.change_x
        self.rect_y -= self.change_y