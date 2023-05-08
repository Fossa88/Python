import pygame
import random
pygame.init()

running = True
(width, height) = (600, 400)
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Chapter 1: The intro')

clock = pygame.time.Clock()
fps_limit = 60

    # Colours
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
AMARANTH = (159, 43, 104)

    # Player Rectangle
colour = BLUE
Xpos = 300
Ypos = 200
Vel = 2
player = pygame.draw.rect(surface, colour, pygame.Rect(Xpos, Ypos, 30, 30))

    # Rectangle for collision detection
colour1 = GREEN
Xpos1 = random.randint(100,300)
Ypos1 = random.randint(100,500)
Size = random.randint(1,100)
Rectangle = pygame.draw.rect(surface, colour1, pygame.Rect(Xpos1, Ypos1, Size, Size))


while running:
    clock.tick(fps_limit)
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        Xpos -= Vel

    if keys[pygame.K_d]:
        Xpos += Vel

    if keys[pygame.K_w]:
        Ypos -= Vel

    if keys[pygame.K_s]:
        Ypos += Vel
                
        
    if player.colliderect(Rectangle):
        colour1 = RED
    else:
        colour1 = GREEN

    surface.fill(AMARANTH)
    player = pygame.draw.rect(surface, colour, pygame.Rect(Xpos, Ypos, 30, 30))
    Rectangle = pygame.draw.rect(surface, colour1, pygame.Rect(Xpos1, Ypos1, Size, Size))

    pygame.display.flip()

pygame.quit()
