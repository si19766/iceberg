import pygame

def Loadify(img):
    return pygame.image.load(img).convert_alpha()


def TransformImage(img, x, y):
    return pygame.transform.scale(img, [x,y])

def RenderFont(font, text, colour):
    """Easy function that allows you to render a font quickly"""
    rendered_font = pygame.font.Font.render(font, text, True, colour)
    return rendered_font

def ButtonCentre(button_width):
    window_tuple = pygame.display.get_window_size()
    centre_x = window_tuple[0]/2
    button_centre = centre_x - button_width/2
    return button_centre

def ButtonSpacing(number_of_buttons):
    window_tuple = pygame.display.get_window_size()
    spacing = window_tuple[1]/(number_of_buttons+1)
    return spacing