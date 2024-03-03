import pygame

WIDTH = 1300
HEIGHT = 700
SIZE = [WIDTH, HEIGHT]

screen = pygame.display.set_mode(SIZE)
time = pygame.time.Clock()

while True:
    screen.fill(pygame.Color('pink'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.flip()
    time.tick(30)