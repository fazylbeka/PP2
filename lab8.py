#RACER
import pygame
import random
from pygame.locals import *

pygame.init()
WIDTH,  HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RACER")

#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 255)

#игроки
player_width = 60
player_height = 70
player_x = WIDTH//2- player_width//2
player_y = HEIGHT - player_height-10
player_speed = 5

#кедергі
obstacle_width = 50
obstacle_height = 70
obstacle_speed = 5
obstacles =[]

font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
running = True
score = 0

def draw_player(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, player_width, player_height))

def draw_obstacles():
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)

def draw_score( score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed


    if random.randint(1, 20) == 1:
        obstacle_x = random.randint(0, WIDTH - obstacle_width)
        obstacle_y = -obstacle_height
        obstacles.append(pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    for obstacle in obstacles:
        obstacle.y += obstacle_speed
        if obstacle.colliderect(pygame.Rect(player_x, player_y, player_width, player_height)):
            print("Game Over!")
            running = False
        if obstacle.y > HEIGHT:
            obstacles.remove(obstacle)
            score += 1

    draw_player(player_x, player_y)
    draw_obstacles()
    draw_score(score)

    pygame.display.update()
    clock.tick(60)

pygame.quit()







