import pygame


class ParameterMenu(object):
    def __init__(self, screen, LBLUE):
        self.OnParameterMenu = True
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.screen = screen
        self.LBLUE = LBLUE
        self.width, self.height = pygame.display.get_surface().get_size()
        self.bar_list = []
        self.slider_list = []
        self.boatNumber = 5
        self.icebergNumber = 20
        self.height_divider = 8
        self.slider_width = self.width / 2
        self.slider_height = 10
        self.slider_radius = 10
        self.bar_limit = []
        self.slider_left_coord = (self.width / 2) - (self.slider_width / 2)
        self.slider_right_coord = (self.width / 2) + (self.slider_width / 2)

    def SliderMove(self, new_x, slider_number):

        if slider_number == 0:
            self.slider_list[0] = pygame.Rect(int(new_x) - 10, int(((self.height / self.height_divider) * 2)), 20, 20)
        if slider_number == 1:
            self.slider_list[1] = pygame.Rect(int(new_x) - 10, int(((self.height / self.height_divider) * 4)), 20, 20)

    def Slider_Calc(self):
        boatInc = self.boatNumber * self.slider_width
        icebergInc = self.icebergNumber * self.slider_width

        boatSliderPos = ((self.width / 2) - (self.slider_width / 2)) + boatInc
        icebergSliderPos = ((self.width / 2) - (self.slider_width / 2)) + icebergInc

        return boatSliderPos, icebergSliderPos

    def NewValue(self, new_x, slider):
        percentage_bar = (new_x - self.slider_left_coord) / (self.slider_right_coord - self.slider_left_coord)
        if slider == 0:
            self.boatNumber = percentage_bar
            # ChangeMasterLevel(self.boatNumber, self.icebergNumber)
        if slider == 1:
            self.icebergNumber = percentage_bar
            # ChangeMusicLevel(self.icebergNumber)

    def Control(self, click):
        """Function that lets user adjust volume levels"""
        mx, my = pygame.mouse.get_pos()

        for bars in self.bar_list:
            pygame.draw.rect(self.screen, self.BLACK, bars)

        for sliders in self.slider_list:
            pygame.draw.rect(self.screen, self.RED, sliders)
            if sliders.collidepoint(mx, my):
                if click:
                    if self.slider_list.index(sliders) == 0:
                        while click:
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            if self.bar_limit[0] > mouse_x:
                                mouse_x = self.bar_limit[0]
                            if self.bar_limit[1] < mouse_x:
                                mouse_x = self.bar_limit[1]
                            self.SliderMove(mouse_x, 0)
                            self.screen.fill(self.LBLUE)
                            for bars in self.bar_list:
                                pygame.draw.rect(self.screen, self.BLACK, bars)
                            for sliders in self.slider_list:
                                pygame.draw.rect(self.screen, self.RED, sliders)

                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONUP:
                                    self.NewValue(mouse_x, 0)
                                    click = False
                            pygame.display.update()

                    if self.slider_list.index(sliders) == 1:
                        while click:
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            if self.bar_limit[0] > mouse_x:
                                mouse_x = self.bar_limit[0]
                            if self.bar_limit[1] < mouse_x:
                                mouse_x = self.bar_limit[1]
                            self.SliderMove(mouse_x, 1)
                            self.screen.fill(self.LBLUE)
                            for bars in self.bar_list:
                                pygame.draw.rect(self.screen, self.BLACK, bars)
                            for sliders in self.slider_list:
                                pygame.draw.rect(self.screen, self.RED, sliders)

                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONUP:
                                    self.NewValue(mouse_x, 1)
                                    click = False
                            pygame.display.update()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.OnParameterMenu = False

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        return click

    def Bars(self):
        slider_height = self.slider_height
        slider_width = self.slider_width
        y_offset = slider_height / 2
        height_divider = self.height_divider
        self.bar_limit = [self.slider_left_coord, self.slider_right_coord]

        self.bar_list = [
            pygame.Rect(int(self.slider_left_coord), int(((self.height / height_divider) * 2) + y_offset), slider_width,
                        slider_height),
            pygame.Rect(int(self.slider_left_coord), int(((self.height / height_divider) * 4) + y_offset), slider_width,
                        slider_height)]

    def SlidersInit(self):

        self.slider_list = [
            pygame.Rect(100, 200, 20, 20),
            pygame.Rect(int(self.Slider_Calc()[1]), int(((self.height / self.height_divider) * 4)), 20, 20)]

    def DisplayWindow(self):
        self.Bars()
        self.SlidersInit()
        click = False
        while self.OnParameterMenu:
            self.screen.fill(self.LBLUE)
            click = self.Control(click)
            pygame.display.update()
            pygame.display.flip()
