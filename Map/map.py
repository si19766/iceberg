import pygame
from Map.icebergs import SpawnIcebergs
from Map.ships import SpawnShips
from tools import Loadify, TransformImage
from Map.icebergs import Iceberg
import math
import random
import numpy
from Menu.parameter_menu import ParameterMenu

class Map(object):
    """Class that shows the map with all corresponding objects"""
    def __init__(self, screen, x_res = 1920, y_res = 1080):
        self.BLACK = (0, 0, 0)
        self.WHITE = (255,255,255)
        self.background_image = Loadify("Background.png")
        self.background_image = TransformImage(self.background_image, x_res, y_res)
        self.grid_colour = (0, 0, 0)  # black
        self.iceberg_colour = (255, 255, 255)
        self.iceberg_rect = pygame.Rect(50, 50, 50, 50)
        self.screen = screen  # imported from Menu
        pmen = ParameterMenu(0,0)
        self.ship_list = SpawnShips(pmen.boatNumber) # creates a list
        self.iceberg_list = SpawnIcebergs(pmen.icebergNumber, self.ship_list)  # creates a list
        self.rect_list = []
        self.vector_list = []
        self.rect_list = []


        self.clock = pygame.time.Clock()
        for ship in self.ship_list:
            ship.scan()

    def create_grid(self):
        """Creates the grid"""
        """Horizontal line"""
        for num in range(7):
            pygame.draw.line(self.screen, self.BLACK, (0, (1080/8 * (num + 1))), (1920, (1080/8 * (num + 1))), 2)

        """Vertical line"""
        for num in range(9):
            pygame.draw.line(self.screen, self.BLACK, (((1920/10) * (num + 1)), 0), (((1920/10) * (num + 1)), 1080), 2)

    def define_rects(self):
        x_length = 1920/10
        y_length = 1080/8
        for y_num in range(8):
            for x_num in range(10):
                rect_corners = []
                rect_corners.append(pygame.Rect(x_num*x_length, y_num*y_length, x_length, y_length))
                self.rect_list.append(rect_corners)

    def define_vectors(self):
        for num in range(80):
            x_vec = random.randint(0, 10)
            y_vec = random.randint(0, 10)
            self.rect_list[num].append(numpy.array([x_vec, y_vec]))

    def show_objects(self):
        for iceberg in self.iceberg_list:
            self.screen.blit(iceberg.image, [iceberg.x_coord, iceberg.y_coord])
            for rect, vector in self.rect_list:
                if rect.collidepoint(iceberg.x_coord, iceberg.y_coord):
                    iceberg.x_vec = vector[0]
                    iceberg.y_vec = vector[1]

            iceberg.x_coord += iceberg.x_vec * 0.005
            iceberg.rect.x = iceberg.x_coord
            iceberg.y_coord += iceberg.y_vec * 0.005
            iceberg.rect.y = iceberg.y_coord

        for ship in self.ship_list:
            self.screen.blit(ship.image, [ship.x_coord, ship.y_coord])
            for sonar in ship.sonar_list:
                pygame.draw.circle(self.screen, ship.colour, [sonar.rect_x,sonar.rect_y], 2)
                sonar.Update(self.iceberg_list)
                if sonar.final_coords != [0,0] and sonar.change_x == 0 and sonar.change_y == 0:
                    pygame.draw.circle(self.screen, ship.colour, sonar.final_coords, 2)


    def Run(self):
        running = True
        pygame.init()
        self.define_rects()
        self.define_vectors()
        show = False
        count = 0
        while running:
            self.screen.blit(self.background_image, [0, 0])
            self.show_objects()
            self.create_grid()
            if show == True:
                for iceberg in self.iceberg_list:
                    self.screen.blit(iceberg.image, [iceberg.x_coord, iceberg.y_coord])
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        for ship in self.ship_list:
                            ship.sonar_list = []
                            ship.scan()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        show = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            count += 1
            if count == 400:
                for ship in self.ship_list:
                    ship.sonar_list = []
                    ship.scan()
            self.clock.tick(100)
            pygame.display.update()

        pygame.quit()
        quit()

