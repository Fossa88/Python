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
Constant = 1

# Image def's
    #Room Image Def's
BG1 = pygame.image.load('textures/Room1.png')
def Room1BG(x, y):
    surface.blit(BG1, (x, y))

BG2 = pygame.image.load('textures/Room2.png')
def Room2BG():
    surface.blit(BG2, (0, 0))
    
BG3 = pygame.image.load('textures/Room3.png')
def Room3BG():
    surface.blit(BG3, (0, 0))
    
BG4 = pygame.image.load('textures/Room4.png')
def Room4BG():
    surface.blit(BG4, (0, 0))
    
BG5 = pygame.image.load('textures/Room5.png')
def Room5BG():
    surface.blit(BG5, (0, 0))
    
BG6 = pygame.image.load('textures/Room6.png')
def Room6BG():
    surface.blit(BG6, (0, 0))

TreeTrollFace = pygame.image.load('textures/TreeTop.png')
def TreeTop(x, y):
    surface.blit(TreeTrollFace, (x, y))

Inventory_Sprite = pygame.image.load('textures/Inventory_sprite.png')
def InventorySprite(x, y):
    surface.blit(Inventory_Sprite, (x, y))
    
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

    def update1(self, bushes, trees):
        
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

        # Collision detection with bushes
        for bush in bushes:
            if self.hitbox.colliderect(bush.rect):
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

class BushClass(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('Textures/Bush.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def x(self):
        return self.rect.x

    def y(self):
        return self.rect.y

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

# inventory sprite visibility
inventory_visible = False

# Colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
AMARANTH = (159, 43, 104)
WHITE = (255,255,255)

#Room1
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

#Room2
Gurtrude2 = GurtrudeClass(2, 200)
Bush1 = BushClass(140, 365)
Bush2 = BushClass(363, 365)
Bush3 = BushClass(222, 160)
TreeBottom5 = TreeClass(44, 305)
TreeBottom6 = TreeClass(503, 305)

Gurtrude2_group = pygame.sprite.GroupSingle(Gurtrude2)
Bush1_group = pygame.sprite.GroupSingle(Bush1)
Bush2_group = pygame.sprite.GroupSingle(Bush2)
Bush3_group = pygame.sprite.GroupSingle(Bush3)
TreeBottom5_group = pygame.sprite.GroupSingle(TreeBottom5)
TreeBottom6_group = pygame.sprite.GroupSingle(TreeBottom6)

#Room3
Bush4 = BushClass(350, 325)
Bush5 = BushClass(545, 262)
Bush6 = BushClass(545, 90)
Bush7 = BushClass(160, -45)
Bush8 = BushClass(357, -45)
Bush9 = BushClass(170, 325)
TreeBottom7 = TreeClass(30, 300)

Bush4_group = pygame.sprite.GroupSingle(Bush4)
Bush5_group = pygame.sprite.GroupSingle(Bush5)
Bush6_group = pygame.sprite.GroupSingle(Bush6)
Bush7_group = pygame.sprite.GroupSingle(Bush7)
Bush8_group = pygame.sprite.GroupSingle(Bush8)
Bush9_group = pygame.sprite.GroupSingle(Bush9)
TreeBottom7_group = pygame.sprite.GroupSingle(TreeBottom7)
#Room4

#Room5

#Room6

#Room7?

# Room Def's (aka big mother fucker of code bruhge).
    # Room1
def Room1():
    Gurtrude1.update([Rock1, Rock2], [TreeBottom1, TreeBottom2, TreeBottom3, TreeBottom4])
    Room1BG(0, 0)
    surface.blit(Rock1.image, Rock1.rect)
    surface.blit(Rock2.image, Rock2.rect)
    surface.blit(TreeBottom1.image, TreeBottom1.rect)
    surface.blit(TreeBottom2.image, TreeBottom2.rect)
    surface.blit(TreeBottom3.image, TreeBottom3.rect)
    surface.blit(TreeBottom4.image, TreeBottom4.rect)
    surface.blit(Gurtrude1.image, Gurtrude1.rect)
    TreeTop(500, 0)
    TreeTop(300, -250)
    TreeTop(120, 0) 
    TreeTop(50, -270)

    #Room2
def Room2():
    Gurtrude1.update1([Bush1, Bush2, Bush3], [TreeBottom5, TreeBottom6])
    Room2BG()
    surface.blit(Gurtrude1.image, Gurtrude1.rect)
    surface.blit(Bush1.image, Bush1.rect)
    surface.blit(Bush2.image, Bush2.rect)
    surface.blit(Bush3.image, Bush3.rect)
    surface.blit(TreeBottom5.image, TreeBottom5.rect)
    surface.blit(TreeBottom6.image, TreeBottom6.rect)
    TreeTop(44, 0)
    TreeTop(503, 0)

def Room3():
    Gurtrude1.update1([Bush7, Bush8, Bush9, Bush4, Bush5, Bush6], [TreeBottom7])
    Room3BG()
    surface.blit(Gurtrude1.image, Gurtrude1.rect)
    surface.blit(Bush7.image, Bush7.rect)
    surface.blit(Bush8.image, Bush8.rect)
    surface.blit(Bush9.image, Bush9.rect)
    surface.blit(Bush4.image, Bush4.rect)
    surface.blit(Bush5.image, Bush5.rect)
    surface.blit(Bush6.image, Bush6.rect)
    surface.blit(TreeBottom7.image, TreeBottom7.rect)
    TreeTop(30, 0)
    
def Room4():
    Gurtrude1.update1([Bush1, Bush2, Bush3], [TreeBottom5, TreeBottom6])
    Room4BG()
    
def Room5():
    Gurtrude1.update1([Bush1, Bush2, Bush3], [TreeBottom5, TreeBottom6])
    Room5BG()
    
def Room6():
    Gurtrude1.update1([Bush1, Bush2, Bush3], [TreeBottom5, TreeBottom6])
    Room6BG()
    
while running:
    clock.tick(fps_limit)
    surface.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement Key Get
    keys = pygame.key.get_pressed()

    # Game Keys
    if keys[pygame.K_k]:
        print('Gurtrude XY Pos:', Gurtrude1.rect.x, Gurtrude1.rect.y)

    if keys[pygame.K_i]:
        Constant += 1
        time.sleep(1)
        print(Constant)
    if keys[pygame.K_u]:
        Constant -= 1
        time.sleep(1)
        print(Constant)

    # Inventory visibility
    if keys[pygame.K_e]:
        time.sleep(0.15)
        inventory_visible = not inventory_visible

    # Normal key stuff
    if keys[pygame.K_LSHIFT]:
        Gurtrude1.velocity = 3
    else:
        Gurtrude1.velocity = 2

    # Gurtrude world boundaries
    if Gurtrude1.rect.x < 0:
        Gurtrude1.rect.x = 1
    if Gurtrude1.rect.x > 570:
        Gurtrude1.rect.x = 569
    if Gurtrude1.rect.y < 0:
        Gurtrude1.rect.y = 1
    if Gurtrude1.rect.y > 370:
        Gurtrude1.rect.y = 369

    # Image blits
    if Constant == 1:
        Room1()
    elif Constant == 2:
        Room2()
    elif Constant == 3:
        Room3()
    elif Constant == 4:
        Room4()
    elif Constant == 5:
        Room5()
    elif Constant == 6:
        Room6()
    
    # Draw inventory sprite if visible
    if inventory_visible:
        InventorySprite(296, 300)
    
    pygame.display.flip()

pygame.quit()
