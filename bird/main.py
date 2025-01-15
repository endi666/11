# import pygame
#
# from Bird import Bird
# from Pipe import Pipe
# screen = pygame.display.set_mode((800, 600))
# running = True
# clock = pygame.time.Clock()
# char = Bird()
# char1 = Pipe()
# char2 = Pipe()
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                 char.jump()
#     screen.fill((0, 0, 0))
#     char.display(screen)
#     char.move()
#
#     char1.display(screen)
#     char1.move()
#
#     pygame.display.flip()
#     clock.tick(30)