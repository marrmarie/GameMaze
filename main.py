import pygame as pg
from collections import deque
from random import choice

WIDTH = 1202
HEIGHT = 802
SIZE = [WIDTH, HEIGHT]
SQUARE_SIZE = 300
columns = WIDTH // SQUARE_SIZE
rows = HEIGHT // SQUARE_SIZE


pg.init()


screen = pg.display.set_mode(SIZE)
time = pg.time.Clock()
x = 0
y = 0

lab = [[[] for i in range(columns)] for j in range(rows)]

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # top, right, bottom, left
        self.walls = [True, True, True, True]
        self.visited = False

    def fill_current(self):
        f1 = self.x * SQUARE_SIZE
        f2 = self.y * SQUARE_SIZE
        pg.draw.rect(screen, 'black', [f1 + 2, f2 + 2, SQUARE_SIZE - 2, SQUARE_SIZE - 2])

    def draw_lines_and_cell(self):
        x = self.x * SQUARE_SIZE
        y = self.y * SQUARE_SIZE

        if self.visited:
            pg.draw.rect(screen, 'green', (x, y, SQUARE_SIZE, SQUARE_SIZE))

        x1 = self.x // SQUARE_SIZE
        y1 = self.y // SQUARE_SIZE
        if self.walls[0]:
            pg.draw.line(screen, 'black', [x, y], [x + SQUARE_SIZE, y], 3)
        # else:
        #     if 0 not in lab[x1][y1]:
        #         lab[x1][y1].append(0)
        #     if 2 not in lab[x1][y1 - 1]:
        #         lab[x1][y1 - 1].append(2)

        if self.walls[1]:
            pg.draw.line(screen, 'black', [x + SQUARE_SIZE, y], [x + SQUARE_SIZE, y + SQUARE_SIZE], 3)
        # else:
        #     if 1 not in lab[x1][y1]:
        #         lab[x1][y1].append(1)
        #     if 3 not in lab[x1 + 1][y1]:
        #         lab[x1 + 1][y1].append(3)

        if self.walls[2]:
            pg.draw.line(screen, 'black', [x + SQUARE_SIZE, y + SQUARE_SIZE], [x, y + SQUARE_SIZE], 3)
        # else:
        #     if 2 not in lab[x1][y1]:
        #         lab[x1][y1].append(2)
        #     if 0 not in lab[x1][y1 + 1]:
        #         lab[x1][y1 + 1].append(0)

        if self.walls[3]:
            pg.draw.line(screen, 'black', [x, y + SQUARE_SIZE], [x, y], 3)
        # else:
        #     if 3 not in lab[x1][y1]:
        #         lab[x1][y1].append(3)
        #     if 1 not in lab[x1 - 1][y1]:
        #         lab[x1 - 1][y1].append(1)

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
    global lab
    x1 = now.x - next.x
    xx = now.x // SQUARE_SIZE
    yy = now.y // SQUARE_SIZE

    if x1 == 1:
        now.walls[3] = False
        next.walls[1] = False
    # else:
    #     if 3 not in lab[xx][yy]:
    #         lab[xx][yy].append(3)
    #     if 1 not in lab[xx - 1][yy]:
    #         lab[xx - 1][yy].append(1)

    if x1 == -1:
        now.walls[1] = False
        next.walls[3] = False
    # else:
    #     if 1 not in lab[xx][yy]:
    #         lab[xx][yy].append(1)
    #     if 3 not in lab[xx + 1][yy]:
    #         lab[xx + 1][yy].append(3)

    y1 = now.y - next.y
    if y1 == 1:
        now.walls[0] = False
        next.walls[2] = False
    # else:
    #     if 0 not in lab[xx][yy]:
    #         lab[xx][yy].append(0)
    #     if 2 not in lab[xx][yy - 1]:
    #         lab[xx][yy - 1].append(2)
    if y1 == -1:
        now.walls[2] = False
        next.walls[0] = False
    # else:
    #     if 2 not in lab[xx][yy]:
    #         lab[xx][yy].append(2)
    #     if 0 not in lab[xx][yy + 1]:
    #         lab[xx][yy + 1].append(0)



grid = []
for row in range(rows):
    for col in range(columns):
        grid.append(Cell(col, row))

cell_now = grid[0]

queue = deque()
running = True

while running:
    screen.fill(pg.Color('pink'))

    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        elif i.type == pg.KEYDOWN:
            for j in range(len(lab)):
                print(*lab[j])
            q = grid[(x // SQUARE_SIZE) + (y // SQUARE_SIZE) * columns]
            if i.key == pg.K_LEFT and x - SQUARE_SIZE >= 0 and not q.walls[3]:
                x -= SQUARE_SIZE
            elif i.key == pg.K_RIGHT and x + SQUARE_SIZE * 2 <= WIDTH and not q.walls[1]:
                x += SQUARE_SIZE
            elif i.key == pg.K_UP and y - SQUARE_SIZE >= 0 and not q.walls[0]:
                y -= SQUARE_SIZE
            elif i.key == pg.K_DOWN and y + SQUARE_SIZE * 2 <= HEIGHT and not q.walls[2]:
                y += SQUARE_SIZE



    for c in grid:
        c.draw_lines_and_cell()

    cell_now.visited = True
    cell_now.fill_current()

    next_c = cell_now.go()
    if next_c:
        next_c.visited = True
        queue.append(cell_now)
        passage(cell_now, next_c)
        cell_now = next_c
    elif queue:
        cell_now = queue.pop()
    pg.draw.rect(screen, 'black', (x + SQUARE_SIZE * 0.05, y + SQUARE_SIZE * 0.05, SQUARE_SIZE * 0.9, SQUARE_SIZE * 0.9))
    pg.display.flip()
    time.tick(10)