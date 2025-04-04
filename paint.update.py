import pygame
import sys
import math

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


def draw_square(start_pos, end_pos, color):
    side_length = min(end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])  # Ensure it's a square
    pygame.draw.rect(canvas, color, pygame.Rect(start_pos, (side_length, side_length)))


def draw_right_triangle(start_pos, end_pos, color):
    point1 = start_pos
    point2 = (start_pos[0], end_pos[1])
    point3 = (end_pos[0], end_pos[1])
    pygame.draw.polygon(canvas, color, [point1, point2, point3])


def draw_equilateral_triangle(center, size, color):
    height = math.sqrt(3) * size / 2
    point1 = (center[0] - size / 2, center[1] + height / 2)  # Left point
    point2 = (center[0] + size / 2, center[1] + height / 2)  # Right point
    point3 = (center[0], center[1] - height / 2)  # Top point
    pygame.draw.polygon(canvas, color, [point1, point2, point3])


def draw_rhombus(center, size, color):
    half_size = size / 2
    point1 = (center[0], center[1] - half_size)
    point2 = (center[0] + half_size, center[1])
    point3 = (center[0], center[1] + half_size)
    point4 = (center[0] - half_size, center[1])
    pygame.draw.polygon(canvas, color, [point1, point2, point3, point4])


drawing = False
rect_start = None
circle_center = None
erase_start_pos = None
shape_mode = None  # None, 'square', 'triangle', 'equilateral', 'rhombus'

while True:
    screen.fill(WHITE)
    screen.blit(canvas, (0, 0))
    draw_palette()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left Mouse Button
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

                # Set shape mode based on selected area
                if 10 <= event.pos[0] <= 50 and 70 <= event.pos[1] <= 110:
                    shape_mode = 'square'
                elif 70 <= event.pos[0] <= 110 and 70 <= event.pos[1] <= 110:
                    shape_mode = 'triangle'
                elif 130 <= event.pos[0] <= 170 and 70 <= event.pos[1] <= 110:
                    shape_mode = 'equilateral'
                elif 190 <= event.pos[0] <= 230 and 70 <= event.pos[1] <= 110:
                    shape_mode = 'rhombus'

                if eraser_mode:
                    erase_start_pos = event.pos

        if event.type == pygame.MOUSEMOTION:
            if drawing:
                if shape_mode == 'square' and rect_start:
                    screen.fill(WHITE)
                    screen.blit(canvas, (0, 0))
                    draw_palette()
                    draw_square(rect_start, event.pos, current_color)

                elif shape_mode == 'triangle' and rect_start:
                    screen.fill(WHITE)
                    screen.blit(canvas, (0, 0))
                    draw_palette()
                    draw_right_triangle(rect_start, event.pos, current_color)

                elif shape_mode == 'equilateral' and rect_start:
                    screen.fill(WHITE)
                    screen.blit(canvas, (0, 0))
                    draw_palette()
                    size = int(math.sqrt((event.pos[0] - rect_start[0])**2 + (event.pos[1] - rect_start[1])**2))
                    draw_equilateral_triangle(rect_start, size, current_color)

                elif shape_mode == 'rhombus' and rect_start:
                    screen.fill(WHITE)
                    screen.blit(canvas, (0, 0))
                    draw_palette()
                    size = int(math.sqrt((event.pos[0] - rect_start[0])**2 + (event.pos[1] - rect_start[1])**2))
                    draw_rhombus(rect_start, size, current_color)

                if eraser_mode and erase_start_pos:
                    screen.fill(WHITE)
                    screen.blit(canvas, (0, 0))
                    draw_palette()
                    erase(erase_start_pos, event.pos)

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if shape_mode == 'square' and rect_start:
                    draw_square(rect_start, event.pos, current_color)
                    rect_start = None
                elif shape_mode == 'triangle' and rect_start:
                    draw_right_triangle(rect_start, event.pos, current_color)
                    rect_start = None
                elif shape_mode == 'equilateral' and rect_start:
                    size = int(math.sqrt((event.pos[0] - rect_start[0])**2 + (event.pos[1] - rect_start[1])**2))
                    draw_equilateral_triangle(rect_start, size, current_color)
                    rect_start = None
                elif shape_mode == 'rhombus' and rect_start:
                    size = int(math.sqrt((event.pos[0] - rect_start[0])**2 + (event.pos[1] - rect_start[1])**2))
                    draw_rhombus(rect_start, size, current_color)
                    rect_start = None
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
