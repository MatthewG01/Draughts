import pygame
from .constants import BLACK, ROWS, COLUMNS, WHITE, SQUARE
from .piece import Piece

class Board(object):

    def __init__(self):
        self.gameBoard = []
        self.whitePieces = 12
        self.blackPieces = 12
        self.createBoard()

    def drawSquares(self, win):
        """Draws the squares of the board"""
        # Referenced from Tech with Tim Tutorial (see project documentation)
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, WHITE, (row * SQUARE, col * SQUARE, SQUARE, SQUARE))

    def createBoard(self):
        """Populates the board list with pieces"""
        # Referenced from Tech with Tim Tutorial (see project documentation)
        for row in range(ROWS):
            self.gameBoard.append([])
            for col in range(COLUMNS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.gameBoard[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.gameBoard[row].append(Piece(row, col, BLACK))
                    else:
                        self.gameBoard[row].append(0)
                else:
                    self.gameBoard[row].append(0)

    def draw(self, win):
        """Draws the board and pieces"""
        # Referenced from Tech with Tim Tutorial (see project documentation)
        self.drawSquares(win)
        for row in range(ROWS):
            for col in range(COLUMNS):
                pieceValue = self.gameBoard[row][col]
                if pieceValue != 0:
                    pieceValue.draw(win)

    def move(self, selectedPieceRow, selectedPieceCol, destRow, destCol, turn):
        """Moves pieces by swapping the selected piece and the destination in the board list"""
        selectedPiece = self.gameBoard[selectedPieceRow][selectedPieceCol]

        # Selected an empty space instead of a piece
        if selectedPiece == 0:
            return False

        # If it is Blacks' turn and selected piece is not a Black King
        if turn == True and selectedPiece.getColour() == (0, 0, 0) and selectedPiece.getKing() == False:

            # Pieces can only move diagonally into squares 1 valid move away from them
            if destRow < selectedPieceRow - 1 or destRow > selectedPieceRow or destCol > selectedPieceCol + 1 or destCol < selectedPieceCol -1 or destCol == selectedPieceCol or destRow == selectedPieceRow:
                return False

            # Pieces can move into valid empty squares
            if self.gameBoard[destRow][destCol] == 0:
                selectedPiece.move(destRow, destCol)
                self.gameBoard[selectedPieceRow][selectedPieceCol], self.gameBoard[destRow][destCol] = self.gameBoard[destRow][destCol], self.gameBoard[selectedPieceRow][selectedPieceCol]
                if destRow == 0:
                    selectedPiece.makeKing()
                    return True
                else:
                    return True

            # Prevents player from taking their own piece
            elif self.gameBoard[destRow][destCol] == (0, 0, 0):
                return False

            # Allows Black piece to take White piece
            elif self.gameBoard[destRow][destCol].getColour() == (255, 255, 255):

                # When selected piece is below and to the left of White piece
                if self.gameBoard[destRow - 1 ][destCol + 1] == 0 and selectedPieceCol == destCol - 1:
                    selectedPiece.move((destRow - 1), (destCol + 1 ))
                    self.gameBoard[selectedPieceRow][selectedPieceCol], self.gameBoard[destRow -1][destCol + 1] = self.gameBoard[destRow -1][destCol + 1], self.gameBoard[selectedPieceRow][selectedPieceCol]
                    self.gameBoard[destRow][destCol] = 0
                    self.whitePieces = self.whitePieces - 1
                    if destRow - 1 == 0:
                        selectedPiece.makeKing()
                        return True
                    else:
                        return True

                # When selected piece is below and to the right of White piece
                elif self.gameBoard[destRow - 1][destCol - 1] == 0 and selectedPieceCol == destCol + 1:
                    selectedPiece.move((destRow - 1), (destCol -1))
                    self.gameBoard[selectedPieceRow][selectedPieceCol], self.gameBoard[destRow -1 ][destCol - 1] = self.gameBoard[destRow -1 ][destCol - 1], self.gameBoard[selectedPieceRow][selectedPieceCol]
                    self.gameBoard[destRow][destCol] = 0
                    self.whitePieces = self.whitePieces - 1
                    if destRow - 1 == 0:
                        selectedPiece.makeKing()
                        return True
                    else:
                        return True

        # If it is Blacks' turn and selected piece is a Black King
        if turn == True and selectedPiece.getColour() == (0, 0, 0) and selectedPiece.getKing() == True:

            # Pieces can only move diagonally into squares 1 valid move away from them
            if destRow < selectedPieceRow - 1 or destRow > selectedPieceRow + 1 or destCol > selectedPieceCol + 1 or destCol < selectedPieceCol -1 or destCol == selectedPieceCol or destRow == selectedPieceRow:
                return False

            # Pieces can move into valid empty squares
            if self.gameBoard[destRow][destCol] == 0:
                selectedPiece.move(destRow, destCol)
                self.gameBoard[selectedPieceRow][selectedPieceCol], self.gameBoard[destRow][destCol] = self.gameBoard[destRow][destCol], self.gameBoard[selectedPieceRow][selectedPieceCol]
                return True

            # Prevents player from taking their own piece
            elif self.gameBoard[destRow][destCol] == (0, 0, 0):
                return False

            # Allows Black piece to take White piece
            elif self.gameBoard[destRow][destCol].getColour() == (255, 255, 255):

                # When selected piece is below and to the left of White piece
                if self.gameBoard[destRow - 1][destCol + 1] == 0 and selectedPieceRow == destRow + 1 and selectedPieceCol == destCol - 1:
                    selectedPiece.move((destRow - 1), (destCol + 1))
                    self.gameBoard[selectedPieceRow][selectedPieceCol], self.gameBoard[destRow - 1][destCol + 1] = self.gameBoard[destRow - 1][destCol + 1], self.gameBoard[selectedPieceRow][selectedPieceCol]
                    self.gameBoard[destRow][destCol] = 0
                    return True

                # When selected piece is above and to the left of White piece
                elif self.gameBoard[destRow + 1][destCol + 1] == 0 and selectedPieceRow == destRow - 1 and selectedPieceCol == destCol - 1:
                    selectedPiece.move((destRow + 1), (destCol + 1))
                    self.gameBoard[selectedPieceRow][selectedPieceCol], self.gameBoard[destRow + 1][destCol + 1] = self.gameBoard[destRow + 1][destCol + 1], self.gameBoard[selectedPieceRow][selectedPieceCol]
                    self.gameBoard[destRow][destCol] = 0
                    self.whitePieces = self.whitePieces - 1
                    return True

                # When selected piece is below and to the right of White piece
                elif self.gameBoard[destRow - 1][destCol - 1] == 0 and selectedPieceRow == destRow + 1 and selectedPieceCol == destCol + 1:
                    selectedPiece.move((destRow - 1), (destCol - 1))
                    self.gameBoard[selectedPieceRow][selectedPieceCol], self.gameBoard[destRow - 1][destCol - 1] = self.gameBoard[destRow - 1][destCol - 1], self.gameBoard[selectedPieceRow][selectedPieceCol]
                    self.gameBoard[destRow][destCol] = 0
                    self.whitePieces = self.whitePieces - 1
                    return True

                # When selected piece is above and to the right of White piece
                elif self.gameBoard[destRow + 1][destCol - 1] == 0 and selectedPieceRow == destRow -1 and selectedPieceCol == destCol + 1:
                    selectedPiece.move((destRow + 1), (destCol -1))
                    self.gameBoard[selectedPieceRow][selectedPieceCol], self.gameBoard[destRow + 1][destCol -1] = self.gameBoard[destRow + 1][destCol -1], self.gameBoard[selectedPieceRow][selectedPieceCol]
                    self.gameBoard[destRow][destCol] = 0
                    self.whitePieces = self.whitePieces - 1
                    return True
                else:
                    return False
            else:
                return False

        # If it is Whites' turn and selected piece is not a White King
        if turn == False and selectedPiece.getColour() == (255, 255, 255) and selectedPiece.getKing() == False:

            # Pieces can only move diagonally into squares 1 valid move away from them
            if destRow < selectedPieceRow or destRow > selectedPieceRow + 1 or destCol > selectedPieceCol + 1 or destCol < selectedPieceCol -1 or destCol == selectedPieceCol or destRow == selectedPieceRow:
                return False

            # Pieces can move into valid empty squares
            if self.gameBoard[destRow][destCol] == 0:
                selectedPiece.move(destRow, destCol)
                self.gameBoard[selectedPieceRow][selectedPieceCol], self.gameBoard[destRow][destCol] = self.gameBoard[destRow][destCol], self.gameBoard[selectedPieceRow][selectedPieceCol]
                if destRow == 7:
                    selectedPiece.makeKing()
                    return True
                else:
                    return True

            # Prevents player from taking their own piece
            elif self.gameBoard[destRow][destCol] == (255, 255, 255):
                return False

            # Allows White piece to take Black piece
            elif self.gameBoard[destRow][destCol].getColour() == (0, 0, 0):

                # When selected piece is above and to the right of Black piece
                if self.gameBoard[destRow + 1][destCol - 1] == 0 and selectedPieceCol == destCol + 1:
                    selectedPiece.move((destRow + 1), (destCol - 1))
                    self.gameBoard[selectedPieceRow][selectedPieceCol], self.gameBoard[destRow + 1][destCol - 1] = self.gameBoard[destRow + 1][destCol - 1], self.gameBoard[selectedPieceRow][selectedPieceCol]
                    self.gameBoard[destRow][destCol] = 0
                    self.blackPieces = self.blackPieces - 1
                    if destRow + 1 == 7:
                        selectedPiece.makeKing()
                        return True
                    else:
                        return True

                # When selected piece is above and to the left of Black piece
                elif self.gameBoard[destRow + 1][destCol + 1]  == 0 and selectedPieceCol == destCol - 1:
                    selectedPiece.move((destRow + 1), (destCol + 1))
                    self.gameBoard[selectedPieceRow][selectedPieceCol], self.gameBoard[destRow + 1][destCol + 1] = self.gameBoard[destRow + 1][destCol + 1], self.gameBoard[selectedPieceRow][selectedPieceCol]
                    self.gameBoard[destRow][destCol] = 0
                    self.blackPieces = self.blackPieces - 1
                    if destRow + 1 == 7:
                        selectedPiece.makeKing()
                        return True
                    else:
                        return True

        # If it is Whites' turn and selected piece is a White King
        if turn == False and selectedPiece.getColour() == (255, 255, 255) and selectedPiece.getKing() == True:

            # Pieces can only move diagonally into squares 1 valid move away from them
            if destRow < selectedPieceRow - 1 or destRow > selectedPieceRow + 1 or destCol > selectedPieceCol + 1 or destCol < selectedPieceCol -1 or destCol == selectedPieceCol or destRow == selectedPieceRow:
                return False

            # Pieces can move into valid empty squares
            if self.gameBoard[destRow][destCol] == 0:
                selectedPiece.move(destRow, destCol)
                self.gameBoard[selectedPieceRow][selectedPieceCol], self.gameBoard[destRow][destCol] = self.gameBoard[destRow][destCol], self.gameBoard[selectedPieceRow][selectedPieceCol]
                return True

            # Prevents player from taking their own piece
            elif self.gameBoard[destRow][destCol] == (255, 255, 255):
                return False

            # Allows White piece to take Black piece
            elif self.gameBoard[destRow][destCol].getColour() == (0, 0, 0):

                # When selected piece is below and to the left of Black piece
                if self.gameBoard[destRow - 1][destCol + 1] == 0 and selectedPieceRow == destRow + 1 and selectedPieceCol == destCol - 1:
                    selectedPiece.move((destRow - 1), (destCol + 1))
                    self.gameBoard[selectedPieceRow][selectedPieceCol], self.gameBoard[destRow - 1][destCol + 1] = self.gameBoard[destRow - 1][destCol + 1], self.gameBoard[selectedPieceRow][selectedPieceCol]
                    self.gameBoard[destRow][destCol] = 0
                    self.blackPieces = self.blackPieces - 1
                    return True

                # When selected piece is above and to the left of Black piece
                elif self.gameBoard[destRow + 1][destCol + 1] == 0 and selectedPieceRow == destRow -1 and selectedPieceCol == destCol - 1:
                    selectedPiece.move((destRow + 1), (destCol + 1))
                    self.gameBoard[selectedPieceRow][selectedPieceCol], self.gameBoard[destRow + 1][destCol + 1] = self.gameBoard[destRow + 1][destCol + 1], self.gameBoard[selectedPieceRow][selectedPieceCol]
                    self.gameBoard[destRow][destCol] = 0
                    self.blackPieces = self.blackPieces - 1
                    return True

                # When selected piece is below and to the right of Black piece
                elif self.gameBoard[destRow - 1][destCol - 1] == 0 and selectedPieceRow == destRow + 1 and selectedPieceCol == destCol + 1:
                    selectedPiece.move((destRow - 1), (destCol - 1))
                    self.gameBoard[selectedPieceRow][selectedPieceCol], self.gameBoard[destRow - 1][destCol - 1] = self.gameBoard[destRow - 1][destCol - 1], self.gameBoard[selectedPieceRow][selectedPieceCol]
                    self.gameBoard[destRow][destCol] = 0
                    self.blackPieces = self.blackPieces - 1
                    return True

                # When selected piece is above and to the right of Black piece
                elif self.gameBoard[destRow + 1][destCol - 1] == 0 and selectedPieceRow == destRow - 1 and selectedPieceCol == destCol + 1:
                    selectedPiece.move((destRow + 1), (destCol -1))
                    self.gameBoard[selectedPieceRow][selectedPieceCol], self.gameBoard[destRow + 1][destCol -1] = self.gameBoard[destRow + 1][destCol -1], self.gameBoard[selectedPieceRow][selectedPieceCol]
                    self.gameBoard[destRow][destCol] = 0
                    self.blackPieces = self.blackPieces - 1
                    return True
            else:
                return False


