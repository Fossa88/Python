import pygame
pygame.init()
import time

# Boundary's
running = True
(width, height) = (600, 400)
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Music Cube (Hi Jaimie)')

# Variables
clock = pygame.time.Clock()
fps_limit = 60

# Colours
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
AMARANTH = (159, 43, 104)

# BG
IceHockey = pygame.image.load('Background505.png')
def BG():
    surface.blit(IceHockey, (0, 0))

# Classes
class cube(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('Heart.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = pygame.Vector2(2, 2)
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)

    # I fucking hated writing this shit (I pray I never have to touch it again)
    # And there is probably a 200% easier way to write this XD
    def update(self, rectangleV, rectangleH):
        collided = False

        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        self.hitbox.x = self.rect.x
        self.hitbox.y = self.rect.y

        for rectangle1 in rectangleV:
            if self.hitbox.colliderect(rectangle1.rect):
                if self.velocity.x > 0: 
                    self.rect.right = rectangle1.rect.left
                else:
                    self.rect.left = rectangle1.rect.right
                self.velocity.x *= -1 
                collided = True

        for rectangle2 in rectangleH:
            if self.hitbox.colliderect(rectangle2.rect):
                if self.velocity.y > 0:
                    self.rect.bottom = rectangle2.rect.top
                else:
                    self.rect.top = rectangle2.rect.bottom
                self.velocity.y *= -1
                collided = True

        if not collided:
            self.velocity.normalize_ip()
            self.velocity *= 2  # Speed Changer

class rectangleV(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('RectangleVertical.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def x(self):
        return self.rect.x

    def y(self):
        return self.rect.y

class rectangleH(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('RectangleHorizontal.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def x(self):
        return self.rect.x

    def y(self):
        return self.rect.y

# Initialization P1
    # Cube
cube1 = cube(330, 230)  # Update initial position

    # Vertical Rectangles
rectangleV1 = rectangleV(500, 175)

    # Horizontal Rectangles
rectangleH1 = rectangleH(330, 300)

# Initialization P2
    # Cube
cube_group = pygame.sprite.GroupSingle(cube1)

    # Vertical Rectangles
rectangleV1_group = pygame.sprite.GroupSingle(rectangleV1)

    # Horizontal Rectangles
rectangleH1_group = pygame.sprite.GroupSingle(rectangleH1)

# Game Function
while running:
    clock.tick(fps_limit)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    print('cube1 XY Pos:', cube1.rect.x, cube1.rect.y)
            
    # Cube movement
    cube1.update([rectangleV1], [rectangleH1])
    
    # Blits
    BG()
    surface.blit(cube1.image, cube1.rect)
    surface.blit(rectangleV1.image, rectangleV1.rect)
    surface.blit(rectangleH1.image, rectangleH1.rect)
    
    pygame.display.flip()
pygame.quit()