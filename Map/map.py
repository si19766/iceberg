import pygame

class Map(object):
    def __init__(self, screen):
        self.background_colour = (52, 180, 235)  # blue
        self.grid_colour = (0, 0, 0)  # black
        self.screen = screen  # imported from menu
        