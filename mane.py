# import pygame
#
# from Character import Character
#
# screen = pygame.display.set_mode((800, 600))
# running = True
# char = []
#
# for i in range(150):
#     char.append(Character())
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     # screen.fill((0, 0, 0))
#
#     for g in range(len(char)):
#         char[g].display(screen)
#         char[g].move()
#         char[g].change_color()
#     pygame.display.flip()
#
