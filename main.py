import pygame
import random


# initialize Pygame
pygame.init()

# build our display window
screen = pygame.display.set_mode((400, 400))

# clock
clock = pygame.time.Clock()

# fonts and dimensions things
food = pygame.Rect(random.randrange(0, 380, 20),
                    random.randrange(0, 380, 20), 20, 20)

font = pygame.font.Font(None, 36)
snake = [(200, 200)]
snake_dir = (0, 0)
score = 0

# reset game function
def reset_game():
    global snake, snake_dir, food, score
    snake = [(200, 200)]
    snake_dir = (0, 0)
    food.topleft = (random.randrange(0, 380, 20),
                        random.randrange(0, 380, 20), 20, 20)
    score = 0


# main game loop