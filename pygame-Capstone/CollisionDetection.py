import pygame
import random
pygame.init()

running = True
(width, height) = (600, 400)
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pygame Collision')

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                Ypos = Ypos + 10
                print('------------')
                print('Xpos ' + str(Xpos))
                print('Ypos ' + str(Ypos))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Ypos = Ypos - 10
                print('------------')
                print('Xpos ' + str(Xpos))
                print('Ypos ' + str(Ypos))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                Xpos = Xpos + 10
                print('------------')
                print('Xpos ' + str(Xpos))
                print('Ypos ' + str(Ypos))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                Xpos = Xpos - 10
                print('------------')
                print('Xpos ' + str(Xpos))
                print('Ypos ' + str(Ypos))
                
        
    if player.colliderect(Rectangle):
        colour1 = RED
    else:
        colour1 = GREEN

    surface.fill(AMARANTH)
    player = pygame.draw.rect(surface, colour, pygame.Rect(Xpos, Ypos, 30, 30))
    Rectangle = pygame.draw.rect(surface, colour1, pygame.Rect(Xpos1, Ypos1, Size, Size))

    pygame.display.flip()

pygame.quit()

