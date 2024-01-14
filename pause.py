import sys
import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
BUTTON_X = 300
BUTTON1_Y = 150
BUTTON2_Y = 250
BUTTON3_Y = 350
COLOUR = (192, 192, 192)
TEXT = (0, 0, 0)
SKY = (137, 235, 255)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
Clock = pygame.time.Clock()


def display():
    heading = pygame.font.SysFont("Verdana", 35)
    title = pygame.font.SysFont("Verdana", 45, bold=True)
    window.fill(SKY)
    gameover = title.render('PAUSED', False, (255, 0, 0))
    window.blit(gameover, (300, 50))
    pygame.draw.rect(window, COLOUR, [BUTTON_X, BUTTON1_Y, BUTTON_WIDTH, BUTTON_HEIGHT])
    resume = heading.render("RESUME", False, TEXT)
    window.blit(resume, (325, 150))
    pygame.draw.rect(window, COLOUR, [BUTTON_X, BUTTON2_Y, BUTTON_WIDTH, BUTTON_HEIGHT])
    retry = heading.render("RETRY", False, TEXT)
    window.blit(retry, (345, 250))
    pygame.draw.rect(window, COLOUR, [BUTTON_X, BUTTON3_Y, BUTTON_WIDTH, BUTTON_HEIGHT])
    quit_text = heading.render("QUIT", False, TEXT)
    window.blit(quit_text, (355, 350))
    pygame.display.update()


def mouse_click(mouse):
    if BUTTON_X <= mouse[0] <= BUTTON_X + BUTTON_WIDTH:
        if BUTTON1_Y <= mouse[1] <= BUTTON1_Y + BUTTON_HEIGHT:
            return 1
        elif BUTTON2_Y <= mouse[1] <= BUTTON2_Y + BUTTON_HEIGHT:
            return 2
        elif BUTTON3_Y <= mouse[1] <= BUTTON3_Y + BUTTON_HEIGHT:
            return -1
    else:
        return 0


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
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


def main():
    run = True
    verdict = 0
    while run:
        mouse = pygame.mouse.get_pos()

        mouse_shape(mouse)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                verdict = mouse_click(mouse)

        if verdict != 0:
            run = False

        display()

    return verdict
