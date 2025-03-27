
import pygame
import os
from datetime import datetime


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

ball_radius = 25
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed = 20

RED = (255, 0, 0)
WHITE = (255, 255, 255)

background = pygame.image.load("clock.png")
hand_sec = pygame.image.load("sec_hand.png")  # Правая рука (секунды)
hand_min = pygame.image.load("min_hand.png")  # Левая рука (минуты)

pygame.mixer.init()
music_files = ["track1.mp3", "track2.mp3", "track3.mp3"]
current_music_index = 0

def play_music():
    pygame.mixer.music.load(music_files[current_music_index])
    pygame.mixer.music.play(-1)

def stop_music():
    pygame.mixer.music.stop()


def next_music():
    global current_music_index
    current_music_index = (current_music_index + 1) % len(music_files)
    play_music()


def prev_music():
    global current_music_index
    current_music_index = (current_music_index - 1) % len(music_files)
    play_music()

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.now()
    seconds = now.second
    minutes = now.minute


    angle_second = seconds * 6
    angle_minute = minutes * 6


    rotated_second = pygame.transform.rotate(hand_sec, -angle_second)
    rotated_minute = pygame.transform.rotate(hand_min, -angle_minute)


    rect_second = rotated_second.get_rect(center=(400, 300))
    rect_minute = rotated_minute.get_rect(center=(400, 300))

    keys = pygame.key.get_pressed()


    if keys[pygame.K_UP] and ball_y - ball_radius > 0:
        ball_y -= ball_speed
    if keys[pygame.K_DOWN] and ball_y + ball_radius < HEIGHT:
        ball_y += ball_speed
    if keys[pygame.K_LEFT] and ball_x - ball_radius > 0:
        ball_x -= ball_speed
    if keys[pygame.K_RIGHT] and ball_x + ball_radius < WIDTH:
        ball_x += ball_speed


    if keys[pygame.K_p]:
        play_music()
    if keys[pygame.K_s]:
        stop_music()
    if keys[pygame.K_n]:
        next_music()
    if keys[pygame.K_b]:
        prev_music()


    screen.fill(WHITE)

    screen.blit(background, (0, 0))


    screen.blit(rotated_second, rect_second.topleft)
    screen.blit(rotated_minute, rect_minute.topleft)


    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)


    pygame.display.flip()


    clock.tick(60)

pygame.quit()



