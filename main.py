"""
18/7, 19/7, 20/7, 21/7, 25/7, 26/7, 27/7
"""

import pygame
import random as rand

import difficulty1p
import difficulty2p
import highscore
import instruction

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
BUTTON_WIDTH = 500
BUTTON_HEIGHT = 50
BUTTON1_X = 125
BUTTON2_X = 425
BUTTON1_Y = 250
BUTTON2_Y = 325
BUTTON3_Y = 400
COLOUR = (192, 192, 192)
TEXT = (0, 0, 0)
SKY = (137, 235, 255)

objs = []
start_time = 0

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Key Planes")
Clock = pygame.time.Clock()
bg = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
CONTENT = pygame.font.SysFont('Verdana', 25)
HEADING = pygame.font.SysFont("Verdana", 35)
TITLE = pygame.font.SysFont("Verdana", 45)
NAME = pygame.font.SysFont("Forte", 90)


class Plane:
    def __init__(self, y, vel):
        self.x = WINDOW_WIDTH
        self.y = y
        self.vel = vel

    def draw(self, win):
        win.blit(pygame.image.load("image/plane.png"), (self.x, self.y))


# display GUI
def display():
    window.fill(SKY)
    for obj in objs:
        obj.draw(window)
    game_name = NAME.render("KEY PLANES", False, (255, 153, 51))
    window.blit(game_name, (145, 75))
    pygame.draw.rect(window, COLOUR, [BUTTON1_X, BUTTON1_Y, BUTTON_WIDTH / 2, BUTTON_HEIGHT])
    single = HEADING.render("1 PLAYER", False, TEXT)
    window.blit(single, (165, 250))
    pygame.draw.rect(window, COLOUR, [BUTTON2_X, BUTTON1_Y, BUTTON_WIDTH / 2, BUTTON_HEIGHT])
    multi = HEADING.render("2 PLAYER", False, TEXT)
    window.blit(multi, (470, 250))
    pygame.draw.rect(window, COLOUR, [BUTTON1_X, BUTTON2_Y, BUTTON_WIDTH / 2, BUTTON_HEIGHT])
    how = HEADING.render("HOW TO PLAY", False, TEXT)
    window.blit(how, (125, 325))
    pygame.draw.rect(window, COLOUR, [BUTTON2_X, BUTTON2_Y, BUTTON_WIDTH / 2, BUTTON_HEIGHT])
    highscore = HEADING.render("HIGHSCORE", False, TEXT)
    window.blit(highscore, (445, 325))
    pygame.draw.rect(window, COLOUR, [BUTTON1_X, BUTTON3_Y, BUTTON_WIDTH + 50, BUTTON_HEIGHT])
    quit_text = HEADING.render("QUIT", False, TEXT)
    window.blit(quit_text, (350, 400))
    pygame.display.update()


# what happens when mouse clicks on button
def mouse_click(mouse):
    global run
    if BUTTON1_X <= mouse[0] <= BUTTON1_X + BUTTON_WIDTH + 50 and BUTTON3_Y <= mouse[1] <= BUTTON3_Y + BUTTON_HEIGHT:
        run = False
    elif BUTTON1_X <= mouse[0] <= BUTTON1_X + BUTTON_WIDTH / 2:
        if BUTTON1_Y <= mouse[1] <= BUTTON1_Y + BUTTON_HEIGHT:
            difficulty1p.main()
        elif BUTTON2_Y <= mouse[1] <= BUTTON2_Y + BUTTON_HEIGHT:
            instruction.main()
    elif BUTTON2_X <= mouse[0] <= BUTTON2_X + BUTTON_WIDTH / 2:
        if BUTTON1_Y <= mouse[1] <= BUTTON1_Y + BUTTON_HEIGHT:
            difficulty2p.main()
        elif BUTTON2_Y <= mouse[1] <= BUTTON2_Y + BUTTON_HEIGHT:
            highscore.main()
    else:
        pass


# shape of mouse
def mouse_shape(mouse):
    if BUTTON1_X <= mouse[0] <= BUTTON1_X + BUTTON_WIDTH + 50 and BUTTON3_Y <= mouse[1] <= BUTTON3_Y + BUTTON_HEIGHT:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    elif BUTTON1_X <= mouse[0] <= BUTTON1_X + BUTTON_WIDTH / 2:
        if BUTTON1_Y <= mouse[1] <= BUTTON1_Y + BUTTON_HEIGHT:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif BUTTON2_Y <= mouse[1] <= BUTTON2_Y + BUTTON_HEIGHT:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    elif BUTTON2_X <= mouse[0] <= BUTTON2_X + BUTTON_WIDTH / 2:
        if BUTTON1_Y <= mouse[1] <= BUTTON1_Y + BUTTON_HEIGHT:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif BUTTON2_Y <= mouse[1] <= BUTTON2_Y + BUTTON_HEIGHT:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


# moving planes across screen
def move_plane():
    for obj in objs:
        if 0 < obj.x <= WINDOW_WIDTH:
            obj.x -= obj.vel
        else:
            objs.pop(objs.index(obj))


# creating planes
def create_plane():
    global start_time
    overlap = True
    if len(objs) == 0:
        objs.append(Plane(rand.randint(0, WINDOW_HEIGHT), rand.randint(3, 9)))
        start_time = pygame.time.get_ticks()
    else:
        if pygame.time.get_ticks() - start_time >= rand.randint(1000, 3000):
            obj_y = rand.randint(0, WINDOW_HEIGHT)
            while overlap:
                overlap = False
                for obj in objs:
                    if obj.y - 10 <= obj_y <= obj.y + 10:
                        obj_y = rand.randint(0, WINDOW_HEIGHT)
                        overlap = True
                        break
            objs.append(Plane(obj_y, rand.randint(3, 9)))
            start_time = pygame.time.get_ticks()


run = True
while run:
    Clock.tick(30)
    mouse = pygame.mouse.get_pos()

    mouse_shape(mouse)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            mouse_click(mouse)

    move_plane()

    create_plane()

    display()
