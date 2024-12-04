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
        self.direction_red = 1
        self.direction_green = 1
        self.direction_blue = 1

        self.red = 80
        self.green = 160
        self.blue = 240

    def display(self, screen):
        pygame.draw.rect(screen, (self.red, self.green, self.blue), (self.x, self.y, self.width, self.height))

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

    def change_color(self):
        self.red += self.direction_red
        self.green += self.direction_green
        self.blue += self.direction_blue


        if self.red == 255:
            self.red = 0
        if self.green == 255:
            self.green = 0
        if self.blue == 255:
            self.blue = 0
