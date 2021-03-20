import pygame

def Loadify(img):
    return pygame.image.load(img).convert_alpha()


def TransformImage(img, x, y):
    return pygame.transform.scale(img, [x,y])

def RenderFont(text, size, colour):
    """Easy function that allows you to render a font quickly"""
    return pygame.font.Font("Data/Fonts/PixelFJVerdana12pt.ttf", size).render(text, True, colour)