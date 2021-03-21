import pygame
import math
from DataGen.data_gen import LocationGenerator
from tools import Loadify, TransformImage

def SpawnShips(NumShips):
    ShipList = []
    for i in range(NumShips):
        ShipCoords = LocationGenerator()
        DestinationCoords = LocationGenerator()
        Frequency = i+1
        ShipColour = ((255/NumShips)*(i+1),(255/(NumShips*2))*(i),(255/(NumShips*6))*(i))
        Boat = Ship(ShipCoords[0], ShipCoords[1], DestinationCoords[0], DestinationCoords[1], Frequency, "Map/Ship.png", ShipColour)
        ShipList.append(Boat)
    return ShipList

class Ship(object):
    def __init__(self, x_coord, y_coord, x_dest, y_dest, frequency, image, colour):
        self.x_dimen, self.y_dimen = 25,90
        self.x_coord, self.y_coord = x_coord, y_coord
        self.x_speed, self.y_speed = 0,0
        self.max_speed = 0.1
        self.x_destination, self. y_destination = x_coord, y_coord
        self.x_finaldestination, self.x_finaldestination = x_dest, y_dest
        self.sailing = False
        self.image = Loadify(image)
        self.image = TransformImage(self.image, self.x_dimen, self.y_dimen)
        self.frequency = frequency
        self.colour = colour
        self.sonar_list = []
        self.detection_list = []
        self.detection_points = []

    def scan(self):
        # Generate a ring of lasers around the ship which are moving away from the ship at a certain angle.
        for i in range(900):
            shoot_angle = i/2.5
            self.sonar_list.append(sonar(self.x_coord+11, self.y_coord+25, shoot_angle, self.frequency))

    def sail(self):
        if self.sailing == False:
            self.sailing = True
            self.x_coord += self.x_speed
            self.y_coord += self.y_speed
        if self.x_coord == self.x_destination and self.y_coord == self.y_destination:
            self.sailing = False

class sonar(object):

    def __init__(self, x, y, angle, frequency):
        self.angle = angle
        self.x_speed = math.cos(self.angle)*10
        self.y_speed = math.sin(self.angle)*10
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
        self.counter = 0
        self.counter_start = False
        self.final_coords = [0,0]

    def Update(self, Iceberg_List):
        # New position for iceberg
        for bergs in Iceberg_List:
            if bergs.rect.collidepoint(self.rect_x, self.rect_y):
                self.change_x = self.x_speed * -1
                self.change_y = self.y_speed * -1
                self.counter_start = True
                self.final_coords= [self.rect_x,self.rect_y]
        self.rect_x -= self.change_x
        self.rect_y -= self.change_y
        if self.change_x == (self.x_speed * -1) and (self.spawn_x + 10) >= self.rect_x >= (self.spawn_x - 10):
            if self.change_y == (self.y_speed * -1) and (self.spawn_y + 10) >= self.rect_y >= (self.spawn_y - 10):
                self.change_x = 0
                self.change_y = 0
        if self.counter_start:
            self.counter += 1
