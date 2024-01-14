import sys
import pygame

import game2p

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
BUTTON_WIDTH = 250
BUTTON_HEIGHT = 50
BUTTON_X = 275
BUTTON1_Y = 150
BUTTON2_Y = 250
BUTTON3_Y = 350
COLOUR = (192, 192, 192)
TEXT = (0, 0, 0)
SKY = (137, 235, 255)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
Clock = pygame.time.Clock()


# display GUI
def display():
    content = pygame.font.SysFont('Verdana', 25)
    heading = pygame.font.SysFont("Verdana", 35)
    title = pygame.font.SysFont("Verdana", 45, bold=True)
    window.fill(SKY)
    title = title.render("2 PLAYER", False, TEXT)
    window.blit(title, (280, 50))
    pygame.draw.rect(window, COLOUR, [BUTTON_X, BUTTON1_Y, BUTTON_WIDTH, BUTTON_HEIGHT])
    easy = heading.render("EASY", False, TEXT)
    window.blit(easy, (355, 150))
    pygame.draw.rect(window, COLOUR, [BUTTON_X, BUTTON2_Y, BUTTON_WIDTH, BUTTON_HEIGHT])
    med = heading.render("MEDIUM", False, TEXT)
    window.blit(med, (330, 250))
    pygame.draw.rect(window, COLOUR, [BUTTON_X, BUTTON3_Y, BUTTON_WIDTH, BUTTON_HEIGHT])
    hard = heading.render("HARD", False, TEXT)
    window.blit(hard, (355, 350))
    pygame.draw.rect(window, SKY, [10, 10, 100, 30])
    back = content.render("< BACK", False, TEXT)
    window.blit(back, (10, 10))
    pygame.display.update()


# what happens when buttons clicked
def mouse_click(mouse):
    if BUTTON_X <= mouse[0] <= BUTTON_X + BUTTON_WIDTH:
        if BUTTON1_Y <= mouse[1] <= BUTTON1_Y + BUTTON_HEIGHT:
            game2p.start(1)
            return False
        elif BUTTON2_Y <= mouse[1] <= BUTTON2_Y + BUTTON_HEIGHT:
            game2p.start(2)
            return False
        elif BUTTON3_Y <= mouse[1] <= BUTTON3_Y + BUTTON_HEIGHT:
            game2p.start(3)
            return False
    elif 10 <= mouse[0] <= 110:
        if 10 <= mouse[1] <= 40:
            return False
    else:
        return True


# shape of mouse
def mouse_shape(mouse):
    if BUTTON_X <= mouse[0] <= BUTTON_X + BUTTON_WIDTH:
        if BUTTON1_Y <= mouse[1] <= BUTTON1_Y + BUTTON_HEIGHT:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif BUTTON2_Y <= mouse[1] <= BUTTON2_Y + BUTTON_HEIGHT:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif BUTTON3_Y <= mouse[1] <= BUTTON3_Y + BUTTON_HEIGHT:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    elif 10 <= mouse[0] <= 110:
        if 10 <= mouse[1] <= 40:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


def main():
    run = True
    while run:
        Clock.tick(30)
        mouse = pygame.mouse.get_pos()

        mouse_shape(mouse)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                run = mouse_click(mouse)

        display()
