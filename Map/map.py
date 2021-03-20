import pygame
from icebergs import SpawnIcebergs


class Map(object):
    def __init__(self, screen):
        self.background_colour = (52, 180, 235)  # blue
        self.grid_colour = (0, 0, 0)  # black
        self.iceberg_colour = (255, 255, 255)
        self.iceberg_rect = pygame.Rect(50, 50, 50, 50)
        self.screen = screen  # imported from menu
        self.iceberg_list = SpawnIcebergs  # creates a list

    def show_icebergs(self):
        pass
        for iceberg in self.iceberg_list:
            #self.screen.blit()


    def Run(self):
        running = True
        while running:
            self.screen.fill(self.background_colour)
            pygame.draw.rect(self.screen, self.iceberg_colour, self.iceberg_rect)
            self.show_icebergs()