import pygame

# Referenced from Tech with Tim Tutorial (see project documentation)

# Board Constants
WIDTH = 800
HEIGHT = 800
ROWS = 8
COLUMNS = 8
SQUARE = WIDTH/COLUMNS

# RGB values for pieces and board
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Loading crown image for king pieces, crown asset from Tech with Tim Tutorial (see project documentation)
CROWN = pygame.transform.scale(pygame.image.load("assets/crown.png"), (44, 25))