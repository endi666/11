import pygame.draw


class Character:
    def __init__(self):
        self.x = 77
        self.direction = 1
        self.y = 300
        self.width = 50
        self.height = 50

    def display(self, screen):
        pygame.draw.rect(screen, (70,0, 160), (self.x, self.y, self.width, self.height))

    def move(self):
        self.x += self.direction
        if self.x == 800:
            self.direction = -1
        if self.x == 0:
            self.direction = 1
