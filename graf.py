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
            pg.draw.rect(screen, 'green', (x, y, square_size, square_size))

        if self.walls[0]:
            pg.draw.line(screen, 'black', [x, y], [x + square_size, y], 3)

        if self.walls[1]:
            pg.draw.line(screen, 'black', [x + square_size, y], [x + square_size, y + square_size], 3)

        if self.walls[2]:
            pg.draw.line(screen, 'black', [x + square_size, y + square_size], [x, y + square_size], 3)

        if self.walls[3]:
            pg.draw.line(screen, 'black', [x, y + square_size], [x, y], 3)

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
