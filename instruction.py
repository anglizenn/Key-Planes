import pygame
import sys

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
COLOUR = (192, 192, 192)
TEXT = (0, 0, 0)
SKY = (137, 235, 255)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
Clock = pygame.time.Clock()


def display():
    subcontent = pygame.font.SysFont("Verdana", 20, bold=True)
    content = pygame.font.SysFont('Verdana', 20)
    heading = pygame.font.SysFont("Verdana", 30)
    title = pygame.font.SysFont("Verdana", 45, bold=True)
    window.fill(SKY)
    title = title.render('HOW TO PLAY', False, TEXT)
    window.blit(title, (225, 50))
    control = heading.render("CONTROLS", False, TEXT)
    window.blit(control, (100, 125))
    single = subcontent.render("1 Player", False, TEXT)
    window.blit(single, (100, 175))
    keys = content.render("QWERTY - Type letters", False, TEXT)
    space = content.render("SPACE - Submit/Delete", False, TEXT)
    esc = content.render("ESC - Pause", False, TEXT)
    window.blit(keys, (100, 205))
    window.blit(space, (100, 235))
    window.blit(esc, (100, 265))
    multi = subcontent.render("2 Player", False, TEXT)
    window.blit(multi, (100, 315))
    arrow = content.render("< > - Move basket", False, TEXT)
    window.blit(arrow, (100, 345))
    item = heading.render("ITEMS", False, TEXT)
    window.blit(item, (450, 125))
    window.blit(pygame.image.load("./image/coin.png"), (450, 175))
    window.blit(pygame.image.load("./image/dollar.png"), (450, 225))
    window.blit(pygame.image.load("./image/diamond.png"), (450, 275))
    window.blit(pygame.image.load("./image/poop.png"), (450, 325))
    window.blit(pygame.image.load("./image/fire.png"), (450, 375))
    coin = content.render("1 point (Miss -1 life)", False, TEXT)
    dollar = content.render("5 points (Miss -1 life)", False, TEXT)
    diamond = content.render("10 points +1 life", False, TEXT)
    poop = content.render("-1 life", False, TEXT)
    fire = content.render("-1 life -5 points", False, TEXT)
    window.blit(coin, (500, 175))
    window.blit(dollar, (500, 225))
    window.blit(diamond, (500, 275))
    window.blit(poop, (500, 325))
    window.blit(fire, (500, 375))
    pygame.draw.rect(window, SKY, [10, 10, 100, 30])
    back = content.render("< BACK", False, TEXT)
    window.blit(back, (10, 10))
    pygame.display.update()


def mouse_click(mouse):
    if 10 <= mouse[0] <= 110:
        if 10 <= mouse[1] <= 40:
            return False
    else:
        return True


def mouse_shape(mouse):
    if 10 <= mouse[0] <= 110:
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
