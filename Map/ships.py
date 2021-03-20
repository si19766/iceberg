import pygame
import math
from DataGen.data_gen import ShipGen
from tools import Loadify, TransformImage

def SpawnShips(NumShips):
    ShipList = []
    for i in range(NumShips):
        ShipCoords = ShipGen()
        Frequency = i+1
        Boat = Ship(ShipCoords[0], ShipCoords[1], Frequency, image="Map/Ship.png")
        ShipList.append(Boat)
    return ShipList

class Ship(object):
    def __init__(self, x_coord, y_coord, frequency, image):
        self.x_dimen, self.y_dimen = 50,50
        self.x_coord, self.y_coord = x_coord, y_coord
        self.image = Loadify(image)
        self.image = TransformImage(self.image, self.x_dimen, self.y_dimen)
        # Ships unique frequency
        self.frequency = frequency

    def scan(self):
        # Generate a ring of lasers around the ship which are moving away from the ship at a certain angle.
        for i in range(3600):
            shoot_angle = i/10
            current_sonar = sonar(self.x_coord, self.y_coord, shoot_angle, self.frequency)


class sonar(pygame.sprite.Sprite):

    def __init__(self, x, y, angle, frequency):
        super().__init__()
        self.x_speed = math.cos(angle)*500
        self.y_speed = math.sin(angle)*500
        self.image = pygame.Surface([3, 10])
        self.image.fill(WHITE)

        # Passed in Location
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Speed vector
        self.change_x = self.x_speed
        self.change_y = self.y_speed

        # Frequency
        self.freq = frequency

    def Update(self):
        # New position for bullet
        self.rect.y -= self.change_y