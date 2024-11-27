import pygame

from Character import Character

screen = pygame.display.set_mode((800,600))
running = True
char = Character()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    char.display(screen)
    char.move()
    pygame.display.flip()
