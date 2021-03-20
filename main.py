import pygame
from menu.menu import Menu
from menu.savesettings import GetRes

pygame.init()
width = int(GetRes()[0])
height = int(GetRes()[1])

mode = (GetRes()[2])
if mode == "fullscreen":
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode([width, height])

mainmenu = Menu(screen)
mainmenu.MainMenu()
