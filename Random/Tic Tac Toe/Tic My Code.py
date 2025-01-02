import pygame as pg, sys
from pygame import *
import time


# Variables:
XO = 'x'
winner = None
draw = False
width = 400
height = 400
white = (255, 255, 255)
line_color = (10, 10, 10)

# The Board:
TTT = [[None]*3, [None]*3, [None]*3]

# The Window:
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height+100), 0, 32)
pg.display.set_caption('Tic Tac Toe')

# Load Images:
opening = pg.image.load('tic tac opening.png')
x_img = pg.image.load('X.png')
o_img = pg.image.load('O.png')

# Resinzing Images:
x_img = pg.transform.scale(x_img, (80,80))
o_img = pg.transform.scale(o_img, (80, 80))
opening = pg.transform.scale(opening, (width, height+100))

def game_opening():
    screen.blit(opening, (0, 0))
    pg.display.update()
    time.sleep(1)
    screen.fill(white)

    # Drawing Vertical Lines:
    pg.draw.line(screen, line_color, (width/3, 0), (width/3, height), 7)
    pg.draw.line(screen, line_color, (width/3*2, 0), (width/3*2, height), 7)

    # Drawing Horizontal Lines:
    pg.draw.line(screen, line_color, (0, height/3), (width, height/3), 7)
    pg.draw.line(screen, line_color, (0, height/3*2), (width, height/3*2) ,7)
    draw_status()

def draw_status():
    global draw

    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + " won!"
    if draw:
        message = 'Game Draw!'
    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (250, 255, 255))
    
    # Copy Rendered Message:
    screen.fill ((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center = (width/2, 500-50))
    screen.blit(text, text_rect)
    pg.display.update()

def check_win():
    global TTT, winner, draw

    # Check For Winning Rows:
    for row in range (0, 3):
        if ( (TTT [row] [0] == TTT [row] [1] == TTT [row] [2] ) and (TTT [row] [0] is not None) ):
            # This Row Win:
            winner = TTT [row] [0]
            pg.draw.line(screen, (250, 0, 0), (0, (row + 1)* height / 3 - height / 6, \
                                width, (row + 1) * height / 3 - height / 6), 4)
            break
    
    # Check For Winning Columns:
    for col in range (0, 3):
        if (TTT [0] [col] == TTT [1] [col] == TTT [2] [col]) and (TTT [0] [col] is not None):
            # This Column Wins:
            winner = TTT [0] [col]
            # Draw Winning Line:
            pg.draw.line(screen, (250, 0, 0), ((col + 1) * width / 3 - width / 6, 0),\
                      ((col + 1 ) * width / 3 - width / 6, height), 4)
            break
    # Check For Diagonal Wins:
    if (TTT [0] [0] == TTT [1] [1] == TTT [2] [2]) and (TTT [0] [0] is not None):
        # Game Won Left To Right:
        winner = TTT [0] [0]
        pg.draw.line(screen, (250, 70, 70), (50,50), (350, 350), 4)

    if ( TTT [0] [2] == TTT [1] [1] == [2] [0] ) and (TTT [0] [2] is not None):
        # Game Won Right To Left:
        winner [0] [2]
        pg.draw.line(screen, (250, 70, 70), (350,50), (50, 350), 4)

    if (all ([all (row) for row in TTT]) and winner is None):
        draw = True
    draw_status()

def drawOX(row, col):
    global TTT, OX
    if row == 1 :
        posx = 30
    if row == 2 :
        posx = width / 3 + 30
    if row == 3 :
        posx = width / 3 * 2 + 30
    
    if col == 1:
        posy = 30
    if col == 2 :
        posy = height / 3 + 30
    if col == 3 :
        posy = height / 3 * 2 + 30
    TTT [row - 1] [col - 1] = XO
    if (XO == 'x'):
        screen.blit(x_img, (posy, posx))
        XO = 'o'
    else:
        screen.blit(o_img, (posy, posx))
        XO = 'x'
    pg.display.update()
    # Print (posx, posy)
    # Print (TTT)


def user_click():
    # Get Mouse Location:
    x,y = pg.mouse.get_pos()

    # Get Column:
    if (x < width / 3):
        col = 1
    elif (x < width / 3 * 2):
        col = 2
    elif (x < width):
        col = 3
    else:
        col = None
    
    # Get Row:
    if (x < height / 3):
        row = 1
    elif (x < height / 3 * 2):
        row = 2
    elif (x < height):
        row = 3
    else:
        row = None
    # Print (row, col)

    if (row and col and TTT [row - 1 ] [col - 1] is None):
        global XO

        # Draw the x or y on Screen:
        drawXO(row, col)
        check_win()

    
def reset_game():
    global TTT, winner, XO, draw
    time.sleep(3)
    XO = 'x'
    draw = False
    game_opening()
    winner = None
    TTT = [[None] * 3, [None] * 3, [None] * 3]

game_opening()


# Run 4Ever:
while (True):
    for event in pg.event.get():
        if event.type == quit:
            pg.quit()
            sys.exit()
        elif event.type is MOUSEBUTTONDOWN:
            # The User Clicked, Place X or O:
            user_click()
            if (winner or draw):
                reset_game()

    pg.display.update()
    CLOCK.tick(fps)