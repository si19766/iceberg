import pygame
from tools import Loadify, TransformImage, RenderFont
from Map.map import Map


class Menu():
    def __init__(self):
        self.background_image = Loadify("menu/iceburg.jpg")
        self.background_image = TransformImage(self.background_image, 1000, 1000)
        self.screen = pygame.display.set_mode((1000, 1000))
        self.text = "Start Simulation"
        self.LBLUE = (0, 204, 204)
        self.BLACK = (0, 0, 0)
        self.font1 = RenderFont("Demo1", 20, self.BLACK)


    def MainMenu(self):

        button_list = []
        for num in range(5):
            button_list.append(pygame.Rect(950, 150 * num + 150, 200, 50))

        on_main_menu = True
        click = False
        while on_main_menu:

            self.screen.blit(self.background_image, [0, 0])

            mx, my = pygame.mouse.get_pos()
            for button in button_list:
                pygame.draw.rect(self.screen, (255, 0, 0), button)
                if button.collidepoint(mx, my):
                    pygame.draw.rect(self.screen, (0, 255, 0), button)
                    if click:
                        if button_list.index(button) == 0:
                            Map.Run()


            self.screen.blit(self.font1, [950, 150]

            click = False
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Game quits if user presses escape on the main screen
                        pygame.quit()
                        quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                pygame.display.update()

        MainMenu(Initialise.screen)
