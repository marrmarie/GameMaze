import pygame as pg
from collections import deque
from random import choice

WIDTH = 1202
HEIGHT = 902
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
        self.visited = False  # посещена клетка или нет

    def fill_current(self):
        f1 = self.x * SQUARE_SIZE
        f2 = self.y * SQUARE_SIZE
        pg.draw.rect(screen, 'black', [f1 + 2, f2 + 2, SQUARE_SIZE - 2, SQUARE_SIZE - 2])

    def draw_lines_and_cell(self):
        x = self.x * SQUARE_SIZE
        y = self.y * SQUARE_SIZE

        if self.visited:
            pg.draw.rect(screen, 'green', (x, y, SQUARE_SIZE, SQUARE_SIZE))

        if self.walls[0]:
            pg.draw.line(screen, 'black', [x, y], [x + SQUARE_SIZE, y], 3)
        if self.walls[1]:
            pg.draw.line(screen, 'black', [x + SQUARE_SIZE, y], [x + SQUARE_SIZE, y + SQUARE_SIZE], 3)
        if self.walls[2]:
            pg.draw.line(screen, 'black', [x + SQUARE_SIZE, y + SQUARE_SIZE], [x, y + SQUARE_SIZE], 3)
        if self.walls[3]:
            pg.draw.line(screen, 'black', [x, y + SQUARE_SIZE], [x, y], 3)


    def check(self, x, y):
        ind = lambda x, y: x + y * columns
        if x < 0 or x > columns - 1 or y < 0 or y > rows - 1:
            return False
        return grid[ind(x, y)]

    def go(self):
        nei = []
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

def passage(now, next):
    x1 = now.x - next.x
    if x1 == 1:
        now.walls[3] = False
        next.walls[1] = False
    elif x1 == -1:
        now.walls[1] = False
        next.walls[3] = False
    y1 = now.y - next.y
    if y1 == 1:
        now.walls[0] = False
        next.walls[2] = False
    elif y1 == -1:
        now.walls[2] = False
        next.walls[0] = False



#grid = [Cell(col, row) for row in range(rows) for col in range(columns)]
grid = []
for row in range(rows):
    for col in range(columns):
        grid.append(Cell(col, row))

cell_now = grid[0]

queue = deque()
running = True
while running:
    screen.fill(pg.Color('pink'))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    for c in grid:
        c.draw_lines_and_cell()
    cell_now.visited = 1
    cell_now.fill_current()
    next_c = cell_now.go()
    if next_c:
        next_c.visited = True
        passage(cell_now, next_c)
        cell_now = next_c
    pg.display.flip()
    time.tick(30)