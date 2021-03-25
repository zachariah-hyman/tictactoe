import pygame, sys, time
from pygame.locals import *

moves = []
rects = []
gameOver = False

# Initialize program
pygame.init()

# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()

# Setting up color objects
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Setup a 300x300 pixel display with caption
DISPLAYSURF = pygame.display.set_mode((300,400))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Tic Tac Toe")

def displayWin(c):
    gameOver = True
    myfont = pygame.font.SysFont(None,100) # use default system font, size 100
    mytext = myfont.render("{character} Wins!".format(character = c), True, GREEN)
    DISPLAYSURF.blit(mytext, (25,325))
    pygame.display.flip() # update the display

def checkWin(c):
    if moves[0] == c and moves[1] == c and moves[2] == c:
        displayWin(c)
    elif moves[3] == c and moves[4] == c and moves[5] == c:
        displayWin(c)
    elif moves[6] == c and moves[7] == c and moves[8] == c:
        displayWin(c)

def drawX(rect, xTurn):
    pygame.draw.line(DISPLAYSURF, RED, (rect.centerx - 25, rect.centery - 25), (rect.centerx + 25, rect.centery + 25), 2)

    pygame.draw.line(DISPLAYSURF, RED, (rect.centerx - 25, rect.centery + 25), (rect.centerx + 25, rect.centery - 25), 2)

    moves.pop(rects.index(rect))
    moves.insert(rects.index(rect), "X")
    checkWin('X')

def drawO(rect, xTurn):
    moves.pop(rects.index(rect))
    moves.insert(rects.index(rect), 'O')
    pygame.draw.circle(DISPLAYSURF, BLUE, rect.center, 25, 2)
    checkWin('O')

# define a main function
def main():
    # Draw grid
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(DISPLAYSURF, BLACK, (i*100, j*100, 100, 100), 2)
            rects.append(pygame.Rect((i*100, j*100), (98, 98)))
            moves.append(' ')

    screen = pygame.draw.rect(DISPLAYSURF, BLACK, (0, 300, 300, 100))

    xTurn = False

    while True:
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for rect in rects:
                    if rect.collidepoint(mouse_pos):
                        if xTurn == True:
                            drawX(rect, xTurn)
                            xTurn = False
                        elif xTurn == False:
                            drawO(rect, xTurn)
                            xTurn = True
                        print(moves)

        FramePerSec.tick(FPS)

if __name__=="__main__":
    # call the main function
    main()
