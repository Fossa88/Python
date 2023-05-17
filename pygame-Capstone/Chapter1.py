import pygame
import random
pygame.init()
import time

running = True
(width, height) = (600, 400)
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Chapter 1: The intro')  

# Variables
clock = pygame.time.Clock()
fps_limit = 60

# Image def's
BG = pygame.image.load('textures/Chap1Room1.png')
def Background(x,y):
    surface.blit(BG, (x,y))
    
# Classes
class GurtrudeClass(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('GurtrudeImgs/GurtrudeDown.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 150
        self.velocity = 2

    # Gurtrude Movement Code
    def update(self, rocks):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.velocity
            self.image = pygame.image.load('GurtrudeImgs/GurtrudeLeft.png')
        if keys[pygame.K_d]:
            self.rect.x += self.velocity
            self.image = pygame.image.load('GurtrudeImgs/GurtrudeRight.png')
        if keys[pygame.K_w]:
            self.rect.y -= self.velocity
            self.image = pygame.image.load('GurtrudeImgs/GurtrudeUp.png')
        if keys[pygame.K_s]:
            self.rect.y += self.velocity
            self.image = pygame.image.load('GurtrudeImgs/GurtrudeDown.png')

        # Collision detection with rocks
        for rock in rocks:
            if self.rect.colliderect(rock.rect):
                if keys[pygame.K_a]:
                    self.rect.x += self.velocity
                if keys[pygame.K_d]:
                    self.rect.x -= self.velocity
                if keys[pygame.K_w]:
                    self.rect.y += self.velocity
                if keys[pygame.K_s]:
                    self.rect.y -= self.velocity
    def x(self):
        return self.rect.x
    def y(self):
        return self.rect.y
    def velocity(self):
        return self.velocity

class RockClass(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('Textures/Rock1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def x(self):
        return self.rect.x
    def y(self):
        return self.rect.y

Gurtrude1 = GurtrudeClass()
Rock1 = RockClass(200, 200)
Rock2 = RockClass(500, 300)

Gurtrude_group = pygame.sprite.GroupSingle(Gurtrude1)
Rock1_group = pygame.sprite.GroupSingle(Rock1)
Rock2_group = pygame.sprite.GroupSingle(Rock2)

# Colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
AMARANTH = (159, 43, 104)

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

    # Movement Key Get
    keys = pygame.key.get_pressed()

    # Console log key
    if keys[pygame.K_k]:
        print('Rock1 XY Pos:', Rock1.rect.x, Rock1.rect.y)
        print('Rock2 XY Pos:', Rock2.rect.x, Rock2.rect.y)
        print('Gurtrude XY Pos:', Gurtrude1.rect.x, Gurtrude1.rect.y)

        # Normal key stuff lmao
    if keys[pygame.K_LSHIFT]:
        Gurtrude1.velocity = 3
    else:
        Gurtrude1.velocity = 2

        #Gurtrude world boundries
    if Gurtrude1.rect.x < 0:
        Gurtrude1.rect.x = 1 
    if Gurtrude1.rect.x > 570:
        Gurtrude1.rect.x = 569
    if Gurtrude1.rect.y < 0:
        Gurtrude1.rect.y = 1
    if Gurtrude1.rect.y > 370:
        Gurtrude1.rect.y = 369
                
    # Collision detection
    Gurtrude1.update([Rock1, Rock2])
    if pygame.sprite.spritecollide(Gurtrude1, Rock1_group, False):
        # Collision detected
        colour1 = RED
    elif pygame.sprite.spritecollide(Gurtrude1, Rock2_group, False):
        colour1 = AMARANTH
    else:
        colour1 = GREEN

    Rectangle = pygame.draw.rect(surface, colour1, pygame.Rect(Xpos1, Ypos1, Size, Size))

    # Image blits
    Background(0,0)
    surface.blit(Rock1.image, Rock1.rect)
    surface.blit(Rock2.image, Rock2.rect)
    surface.blit(Gurtrude1.image, Gurtrude1.rect)

    pygame.display.flip()

pygame.quit()
