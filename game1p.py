import sys
import pygame
import random as rand

import gameover
import pause

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
COLOUR = (255, 0, 0)
TEXT = (0, 0, 0)
LENGTH = 10
SKY = (137, 235, 255)

objs = []
empty_objs = []
items = []
items_fall = []
letters = []
letter_num = []
key_list = []
start_time = 0
total_plane = 0
letter_range = []
velocity = []

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
Clock = pygame.time.Clock()


class Plane:
    def __init__(self, y, vel):
        self.x = WINDOW_WIDTH
        self.y = y
        self.vel = vel

    def draw(self, win):
        win.blit(pygame.image.load("image/plane.png"), (self.x, self.y))


class Drops:
    def __init__(self, y):
        self.x = WINDOW_WIDTH + 15
        self.y = y
        prob = rand.random()
        if prob < 0.35:
            self.type = 3
        elif 0.35 <= prob < 0.65:
            self.type = 1
        elif 0.65 <= prob < 0.8:
            self.type = 4
        elif 0.8 <= prob < 0.95:
            self.type = 2
        else:
            self.type = 5

    def draw(self, win):
        if self.type == 1:
            win.blit(pygame.image.load("image/poop.png"), (self.x, self.y))
        elif self.type == 2:
            win.blit(pygame.image.load("image/fire.png"), (self.x, self.y))
        elif self.type == 3:
            win.blit(pygame.image.load("image/coin.png"), (self.x, self.y))
        elif self.type == 4:
            win.blit(pygame.image.load("image/dollar.png"), (self.x, self.y))
        elif self.type == 5:
            win.blit(pygame.image.load("image/diamond.png"), (self.x, self.y))


class Alphabet:
    def __init__(self, x, y):
        self.x = WINDOW_WIDTH + x + 60
        self.y = y + 10
        self.type = rand.randint(1, 26)

    def draw(self, win):
        win.blit(pygame.image.load("./image/" + letter_image(self.type)), (self.x, self.y))


class User:
    def __init__(self, x, type):
        self.x = 175 + x
        self.y = 350
        self.type = type

    def draw(self, win):
        file = letter_image(self.type)
        win.blit(pygame.image.load("./image/key" + file), (self.x, self.y))


# getting image of letter
def letter_image(type):
    switcher = {
        1: "A.png",
        2: "B.png",
        3: "C.png",
        4: "D.png",
        5: "E.png",
        6: "F.png",
        7: "G.png",
        8: "H.png",
        9: "I.png",
        10: "J.png",
        11: "K.png",
        12: "L.png",
        13: "M.png",
        14: "N.png",
        15: "O.png",
        16: "P.png",
        17: "Q.png",
        18: "R.png",
        19: "S.png",
        20: "T.png",
        21: "U.png",
        22: "V.png",
        23: "W.png",
        24: "X.png",
        25: "Y.png",
        26: "Z.png",
    }
    return switcher.get(type)


# draw the objects on the screen
def display(lives, score):
    content = pygame.font.SysFont('Verdana', 25)
    window.fill(SKY)
    for obj in objs:
        obj.draw(window)
    for item in items:
        item.draw(window)
    for letter in letters:
        ind = letters.index(letter)
        for x in range(letter_num[ind]):
            letter[x].draw(window)
    for item in items_fall:
        item.draw(window)
    for obj in empty_objs:
        obj.draw(window)
    for key in key_list:
        key.draw(window)
    for x in range(lives):
        window.blit(pygame.image.load("image/heart.png"), (10 + (x * 40), 460))
    text = content.render('Score', False, TEXT)
    text_score = content.render(str(score), False, TEXT)
    lives = content.render("Lives", False, TEXT)
    window.blit(text, (720, 425))
    window.blit(text_score, (750, 460))
    window.blit(lives, (10, 425))
    pygame.display.update()


# delete a plane when off screen
def delete(ind):
    objs.pop(ind)
    items.pop(ind)
    letters.pop(ind)
    letter_num.pop(ind)


# create a plane
def create():
    overlap = True
    obj_y = rand.randint(0, 250)
    while overlap:
        overlap = False
        for obj in objs:
            if obj.y - 30 <= obj_y <= obj.y + 30:
                obj_y = rand.randint(0, 250)
                overlap = True
                break
    obj_num = rand.randint(letter_range[0], letter_range[1])
    group = []
    item = Drops(obj_y + 50)
    items.append(item)
    if item.type == 5:
        loop = letter_range[2]
        obj_vel = velocity[2]
    else:
        loop = obj_num
        obj_vel = rand.uniform(velocity[0], velocity[1])
    letter_num.append(loop)
    for x in range(1, loop + 1):
        gap = 30 * (x - 1)
        group.append(Alphabet(LENGTH * x + gap, obj_y))
    letters.append(group)
    objs.append(Plane(obj_y, obj_vel))


