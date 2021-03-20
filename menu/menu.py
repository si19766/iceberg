import pygame
from tools import Loadify, TransformImage, RenderFont, ButtonCentre, ButtonSpacing
from Map.map import Map
from menu.savesettings import GetRes

class Menu():
    def __init__(self, screen):
        self.background_image = Loadify("menu/iceburg.jpg")
        self.background_image = TransformImage(self.background_image, int(GetRes()[0]), int(GetRes()[1]))
        self.screen = screen
        self.text = "Start Simulation"
        self.LBLUE = (0, 204, 204)
        self.BLACK = (0, 0, 0)
        self.font1 = pygame.font.SysFont('Ariel', 35)


    def MainMenu(self):

        rendered_font = RenderFont(self.font1, self.text, self.BLACK)
        button_width = 200
        button_height = 50
        number_of_buttons = 2
        button_list = []
        for num in range(number_of_buttons):
            button_list.append(pygame.Rect(ButtonCentre(button_width), ButtonSpacing(number_of_buttons) * (num+1) - (button_height/2), button_width, button_height))

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
                            Map(self.screen).Run()

            for num in range(number_of_buttons):
                if num == 0:
                    self.text = "Start Simulation"
                elif num == 1:
                    self.text = ".."
                else:
                    self.text = "..."
                rendered_font = RenderFont(self.font1, self.text, self.BLACK)
                self.screen.blit(rendered_font, [ButtonCentre(button_width), ButtonSpacing(number_of_buttons) * (num+1) - (button_height/2)])

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

