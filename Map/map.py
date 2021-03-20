import pygame
from Map.icebergs import SpawnIcebergs
from tools import Loadify, TransformImage

class Map(object):
    """Class that shows the map with all corresponding objects"""
    def __init__(self, screen, x_res = 1920, y_res = 1080):
        self.background_image = Loadify("Background.png")
        self.background_image = TransformImage(self.background_image, x_res, y_res)
        self.grid_colour = (0, 0, 0)  # black
        self.iceberg_colour = (255, 255, 255)
        self.iceberg_rect = pygame.Rect(50, 50, 50, 50)
        self.screen = screen  # imported from menu
        self.iceberg_list = SpawnIcebergs(30)  # creates a list

    def show_icebergs(self):
        for iceberg in self.iceberg_list:
            self.screen.blit(iceberg.image, [iceberg.x_coord, iceberg.y_coord])

    def Run(self):
        running = True
        pygame.init()
        while running:
            self.screen.blit(self.background_image, [0, 0])
            self.show_icebergs()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False


        pygame.quit()
        quit()

