import pygame
from Map.icebergs import SpawnIcebergs


class Map(object):
    def __init__(self, screen):
        self.background_colour = (52, 180, 235)  # blue
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
            self.screen.fill(self.background_colour)
            self.show_icebergs()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False


        pygame.quit()
        quit()

