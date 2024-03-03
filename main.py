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


    def check(self, x, y):
        if x < 0 or x > columns - 1 or y < 0 or y > rows - 1:
            return False
        return grid[x + y * columns]

    def go(self):
        nei  = []
        top = self.check(self.x, self.y - 1)
        right = self.check(self.x + 1, self.y)
        bottom = self.check(self.x, self.y + 1)
        left = self.check(self.x - 1, self.y)
        if top and not top.visited:
            nei.append(top)
        if right and not right.visited:
            nei.append(right)
        if bottom and not bottom.visited:
            nei.append(bottom)
        if left and not left.visited:
            nei.append(left)
        if len(nei) == 0:
            return False
        return choice(nei)

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
    cell_now.visited = 1
    cell_now.fill_current()
    next_c = cell_now.go()
    if next_c:
        next_c.visited = True
        cell_now = next_c
    pg.display.flip()
    time.tick(30)