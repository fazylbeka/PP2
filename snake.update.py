import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")


WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
BLUE = (50, 153, 213)
BLACK = (0, 0, 0)


snake_block = 20
snake_speed = 15


font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def display_score(score, level):
    value = score_font.render("Score: " + str(score), True, WHITE)
    level_value = score_font.render("Level: " + str(level), True, WHITE)
    screen.blit(value, [0, 0])
    screen.blit(level_value, [WIDTH - 150, 0])


def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block, snake_block])


def generate_food():
    food_x = round(random.randrange(0, WIDTH - snake_block) / 20.0) * 20.0
    food_y = round(random.randrange(0, HEIGHT - snake_block) / 20.0) * 20.0
    food_weight = random.randint(5, 20)  # Random weight between 5 and 20
    return food_x, food_y, food_weight


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])


def gameLoop():
    global snake_speed
    game_over = False
    game_close = False


    x1 = WIDTH / 2
    y1 = HEIGHT / 2
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1


    foodx, foody, food_weight = generate_food()


    score = 0
    level = 1

    clock = pygame.time.Clock()


    food_timer = time.time()

    while not game_over:

        while game_close:
            screen.fill(BLUE)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            display_score(score, level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0


        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True


        x1 += x1_change
        y1 += y1_change
        screen.fill(BLUE)


        pygame.draw.rect(screen, RED, [foodx, foody, snake_block, snake_block])


        if x1 == foodx and y1 == foody:
            foodx, foody, food_weight = generate_food()
            Length_of_snake += 1
            score += food_weight


            if score % 40 == 0:
                level += 1
                snake_speed += 5

            food_timer = time.time()


        if time.time() - food_timer > 5:
            foodx, foody, food_weight = generate_food()
            food_timer = time.time()


        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True


        draw_snake(snake_block, snake_List)
        display_score(score, level)

        pygame.display.update()


        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
