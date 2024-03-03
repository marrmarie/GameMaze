import pygame as pg

WIDTH = 1300
HEIGHT = 700
SIZE = [WIDTH, HEIGHT]
screen = pg.display.set_mode(SIZE)
screen.fill(pg.Color('pink'))
rect_big = pg.Rect(500, 250, 300, 200)
pg.draw.rect(screen, ('white'), rect_big)

# surf = pg.Surface((150, 150))
# surf.set_colorkey((0, 0, 0))
# screen.blit(surf, pg.Rect(150, 150, 150, 150))
active=False
user_text= ' '
running = True
while running:

    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            print(pg.mouse.get_pos())
            if rect_big.collidepoint(event.pos):
                pg.draw.rect(screen, ('red'), rect_big)
                #screen.blit(screen, pg.Rect())

    pg.display.update()
    pg.time.delay(100)

pg.quit()