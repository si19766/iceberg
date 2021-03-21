import pygame
from Map.route_calculation import RouteCalculation
from Map.icebergs import SpawnIcebergs
from Map.ships import SpawnShips
from Map.ShadowLayer import FogOfWar
from Map.route import SetSailSpeed
from tools import Loadify, TransformImage
import math
import random
import numpy
from Menu.savesettings import GetValues

class Map(object):
    """Class that shows the map with all corresponding objects"""
    def __init__(self, screen, x_res = 1920, y_res = 1080):
        self.BLACK = (0, 0, 0)
        self.WHITE = (255,255,255)
        self.GREEN = (0,255,0)
        self.background_image = Loadify("Background.png")
        self.background_image = TransformImage(self.background_image, x_res, y_res)
        self.grid_colour = (0, 0, 0)  # black
        self.iceberg_colour = (255, 255, 255)
        self.iceberg_rect = pygame.Rect(50, 50, 50, 50)
        self.screen = screen  # imported from Menu
        self.ship_list = SpawnShips(int(GetValues()[0])) # creates a list
        self.iceberg_list = SpawnIcebergs(int(GetValues()[1]), self.ship_list)  # creates a list
        self.rect_list = []
        self.vector_list = []
        self.rect_list = []
        self.cloud_list = []
        for i in range(0,20):
            temp_x = i * x_res/20
            for i in range (0,12):
                temp_y = i * y_res/12
                self.cloud_list.append(FogOfWar(temp_x, temp_y))
        self.clock = pygame.time.Clock()
        for ship in self.ship_list:
            ship.scan()

#Create gridlines
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


#Shows the fog of war and sets updates opacity
    def ShowFOW(self):
        for cloud in self.cloud_list:
            cloud.image.set_alpha(cloud.opacity)
            self.screen.blit(cloud.image, [cloud.x_coord, cloud.y_coord])


    def show_objects(self):
        for iceberg in self.iceberg_list:
            #Refresh the location of icebergs
            self.screen.blit(iceberg.image, [iceberg.x_coord, iceberg.y_coord])
            for rect, vector in self.rect_list:
                if rect.collidepoint(iceberg.x_coord, iceberg.y_coord):
                    iceberg.x_vec = vector[0]
                    iceberg.y_vec = vector[1]
            #Move icebergs
            iceberg.x_coord += iceberg.x_vec * 0.005
            iceberg.rect.x = iceberg.x_coord
            iceberg.y_coord += iceberg.y_vec * 0.005
            iceberg.rect.y = iceberg.y_coord

        for ship in self.ship_list:
            self.screen.blit(ship.image, [ship.x_coord, ship.y_coord])#           if  ship.x_destination -10 <= ship.x_coord <- ship.x_destination +10:
#                if ship.y_destination - 10 <= ship.y_coord < - ship.y_destination + 10:
 #                   =True
            #Update and move sonar blips
            for sonar in ship.sonar_list:
                sonar.Update(self.iceberg_list)
                if sonar.final_coords != [0,0] and sonar.change_x == 0 and sonar.change_y == 0:
                    pygame.draw.circle(self.screen, ship.colour, sonar.final_coords, 2)
                else:
                    pygame.draw.circle(self.screen, ship.colour, [sonar.rect_x, sonar.rect_y], 2)
                for cloud in self.cloud_list:
                    if sonar.rect_x-50<= cloud.x_coord <= sonar.rect_x+50:
                        if sonar.rect_y-50 <= cloud.y_coord <= sonar.rect_y+50:
                            cloud.opacity -= 30
                            if cloud.opacity < 50:
                                #to boost performance, remove the transparent clouds
                                self.cloud_list.remove(cloud)

            SetSailSpeed(ship)
            ship.sail()

    #Repeating loop to keep objects on map active and updating
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
            self.ShowFOW()
            for ship in self.ship_list:
                pygame.draw.circle(self.screen, self.GREEN, [ship.x_finaldestination, ship.y_finaldestination], 5)  # Draws endpoint
            if show == True:
                for iceberg in self.iceberg_list:
                    self.screen.blit(iceberg.image, [iceberg.x_coord, iceberg.y_coord])
            #Allows manual ping
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

            #Pings after a set amount of ticks
            count += 1
            if count == 200:
                 for ship in self.ship_list:
                    New_Coords = RouteCalculation(ship.sonar_list,SetSailSpeed(ship),ship.x_coord,ship.y_coord) #math.atan(ship.y_finaldestination/ship.x_finaldestination)
                    ship.x_destination = New_Coords[0]
                    ship.y_destination = New_Coords[1]
                    ship.sonar_list = []
                    ship.scan()

                 count = 0
            #Sets tickrate
            self.clock.tick(100)
            pygame.display.update()

        pygame.quit()
        quit()

