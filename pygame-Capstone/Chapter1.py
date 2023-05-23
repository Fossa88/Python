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
def Background(x, y):
    surface.blit(BG, (x, y))

TreeTrollFace = pygame.image.load('textures/TreeTop.png')
def TreeTop(x,y):
    surface.blit(TreeTrollFace, (x,y))

Inventory_Sprite = pygame.image.load('textures/Inventory_sprite.png')
def InventorySprite(x,y):
    surface.blit(Inventory_Sprite, (x,y))

# Classes
class GurtrudeClass(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('GurtrudeImgs/GurtrudeDown.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = 2
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)

    # Gurtrude Movement Code
    def update(self, rocks, trees):
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

        self.hitbox.x = self.rect.x
        self.hitbox.y = self.rect.y

        # Collision detection with rocks
        for rock in rocks:
            if self.hitbox.colliderect(rock.rect):
                if keys[pygame.K_a]:
                    self.rect.x += self.velocity
                if keys[pygame.K_d]:
                    self.rect.x -= self.velocity
                if keys[pygame.K_w]:
                    self.rect.y += self.velocity
                if keys[pygame.K_s]:
                    self.rect.y -= self.velocity

        # Collision detection with trees
        for tree in trees:
            if self.hitbox.colliderect(tree.rect):
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


class TreeClass(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('textures/TreeBottom.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def x(self):
        return self.rect.x

    def y(self):
        return self.rect.y

    # Placing teh obkecys
Gurtrude1 = GurtrudeClass(2, 200)
Rock1 = RockClass(200, 50)
Rock2 = RockClass(300, 300)
TreeBottom1 = TreeClass(500, 330)
TreeBottom2 = TreeClass(300, 50)
TreeBottom3 = TreeClass(120, 310)
TreeBottom4 = TreeClass(50, 30)

Gurtrude_group = pygame.sprite.GroupSingle(Gurtrude1)
Rock1_group = pygame.sprite.GroupSingle(Rock1)
Rock2_group = pygame.sprite.GroupSingle(Rock2)
TreeBottom1_group = pygame.sprite.GroupSingle(TreeBottom1)
TreeBottom2_group = pygame.sprite.GroupSingle(TreeBottom2)
TreeBottom3_group = pygame.sprite.GroupSingle(TreeBottom3)
TreeBottom4_group = pygame.sprite.GroupSingle(TreeBottom4)

# Colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
AMARANTH = (159, 43, 104)

while running:
    clock.tick(fps_limit)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement Key Get
    keys = pygame.key.get_pressed()

    # Game Keys
    if keys[pygame.K_k]:
        print('Rock1 XY Pos:', Rock1.rect.x, Rock1.rect.y)
        print('Rock2 XY Pos:', Rock2.rect.x, Rock2.rect.y)
        print('TreeBottom1 XY Pos:', TreeBottom1.rect.x, TreeBottom1.rect.y)
        print('Gurtrude XY Pos:', Gurtrude1.rect.x, Gurtrude1.rect.y)

    # Normal key stuff lmao
    if keys[pygame.K_LSHIFT]:
        Gurtrude1.velocity = 3
    else:
        Gurtrude1.velocity = 2

    if keys[pygame.K_e]:
        InventorySprite(300,500)
    else:
        InventorySprite(-1000, -10000)

    # Gurtrude world boundaries
    if Gurtrude1.rect.x < 0:
        Gurtrude1.rect.x = 1
    if Gurtrude1.rect.x > 570:
        Gurtrude1.rect.x = 569
    if Gurtrude1.rect.y < 0:
        Gurtrude1.rect.y = 1
    if Gurtrude1.rect.y > 370:
        Gurtrude1.rect.y = 369

    # Collision detection
    Gurtrude1.update([Rock1, Rock2], [TreeBottom1, TreeBottom2, TreeBottom3, TreeBottom4])

    # Image blits
    Background(0, 0)
    surface.blit(Rock1.image, Rock1.rect)
    surface.blit(Rock2.image, Rock2.rect)
    surface.blit(TreeBottom1.image, TreeBottom1.rect)
    surface.blit(TreeBottom2.image, TreeBottom2.rect)
    surface.blit(TreeBottom3.image, TreeBottom3.rect)
    surface.blit(TreeBottom4.image, TreeBottom4.rect)
    surface.blit(Gurtrude1.image, Gurtrude1.rect)
    TreeTop(500,0)
    TreeTop(300,-250)
    TreeTop(120, 0)
    TreeTop(50,-270)
    InventorySprite(302, 300)

    pygame.display.flip()

pygame.quit()
