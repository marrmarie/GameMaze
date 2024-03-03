import pygame as pg
from collections import deque
from random import choice

WIDTH = 1500
HEIGHT = 500
SIZE = [WIDTH, HEIGHT]
SQUARE_SIZE = 50
columns = WIDTH // SQUARE_SIZE
rows = HEIGHT // SQUARE_SIZE
pg.init()
screen = pg.display.set_mode(SIZE)
time = pg.time.Clock()


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # top, right, bottom, left
        self.walls = [True, True, True, True]
        self.visited = 0  # посещена клетка или нет

    def fill_current(self):
        f1  = self.x * SQUARE_SIZE
        f2 = self.y * SQUARE_SIZE
        pg.draw.rect(screen, 'black', [f1, f2, SQUARE_SIZE, SQUARE_SIZE])

    def draw_lines_and_cell(self):
        x = self.x * SQUARE_SIZE
        y = self.y * SQUARE_SIZE

        if self.visited == 1:
            pg.draw.rect(screen, 'black', (x, y, SQUARE_SIZE, SQUARE_SIZE))

        if self.walls[0]:
            pg.draw.line(screen, 'black', [x, y], [x + SQUARE_SIZE, y], 2)
        if self.walls[1]:
            pg.draw.line(screen, 'black', [x + SQUARE_SIZE, y], [x + SQUARE_SIZE, y + SQUARE_SIZE], 2)
        if self.walls[2]:
            pg.draw.line(screen, 'black', [x + SQUARE_SIZE, y + SQUARE_SIZE], [x, y + SQUARE_SIZE], 2)
        if self.walls[3]:
            pg.draw.line(screen, 'black', [x, y + SQUARE_SIZE], [x, y], 2)


grid = []
for i in range(rows):
    for j in range(columns):
        grid.append(Cell(i, j))
cell_now = grid[0]

queue = deque()
running = True
while running:
    screen.fill(pg.Color('pink'))
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
    for c in grid:
        c.draw_lines_and_cell()

    pg.display.flip()
    time.tick(30)