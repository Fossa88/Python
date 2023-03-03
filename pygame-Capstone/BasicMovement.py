import pygame

background_colour = (255,200,100)
(width, height) = (600, 400)
surface = pygame.display.set_mode((width, height))
surface.fill(background_colour)
pygame.display.set_caption('Pygame Collision')

  #Functions
def Refresh():
  pygame.display.flip()


# key = pygame.key.get_pressed()
# if key[pygame.t]:
#  Refresh()

colour = (5, 50, 50)

pygame.draw.circle(surface, colour, (300,200), 20, 0,)

pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
