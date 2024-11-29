from turtledemo.paint import changecolor

import pygame.draw
import random

class Character:
    def __init__(self):
        self.x = 77
        self.direction_x = 1
        self.direction_y = 1
        self.y = 300
        self.width = 50
        self.height = 50
        self.color = (0, 255, 0)

    def display(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        if self.x == 0:
            self.color = + random radiant()
    def move(self):
        self.x += self.direction_x
        self.y += self.direction_y

        if self.x == 750:
            self.direction_x = -1
        if self.x == 0:
            self.direction_x = 1

        if self.y == 550:
            self.direction_y = -1
        if self.y == 0:
            self.direction_y = 1