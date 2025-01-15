# import pygame
#
#
# class Pipe:
#     def __init__(self):
#         self.x = 500
#         self.speed_x = -10
#         self.y = 300
#         self.y2 = 0
#         self.height2 = 100
#         self.width = 50
#         self.height =300
#
#     def display(self, screen):
#         pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.width, self.height))
#         pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y2, self.width, self.height2))
#
#     def move(self):
#         self.x -= 2
#         # self.x += self.speed_x
#         #
#         # if self.x >= 800 + self.width:
#         #     self.x = -2
#         if self.x <= -50:
#                 self.x += 800