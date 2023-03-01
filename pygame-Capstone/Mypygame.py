import pygame

background_colour = (100,245,25)
(width, height) = (600, 400)
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)

pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

colour = (0, 0, 50)
surface = pygame.display.set_mode((100,200))
pygame.draw.rect(surface, colour, pygame.Rect(30, 30, 30, 30))
pygame.display.flip()