import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Application")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
COLOR_PALETTE = [RED, GREEN, BLUE, YELLOW, BLACK]


brush_size = 5
current_color = BLACK
eraser_mode = False


canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)



def draw_palette():
    x = 10
    y = 10
    for color in COLOR_PALETTE:
        pygame.draw.rect(screen, color, (x, y, 50, 50))
        x += 60



def draw_rectangle(start_pos, end_pos, color):
    pygame.draw.rect(canvas, color, pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])))



def draw_circle(center, radius, color):
    pygame.draw.circle(canvas, color, center, radius)



def erase(start_pos, end_pos):
    pygame.draw.rect(canvas, WHITE, pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])))



drawing = False
rect_start = None
circle_center = None
erase_start_pos = None

while True:
    screen.fill(WHITE)


    screen.blit(canvas, (0, 0))
    draw_palette()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # ЛКМ
                drawing = True
                rect_start = event.pos
                circle_center = event.pos


                if 10 <= event.pos[0] <= 50 and 10 <= event.pos[1] <= 50:
                    current_color = RED
                elif 70 <= event.pos[0] <= 110 and 10 <= event.pos[1] <= 50:
                    current_color = GREEN
                elif 130 <= event.pos[0] <= 170 and 10 <= event.pos[1] <= 50:
                    current_color = BLUE
                elif 190 <= event.pos[0] <= 230 and 10 <= event.pos[1] <= 50:
                    current_color = YELLOW
                elif 250 <= event.pos[0] <= 290 and 10 <= event.pos[1] <= 50:
                    current_color = BLACK


                if eraser_mode:
                    erase_start_pos = event.pos

        if event.type == pygame.MOUSEMOTION:
            if drawing:
                if rect_start:
                    screen.fill(WHITE)
                    screen.blit(canvas, (0, 0))
                    draw_palette()
                    draw_rectangle(rect_start, event.pos, current_color)

                if circle_center:
                    screen.fill(WHITE)
                    screen.blit(canvas, (0, 0))
                    draw_palette()
                    draw_circle(circle_center, int(((event.pos[0] - circle_center[0]) ** 2 + (
                                event.pos[1] - circle_center[1]) ** 2) ** 0.5), current_color)


                if eraser_mode and erase_start_pos:
                    screen.fill(WHITE)
                    screen.blit(canvas, (0, 0))
                    draw_palette()
                    erase(erase_start_pos, event.pos)

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if rect_start:
                    draw_rectangle(rect_start, event.pos, current_color)
                    rect_start = None
                elif circle_center:
                    draw_circle(circle_center, int(((event.pos[0] - circle_center[0]) ** 2 + (
                                event.pos[1] - circle_center[1]) ** 2) ** 0.5), current_color)
                    circle_center = None
                drawing = False


                if eraser_mode:
                    erase(erase_start_pos, event.pos)
                    erase_start_pos = None

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                eraser_mode = True
            if event.key == pygame.K_c:
                canvas.fill(WHITE)
            if event.key == pygame.K_d:
                eraser_mode = False


    pygame.display.update()
