import sys
import pygame

import game1p
import game2p

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
BUTTON_X = 300
BUTTON1_Y = 250
BUTTON2_Y = 350
COLOUR = (192, 192, 192)
TEXT = (0, 0, 0)
SKY = (137, 235, 255)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
Clock = pygame.time.Clock()
change = False


# record score if high score broken
def record(level, score):
    global change
    file = open("score.txt", "r")
    text = file.readlines()
    print(text[level-1])
    highscore = int(text[level - 1][:-1])
    if score > highscore:
        text[level - 1] = str(score) + "\n"
        highscore = score
        change = True
    file = open("score.txt", "w")
    file.writelines(text)
    return highscore


def display(score, highscore):
    global change
    content = pygame.font.SysFont('Verdana', 25)
    heading = pygame.font.SysFont("Verdana", 35)
    title = pygame.font.SysFont("Verdana", 45, bold=True)
    window.fill(SKY)
    gameover = title.render('GAME OVER', False, (255, 0, 0))
    window.blit(gameover, (245, 50))
    yourscore = heading.render("Your Score", False, TEXT)
    window.blit(yourscore, (265, 125))
    text_score = heading.render(str(score), False, TEXT)
    window.blit(text_score, (500, 125))
    yourscore = content.render("Best", False, TEXT)
    window.blit(yourscore, (300, 175))
    if change:
        new = content.render("NEW BEST!", False, (255, 0, 0))
        window.blit(new, (540, 175))
    text_score = content.render(str(highscore), False, TEXT)
    window.blit(text_score, (470, 175))
    pygame.draw.rect(window, COLOUR, [BUTTON_X, BUTTON1_Y, BUTTON_WIDTH, BUTTON_HEIGHT])
    retry = heading.render("RETRY", False, TEXT)
    window.blit(retry, (345, 250))
    pygame.draw.rect(window, COLOUR, [BUTTON_X, BUTTON2_Y, BUTTON_WIDTH, BUTTON_HEIGHT])
    quit_text = heading.render("QUIT", False, TEXT)
    window.blit(quit_text, (355, 350))
    pygame.display.update()


def mouse_click(mouse):
    if BUTTON_X <= mouse[0] <= BUTTON_X + BUTTON_WIDTH:
        if BUTTON1_Y <= mouse[1] <= BUTTON1_Y + BUTTON_HEIGHT:
            return 1
        elif BUTTON2_Y <= mouse[1] <= BUTTON2_Y + BUTTON_HEIGHT:
            return -1
        else:
            return 0
    else:
        return 0


def mouse_shape(mouse):
    if BUTTON_X <= mouse[0] <= BUTTON_X + BUTTON_WIDTH:
        if BUTTON1_Y <= mouse[1] <= BUTTON1_Y + BUTTON_HEIGHT:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif BUTTON2_Y <= mouse[1] <= BUTTON2_Y + BUTTON_HEIGHT:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


def main(level, score):
    if score < 0:
        score = 0

    highscore = record(level, score)
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

        if verdict == 0:
            pass
        else:
            run = False

        display(score, highscore)

    if verdict == 1:
        if level>3:
            game2p.start(level)
        else:
            game1p.start(level)


def init(level, score):
    main(level, score)
