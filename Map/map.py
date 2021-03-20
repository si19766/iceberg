import pygame
from Map.icebergs import SpawnIcebergs
from Map.ships import SpawnShips
from tools import Loadify, TransformImage

class Map(object):
    """Class that shows the map with all corresponding objects"""
    def __init__(self, screen, x_res = 1920, y_res = 1080):
        self.BLACK = (0, 0, 0)
        self.background_image = Loadify("Background.png")
        self.background_image = TransformImage(self.background_image, x_res, y_res)
        self.grid_colour = (0, 0, 0)  # black
        self.iceberg_colour = (255, 255, 255)
        self.iceberg_rect = pygame.Rect(50, 50, 50, 50)
        self.screen = screen  # imported from Menu
        self.iceberg_list = SpawnIcebergs(30)  # creates a list
        self.ship_list = SpawnShips(1) # creates a list

    def create_grid(self):
        """Creates the grid"""
        """Horizontal line"""
        for num in range(7):
            pygame.draw.line(self.screen, self.BLACK, (0, (1080/8 * (num + 1))), (1920, (1080/8 * (num + 1))), 2)

        """Vertical line"""
        for num in range(9):
            pygame.draw.line(self.screen, self.BLACK, (((1920/10) * (num + 1)), 0), (((1920/10) * (num + 1)), 1080), 2)

    def show_objects(self):
        for iceberg in self.iceberg_list:
            self.screen.blit(iceberg.image, [iceberg.x_coord, iceberg.y_coord])
        for ship in self.ship_list:
            self.screen.blit(ship.image, [ship.x_coord, ship.y_coord])


    def Run(self):
        running = True
        pygame.init()
        while running:
            self.screen.blit(self.background_image, [0, 0])
            self.show_objects()
            self.create_grid()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False


        pygame.quit()
        quit()

