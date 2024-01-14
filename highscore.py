import sys
import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
COLOUR = (192, 192, 192)
TEXT = (0, 0, 0)
SKY = (137, 235, 255)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
Clock = pygame.time.Clock()


def display(text):
    content = pygame.font.SysFont('Verdana', 25)
    heading = pygame.font.SysFont("Verdana", 35)
    title = pygame.font.SysFont("Verdana", 45, bold=True)
    window.fill(SKY)
    title = title.render('HIGHSCORE', False, TEXT)
    window.blit(title, (240, 50))
    single = heading.render("1 PLAYER", False, TEXT)
    window.blit(single, (250, 150))
    multi = heading.render("2 PLAYER", False, TEXT)
    window.blit(multi, (500, 150))
    easy = heading.render("EASY", False, TEXT)
    window.blit(easy, (20, 240))
    med = heading.render("MEDIUM", False, TEXT)
    window.blit(med, (20, 315))
    hard = heading.render("HARD", False, TEXT)
    window.blit(hard, (20, 390))
    for x in range(3):
        window.blit(content.render(text[x][:-1], False, TEXT), (320, 245 + (x * 75)))
    for x in range(3):
        y = 3 + x
        window.blit(content.render(text[y][:-1], False, TEXT), (570, 245 + (x * 75)))
    pygame.draw.rect(window, SKY, [10, 10, 100, 30])
    back = content.render("< BACK", False, TEXT)
    window.blit(back, (10, 10))
    pygame.display.update()


def score():
    file = open("score.txt", "r")
    return file.readlines()


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
    text = score()

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

        display(text)
