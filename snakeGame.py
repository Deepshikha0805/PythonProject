import pygame as py
from pygame.locals import *
import time as tm
import random

py.init()
red = (255, 0, 0)
blue = (51, 153, 255)
black = (0,0,0)
green = (51, 102, 0)
yellow = (0, 255, 255)

win_width = 600
win_height = 400
window = py.display.set_mode((win_width, win_height))
py.display.set_caption("Snake Game")

snake = 10
snake_speed = 15
clock = py.time.Clock()

# fonts=py.font.get_fonts()
# print(fonts)
font_style = py.font.SysFont("comicsansms", 26)
score_font = py.font.SysFont("gabriola", 30)


def user_score(score):
    number = score_font.render("Score :", True, green)
    window.blit(number, [0, 0])


def game_snake(snake, snake_length_list):
    for x in snake_length_list:
        py.draw.rect(window, green, [x[0], x[1], snake, snake])


def message(msg):
    msg = font_style.render(msg, True, red)
    window.blit(msg, [win_width / 6, win_height / 3])


py.init()


def game_loop():
    gameOver = False
    gameClose = False

    x1 = win_width / 2
    y1 = win_height / 2

    x1_change = 0
    y1_change = 0

    snake_length_list = []
    snake_length = 1

    foodx = round(random.randrange(0, win_width - snake) / 10.0) * 10.0
    foody = round(random.randrange(0, win_height - snake) / 10.0) * 10.0

    while not gameOver:
        while gameClose == True:
            window.fill(black)
            message("you lost!!press P to Play again and Q to quit the game")
            user_score(snake_length - 1)
            py.display.update()

            for event in py.event.get():
                if event.type == py.KEYDOWN:
                    gameOver = True
                    gameClose = True
                if event.key == py.K_p:
                    game_loop()
        while not gameOver:
            for event in py.event.get():
                if event.type == py.QUIT:
                    gameOver = True
                if event.type == py.KEYDOWN:
                    if event.key == K_LEFT:
                        x1_change = -snake
                        y1_change = 0
                    if event.key == K_RIGHT:
                        x1_change = snake
                        y1_change = 0
                    if event.key == K_UP:
                        x1_change = 0
                        y1_change = -snake
                    if event.key == K_DOWN:
                        x1_change = 0
                        y1_change = snake

            if x1 > win_width or x1 < 0 or y1 > win_height or y1 < 0:
                gameClose = True
            x1 += x1_change
            y1 += y1_change
            window.fill(black)
            py.draw.rect(window, yellow, [foodx, foody, snake, snake])
            snake_size = []
            snake_size.append(x1)
            snake_size.append(y1)
            snake_length_list.append(snake_size)
            if len(snake_length_list) > snake_length:
                del snake_length_list[0]

            game_snake(snake, snake_length_list)
            user_score(snake_length - 1)

            py.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, win_width - snake) / 10.0) * 10.0
                foody = round(random.randrange(0, win_height - snake) / 10.0) * 10.0
                snake_length += 1
            clock.tick(snake_speed)

        py.quit()
        quit()


game_loop()



