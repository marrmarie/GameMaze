import pygame as pg

class Ball(pg.sprite.Sprite):
    def __init__(self, x, filename):
        pg.sprite.Sprite.__init__(self)
        # self.image = surf

        self.image = pg.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, 0))

        # self.speed = speed
        # self.add(group)

    # def update(self, *args):
    #     if self.rect.y < args[0] - 20:
    #         self.rect.y += self.speed
    #     else:
    #         self.kill()
