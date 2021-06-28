import pygame
from .constants import WHITE, BLACK, SQUARE, CROWN

class Piece (object):

    PADDING = 10
    OUTLINE = 2

    def __init__(self, row, col, colour):
        # Referenced from Tech with Tim Tutorial (see project documentation)
        self.row = row
        self.col = col
        self.colour = colour
        self.king = False
        self.x = 0
        self.y = 0
        self.calcPosition()

    def getColour(self):
        """Allows other classes to access piece colour value"""
        return self.colour

    def getKing(self):
        """Allows other classes to access piece king value"""
        return self.king

    def calcPosition(self):
        """Centres pieces in middle of board squares"""
        # Referenced from Tech with Tim Tutorial (see project documentation)
        self.x = SQUARE * self.col + SQUARE // 2
        self.y = SQUARE * self.row + SQUARE // 2

    def makeKing(self):
        """Make a piece a King"""
        # Referenced from Tech with Tim Tutorial (see project documentation)
        self.king = True

    def draw(self, win):
        """Draws the pieces"""
        # Referenced from Tech with Tim Tutorial (see project documentation)
        radius = SQUARE // 2 - self.PADDING
        if self.colour == BLACK:
            pygame.draw.circle(win, WHITE, (self.x, self.y), radius + self.OUTLINE)
        else:
            pygame.draw.circle(win, BLACK, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.colour, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))

    def move(self, row, col):
        """Updates position of pieces"""
        # Referenced from Tech with Tim Tutorial (see project documentation)
        self.row = row
        self.col = col
        self.calcPosition()

    def __repr__(self):
        # Referenced from Tech with Tim Tutorial (see project documentation)
        return str(self.colour)