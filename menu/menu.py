import pygame

class Init():
    def __init__(self):
        self.background = "menu/iceburg.jpg"
        self.button =
        self.text = "Start Simulation"


    def Initialise(self):
        """Main Menu"""


        def MainMenu(screen):
            image1 = Initialise.upgrade_bars_images
            image2 = Initialise.buttons_images
            image3 = Initialise.upgrade_levels_text_images
            background_image = Loadify("Images/Backgrounds/main menu.png")
            background_image = TransformImage(background_image, Initialise.width, Initialise.height)

            MainMenuMusic()
            LBLUE = (0, 204, 204)
            BLACK = (0, 0, 0)

            font1 = RenderFont("Race Menu", 20, BLACK)
            font2 = RenderFont("Open Settings Menu [2]", 20, BLACK)
            font3 = RenderFont("Upgrades [3]", 20, BLACK)
            font4 = RenderFont("Shop [4]", 20, BLACK)
            font5 = RenderFont("Staff [5]", 20, BLACK)

            button_list = []
            for num in range(5):
                button_list.append(pygame.Rect(950, 150 * num + 150, 200, 50))

            on_main_menu = True
            click = False
            while on_main_menu:

                screen.blit(background_image, [0, 0])

                mx, my = pygame.mouse.get_pos()
                for button in button_list:
                    pygame.draw.rect(screen, (255, 0, 0), button)
                    if button.collidepoint(mx, my):
                        pygame.draw.rect(screen, (0, 255, 0), button)
                        if click:
                            if button_list.index(button) == 0:
                                RaceMenu(screen).DisplayWindow()
                            elif button_list.index(button) == 1:
                                SettingsMenu(screen)
                            elif button_list.index(button) == 2:
                                UpgradesMenu(screen, image1, image2, image3).ShowWindow()
                            elif button_list.index(button) == 3:
                                ShopMenu(screen).ShowWindow()
                            elif button_list.index(button) == 4:
                                StaffMenu(screen).DisplayWindow()

                screen.blit(font1, [950, 150])
                screen.blit(font2, [950, 300])
                screen.blit(font3, [950, 450])
                screen.blit(font4, [950, 600])
                screen.blit(font5, [950, 750])

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
