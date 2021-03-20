import pygame

def Loadify(img):
    return pygame.image.load(img).convert_alpha()


def TransformImage(img, x, y):
    return pygame.transform.scale(img, [x,y])