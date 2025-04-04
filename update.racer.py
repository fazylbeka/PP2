import random
import pygame
from pygame.locals import *

pygame.init()
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RACER")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 223, 0)  # Coin color


player_width = 60
player_height = 70
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

obstacle_width = 50
obstacle_height = 70
obstacle_speed = 5
obstacles = []


coin_radius = 10
coins = []


font = pygame.font.Font(None, 36)


clock = pygame.time.Clock()


running = True
score = 0
collected_coins = 0


def draw_player(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, player_width, player_height))


def draw_obstacles():
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)

def draw_coins():
    for coin in coins:
        pygame.draw.circle(screen, YELLOW, (coin['rect'].x, coin['rect'].y), coin_radius)


def draw_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))


def generate_coin():
    coin_x = random.randint(0, WIDTH - coin_radius * 2)
    coin_y = random.randint(-HEIGHT, -coin_radius * 2)
    weight = random.randint(1, 5)  # Random weight (value) for each coin
    return pygame.Rect(coin_x, coin_y, coin_radius * 2, coin_radius * 2), weight


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


    if random.randint(1, 30) == 1:
        coin, weight = generate_coin()
        coins.append({'rect': coin, 'weight': weight})


    for obstacle in obstacles[:]:
        obstacle.y += obstacle_speed
        if obstacle.colliderect(pygame.Rect(player_x, player_y, player_width, player_height)):
            print("Game Over!")
            running = False
        if obstacle.y > HEIGHT:
            obstacles.remove(obstacle)
            score += 1


    for coin in coins[:]:
        coin['rect'].y += 5
        if coin['rect'].colliderect(pygame.Rect(player_x, player_y, player_width, player_height)):
            collected_coins += 1
            score += coin['weight']
            coins.remove(coin)


    if collected_coins >= 5:
        obstacle_speed = 7


    draw_player(player_x, player_y)
    draw_obstacles()
    draw_coins()
    draw_score(score)


    pygame.display.update()


    clock.tick(60)


pygame.quit()
