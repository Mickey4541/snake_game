import pygame
import random
import time
from pygame.locals import *

pygame.init()  # initializing pygame
black = (0, 0, 0)
white = (255, 255, 255)
green = (41, 240, 26)
red = (201, 18, 18)
yellow = (239, 250, 32)

dis_width = 600  # defining window
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))  # displaying the screen
# time.sleep(10)
pygame.display.set_caption("Snake game with Rajan Bhandari")
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 10


font_style = pygame.font.SysFont("calibri", 26)
score_font = pygame.font.SysFont("comicsans", 30)


# print(pygame.font.get_fonts())

def my_score(score):
    value = score_font.render("Score:" + str(score), True, yellow)  # score visibility is true and color is blue
    dis.blit(value, [0, 0])


def message(msg, color):  # this is used to send font in line 57
    msg = font_style.render(msg, True, color)
    dis.blit(msg, [0, dis_height / 10])  # for printing message in centre of display




def my_snake(snake_block, snake_list):  # defining game_snake variable
        for x in snake_list:
            pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

def main_game():
        game_over = False
        game_close = False

        x1 = dis_width / 2  # defining snake position
        y1 = dis_height / 2  # by dividing with 2, the snake position is in center

        x1_change = 0  # defining the length of snake, how snake length changes
        y1_change = 0

        snake_list = []  # when snake eat food, length increases
        length_snake = 1  # initial snake length is 1

        """ here snake = 10, win_width = 600 so, 
        it generate random number from 0 to 590-- (600-10)= 590 """
        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

        # creating a loop until the game is not over
        while not game_over:

            while game_close == True:
                dis.fill(white)
                message("You lost the game !!! Press P to play and Q to Quit",red)
                my_score(length_snake - 1)  # this is when snake eat food length increase by 1
                pygame.display.update()  # This is to update the score

                for event in pygame.event.get():  # from locals import all the keys pressed
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_p:
                            main_game()  # control goes to line 42

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_LEFT:
                       x1_change = -snake_block  # snake moves toward (-) in axis
                       y1_change = 0  # 0 implies dont change

                   elif event.key == pygame.K_RIGHT:
                            x1_change = snake_block
                            y1_change = 0

                   elif event.key == pygame.K_UP:
                            x1_change = 0
                            y1_change = -snake_block

                   elif event.key == pygame.K_DOWN:
                            x1_change = 0
                            y1_change = snake_block

             # when the snake touches the wall
            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True

            x1 += x1_change
            y1 += y1_change
            dis.fill(black)

            pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
            snake_size = []
            snake_size.append(x1)  # for snake size , when snake eats it becomes +1 bigger( 1 append do)
            snake_size.append(y1)
            snake_list.append(snake_size)  # snake size is  append on snake length
            if len(snake_list) > length_snake:
                del snake_list[0]  # delete the length of snake which is on oth index


            my_snake(snake_block, snake_list)
            my_score(length_snake - 1)

            pygame.display.update()

            if x1 == foodx and y1 == foody:  # if the coordinate of snake and food match, snake eat food
                # when snake eat food, following two lines generate food in another random place
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                length_snake += 1

            clock.tick(snake_speed)

        pygame.QUIT()
        quit()

main_game()