# identify key pressed
def keys_pressed(key):
    key_x = (len(key_list) - 1) * 60
    if key == pygame.K_SPACE:
        check()
        key_list.clear()
    if key == pygame.K_ESCAPE:
        return pause.main()
    if len(key_list) == 10:
        return 0
    if key == pygame.K_a:
        key_list.append(User(key_x, 1))
    if key == pygame.K_b:
        key_list.append(User(key_x, 2))
    if key == pygame.K_c:
        key_list.append(User(key_x, 3))
    if key == pygame.K_d:
        key_list.append(User(key_x, 4))
    if key == pygame.K_e:
        key_list.append(User(key_x, 5))
    if key == pygame.K_f:
        key_list.append(User(key_x, 6))
    if key == pygame.K_g:
        key_list.append(User(key_x, 7))
    if key == pygame.K_h:
        key_list.append(User(key_x, 8))
    if key == pygame.K_i:
        key_list.append(User(key_x, 9))
    if key == pygame.K_j:
        key_list.append(User(key_x, 10))
    if key == pygame.K_k:
        key_list.append(User(key_x, 11))
    if key == pygame.K_l:
        key_list.append(User(key_x, 12))
    if key == pygame.K_m:
        key_list.append(User(key_x, 13))
    if key == pygame.K_n:
        key_list.append(User(key_x, 14))
    if key == pygame.K_o:
        key_list.append(User(key_x, 15))
    if key == pygame.K_p:
        key_list.append(User(key_x, 16))
    if key == pygame.K_q:
        key_list.append(User(key_x, 17))
    if key == pygame.K_r:
        key_list.append(User(key_x, 18))
    if key == pygame.K_s:
        key_list.append(User(key_x, 19))
    if key == pygame.K_t:
        key_list.append(User(key_x, 20))
    if key == pygame.K_u:
        key_list.append(User(key_x, 21))
    if key == pygame.K_v:
        key_list.append(User(key_x, 22))
    if key == pygame.K_w:
        key_list.append(User(key_x, 23))
    if key == pygame.K_x:
        key_list.append(User(key_x, 24))
    if key == pygame.K_y:
        key_list.append(User(key_x, 25))
    if key == pygame.K_z:
        key_list.append(User(key_x, 26))
    return 0


# when keys are correctly pressed
def success(ind):
    letter_num.pop(ind)
    letters.pop(ind)
    items_fall.append(items[ind])
    items.pop(ind)
    empty_objs.append(objs[ind])
    objs.pop(ind)
    key_list.clear()


# check if item is released
def check():
    for letter in letters:
        test_letter = []
        test = False
        ind = letters.index(letter)
        for x in range(letter_num[ind]):
            test_letter.append(letter[x].type)
        if len(test_letter) == len(key_list):
            for x in range(len(key_list)):
                if test_letter[x] == key_list[x].type:
                    test = True
                else:
                    test = False
                    break
            if test:
                success(ind)
                break


def clear():
    global objs, empty_objs, items, items_fall, letters, letter_num, key_list
    objs = []
    empty_objs = []
    items = []
    items_fall = []
    letters = []
    letter_num = []
    key_list = []


def start(level):
    global total_plane, letter_range, velocity
    clear()
    if level == 1:
        total_plane = 3
        letter_range = [2, 5, 6]
        velocity = [3, 6, 7]
    elif level == 2:
        total_plane = 4
        letter_range = [3, 6, 8]
        velocity = [4, 7, 8]
    elif level == 3:
        total_plane = 4
        letter_range = [3, 6, 10]
        velocity = [5, 8, 9]
    main(level)


def exit_plane():
    # move empty planes
    for obj in empty_objs:
        if 0 < obj.x <= 800:
            obj.x -= obj.vel + 1
        else:
            empty_objs.pop(empty_objs.index(obj))


def create_plane():
    global start_time
    # create planes
    if len(objs) == 0:
        create()
        start_time = pygame.time.get_ticks()
    else:
        if len(objs) < total_plane:
            if pygame.time.get_ticks() - start_time >= rand.randint(500, 2000):
                create()
                start_time = pygame.time.get_ticks()


def main(level):
    fall_vel = 5
    score = 0
    lives = 3

    choice = 0
    final_run = False
    run = True
    while run:
        Clock.tick(30)

        if lives == 0:
            run = False
            final_run = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                key = event.key
                choice = keys_pressed(key)

        if choice == 2 or choice == -1:
            run = False

        # move objects
        for obj in objs:
            index = objs.index(obj)
            if -60 < obj.x <= 800:
                obj.x -= obj.vel
                items[index].x -= obj.vel
                for i in range(letter_num[index]):
                    letters[index][i].x -= obj.vel
            else:
                if items[index].type == 3 or items[index].type == 4:
                    lives -= 1
                    delete(index)
                else:
                    delete(index)

        # move falling items
        for item in items_fall:
            if item.x < 0:
                item.x = 0
            if 0 <= item.y <= 400:
                item.y += fall_vel
            else:
                if item.type == 1:
                    lives -= 1
                elif item.type == 2:
                    lives -= 1
                    score -= 5
                elif item.type == 3:
                    score += 1
                elif item.type == 4:
                    score += 5
                else:
                    lives += 1
                    score += 10
                items_fall.pop(items_fall.index(item))

        exit_plane()

        create_plane()

        display(lives, score)

    if final_run:
        gameover.init(level, score)

    if choice == 2:
        start(level)
