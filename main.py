import pygame
import pickle
from draughts.constants import WIDTH, HEIGHT, BLACK, WHITE
from draughts.board import Board

FPS = 60

# Creates a window according to WIDTH and HEIGHT constants and captions the window "Draughts"
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draughts")

def colPosition(mousePos):
    """Gets column index value for where player clicks on board"""

    x = mousePos[0]
    if x >= 0 and x <= 100:
        colIndex = 0
    elif x > 100 and x <= 200:
        colIndex = 1
    elif x > 200 and x <= 300:
        colIndex = 2
    elif x > 300 and x <= 400:
        colIndex = 3
    elif x > 400 and x <= 500:
        colIndex = 4
    elif x > 500 and x <= 600:
        colIndex = 5
    elif x > 600 and x <= 700:
        colIndex = 6
    elif x > 700 and x <= 800:
        colIndex = 7

    return colIndex

def rowPosition(mousePos):
    """Gets row index value for where player clicks on board"""

    y = mousePos[1]
    if y >=0 and y <= 100:
        rowIndex = 0
    if y >=100 and y <= 200:
        rowIndex = 1
    if y >=200 and y <= 300:
        rowIndex = 2
    if y >=300 and y <= 400:
        rowIndex = 3
    if y >=400 and y <= 500:
        rowIndex = 4
    if y >=500 and y <= 600:
        rowIndex = 5
    if y >=600 and y <= 700:
        rowIndex = 6
    if y >=700 and y <= 800:
        rowIndex = 7

    return rowIndex


def main():

    # Main structure referenced but adapted from Tech with Tim Tutorial (see project documentation)

    run = True
    # Defining clock makes sure game runs consistently across different machines
    clock = pygame.time.Clock()

    gameBoard = Board()
    firstClick = True

    # Allows Black to move first
    turn = True

    gameOver = False
    currentPiece = []
    while run:

        # Stops the game from running at more than 60 FPS
        clock.tick(FPS)

        # Used to check for player input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Used to check if piece has been clicked on, if it is the turn of that colour
            # piece, what move player wants to make and if move is valid
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if firstClick:
                    mousePos = pygame.mouse.get_pos()
                    pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
                    firstClick = False
                    rowIndex = rowPosition(mousePos)
                    colIndex = colPosition(mousePos)
                    currentPiece = rowIndex, colIndex
                else:
                    mousePos = pygame.mouse.get_pos()
                    pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    firstClick = True
                    rowIndex = rowPosition(mousePos)
                    colIndex = colPosition(mousePos)
                    validMove = gameBoard.move(currentPiece[0], currentPiece[1], rowIndex, colIndex, turn)
                    if turn == True and validMove == True:
                        turn = False
                    elif turn == True and validMove == False:
                        turn = True
                    elif turn == False and validMove == True:
                        turn = True
                    elif turn == False and validMove == False:
                        turn = False

            # Used to detect keyboard input
            elif event.type == pygame.KEYDOWN:

                # Save game and turn
                if event.key == pygame.K_s:
                    save = open("save.dat", "wb")
                    pickle.dump(gameBoard, save)
                    pickle.dump(turn, save)
                    save.close()

                # Load game and turn
                elif event.key == pygame.K_l:
                    save = open("save.dat", "rb")
                    gameBoard = pickle.load(save)
                    turn = pickle.load(save)

        # Updates the display window with player moves
        if gameOver == False:
            gameBoard.draw(WIN)
            pygame.display.update()

        # If Black wins display result
        if gameBoard.whitePieces == 0:
            pygame.font.init()
            resultsBox = pygame.display.set_mode((WIDTH, HEIGHT))
            font = pygame.font.SysFont("arial", 50)
            text = font.render("Black Wins", True, BLACK, WHITE)
            textBox = text.get_rect()
            textBox.center = (WIDTH // 2, HEIGHT // 2)
            resultsBox.fill(BLACK)
            resultsBox.blit(text, textBox)
            pygame.display.update()
            gameOver = True

        # If White wins display result
        elif gameBoard.blackPieces == 0:
            pygame.font.init()
            resultsBox = pygame.display.set_mode((WIDTH, HEIGHT))
            font = pygame.font.SysFont("arial", 50)
            text = font.render("White Wins", True, BLACK, WHITE)
            textBox = text.get_rect()
            textBox.center = (WIDTH // 2, HEIGHT // 2)
            resultsBox.fill(BLACK)
            resultsBox.blit(text, textBox)
            pygame.display.update()
            gameOver = True

    pygame.quit()

main()