import pygame as pg
from collections import deque
from random import choice

WIDTH = 1200
HEIGHT = 750
SIZE = [WIDTH, HEIGHT]
square_size = 50
columns = WIDTH // square_size
rows = HEIGHT // square_size
sizes = [-1, 200, 100, 75, 50, 25]
back_image = pg.image.load('fon.jpg')
rect_im = back_image.get_rect(center=(600, 375))
GREEN = (68, 118, 40)

pg.init()

screen = pg.display.set_mode(SIZE)
time = pg.time.Clock()
x = 0
y = 0


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # top, right, bottom, left
        self.walls = [True, True, True, True]
        self.visited = False

    def fill_current(self):
        f1 = self.x * square_size
        f2 = self.y * square_size
        pg.draw.rect(screen, 'black', [f1 + 2, f2 + 2, square_size - 2, square_size - 2])

    def draw_lines_and_cell(self):
        x = self.x * square_size
        y = self.y * square_size

        if self.visited:
            pg.draw.rect(screen, GREEN, (x, y, square_size, square_size))

        if self.walls[0]:
            pg.draw.line(screen, 'black', [x, y], [x + square_size, y], 3)

        if self.walls[1]:
            pg.draw.line(screen, 'black', [x + square_size, y], [x + square_size, y + square_size], 3)

        if self.walls[2]:
            pg.draw.line(screen, 'black', [x + square_size, y + square_size], [x, y + square_size], 3)

        if self.walls[3]:
            pg.draw.line(screen, 'black', [x, y + square_size], [x, y], 3)

    def check(self, x, y):
        if x < 0 or x > columns - 1 or y < 0 or y > rows - 1:
            return False
        return grid[x + y * columns]

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
    xx = now.x // square_size
    yy = now.y // square_size

    if x1 == 1:
        now.walls[3] = False
        next.walls[1] = False

    if x1 == -1:
        now.walls[1] = False
        next.walls[3] = False

    y1 = now.y - next.y
    if y1 == 1:
        now.walls[0] = False
        next.walls[2] = False

    if y1 == -1:
        now.walls[2] = False
        next.walls[0] = False


grid = []

queue = deque()
running = True
usertext = ''
base_font = pg.font.Font(None, 300)
base_font2 = pg.font.Font(None, 80)
input_text = pg.Rect(550, 300, 0, 200)
game = False
right_input = False
final_input = 'NO'
typing = False
t1 = base_font2.render('', 1, (GREEN))
t2 = base_font2.render('', 1, (GREEN))
final_scene = False

while running:
    screen.blit(back_image, rect_im)

    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        if not final_scene:
            if i.type == pg.KEYDOWN:
                if not game:
                    if i.key == pg.K_BACKSPACE:
                        usertext = usertext[:-1]
                        t1 = base_font2.render('', 1, (GREEN))
                        typing = False

                    else:
                        if ((i.key == pg.K_1 or i.key == pg.K_2 or i.key == pg.K_3 or i.key == pg.K_4
                             or i.key == pg.K_5) and len(usertext) <= 0):
                            usertext += i.unicode
                            typing = True
                            t1 = base_font2.render('нажмите ENTER', 1, (GREEN))
                        if i.key == pg.K_RETURN and len(usertext) == 1:
                            final_input = int(usertext)
                            game = True
                            usertext = ''
                            t1 = base_font2.render('', 1, (GREEN))
                            t = base_font2.render('', 1, (GREEN))
                            square_size = sizes[final_input]
                            columns = WIDTH // square_size
                            rows = HEIGHT // square_size
                else:
                    q = grid[(x // square_size) + (y // square_size) * columns]
                    if i.key == pg.K_LEFT and x - square_size >= 0 and not q.walls[3]:
                        x -= square_size
                    elif i.key == pg.K_RIGHT and x + square_size * 2 <= WIDTH and not q.walls[1]:
                        x += square_size
                    elif i.key == pg.K_UP and y - square_size >= 0 and not q.walls[0]:
                        y -= square_size
                    elif i.key == pg.K_DOWN and y + square_size * 2 <= HEIGHT and not q.walls[2]:
                        y += square_size
                    if x == (columns - 1) * square_size and y == (rows - 1) * square_size:
                        final_scene = True
        else:  # для финальной сцены
            if i.type == pg.MOUSEBUTTONDOWN and 200 <= pg.mouse.get_pos()[0] <= 500 and 450 <= pg.mouse.get_pos()[1] <= 550:
                game = False
                final_scene = False
                typing = True
                square_size = 50
                columns = WIDTH // square_size
                rows = HEIGHT // square_size
                sizes = [-1, 200, 100, 75, 50, 25]
                x = 0
                y = 0
                grid = []
                queue = deque()
                running = True
                usertext = ''
                base_font = pg.font.Font(None, 300)
                base_font2 = pg.font.Font(None, 80)
                input_text = pg.Rect(550, 300, 0, 200)
                right_input = False
                final_input = 'NO'
                t1 = base_font2.render('', 1, (GREEN))
                t2 = base_font2.render('', 1, (GREEN))
            elif i.type == pg.MOUSEBUTTONDOWN and 700 <= pg.mouse.get_pos()[0] <= 1000 and 450 <= pg.mouse.get_pos()[1] <= 550:
                exit()

    if not final_scene:
        if not game:
            if typing and len(usertext) == 1:
                pg.draw.rect(screen, 'white', (370, 600, 450, 60), 0)
                pg.draw.rect(screen, 'white', (input_text), 0)
            txt = base_font.render(usertext, True, GREEN)
            screen.blit(txt, (input_text.x + 5, input_text.y + 5))
            input_text.w = 120

            pg.draw.rect(screen, 'white', (50, 200, 1100, 60))
            t = base_font2.render('введите уровень сложности от 1 до 5', 1, GREEN)
            screen.blit(t, (80, 200))
            screen.blit(t1, (370, 600))
            lab = pg.image.load('надпись.PNG')
            lab = pg.transform.scale(
                lab, (lab.get_width() // 4,
                      lab.get_height() // 4))
            dog_rect = lab.get_rect(center=(600, 100))
            screen.blit(lab, dog_rect)
        if game:
            if grid == []:
                for row in range(rows):
                    for col in range(columns):
                        grid.append(Cell(col, row))
                cell_now = grid[0]
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
            pg.draw.rect(screen, GREEN, (2, 2, square_size - 2, square_size - 2))
            pg.draw.rect(screen, (172, 22, 56), (
                (columns - 1) * square_size + 10, (rows - 1) * square_size + 10, square_size - 20, square_size - 20))
            pg.draw.rect(screen, 'black',
                         (x + square_size * 0.05, y + square_size * 0.05, square_size * 0.9, square_size * 0.9))
    else:
        pg.draw.rect(screen, 'white', (200, 450, 300, 100))
        pg.draw.rect(screen, 'white', (700, 450, 300, 100))
        f1 = base_font2.render('заново', 1, (GREEN))
        screen.blit(f1, (250, 475))
        f1 = base_font2.render('выйти', 1, (GREEN))
        screen.blit(f1, (765, 475))
        n1 = pg.image.load('надпись_финал.PNG')
        n1 = pg.transform.scale(
            n1, (n1.get_width() // 4.5,
                 n1.get_height() // 4.5))
        n1_rect = n1.get_rect(center=(600, 200))
        screen.blit(n1, n1_rect)

    pg.display.flip()
    time.tick(100)
