import pygame
import random
pygame.init()

running = True
(width, height) = (600, 400)
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Chapter 1: The intro')  

clock = pygame.time.Clock()
fps_limit = 60
    #functions

    #Img stuff
GurtrudeImg = pygame.image.load('GurtrudeImgs/GurtrudeDown.png')
def Gurtrude(X,Y):
    surface.blit(GurtrudeImg, (X,Y))    
Xpos = 150
Ypos = 150
Vel = 5

    # Colours
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
AMARANTH = (159, 43, 104)
BaseCol = AMARANTH

    # Rectangle for collision detection
colour1 = GREEN
Xpos1 = random.randint(100,300)
Ypos1 = random.randint(100,500)
Size = random.randint(1,100)
Rectangle = pygame.draw.rect(surface, colour1, pygame.Rect(Xpos1, Ypos1, Size, Size))



    #Big Collision functions block
def CollisionCheck(Sprite1, Sprite2):
    Bool = pygame.sprite.collide_rect(Sprite1, Sprite2)
    if Bool == True:
        BaseCol = BLUE

def MoveLeft():
    Xpos == Xpos + 2

while running:
    clock.tick(fps_limit)
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        Xpos -= Vel
        GurtrudeImg = pygame.image.load('GurtrudeImgs/GurtrudeLeft.png')
    if keys[pygame.K_d]:
        Xpos += Vel
        GurtrudeImg = pygame.image.load('GurtrudeImgs/GurtrudeRight.png')
    if keys[pygame.K_w]:
        Ypos -= Vel
        GurtrudeImg = pygame.image.load('GurtrudeImgs/GurtrudeUp.png')
    if keys[pygame.K_s]:
        Ypos += Vel
        GurtrudeImg = pygame.image.load('GurtrudeImgs/GurtrudeDown.png')
    if Xpos < -0:
        Xpos = 1 
    if Xpos > 590:
        Xpos = 589

                
        #collisions

    surface.fill(BaseCol)
    Rectangle = pygame.draw.rect(surface, colour1, pygame.Rect(Xpos1, Ypos1, Size, Size))
        #Img blits
    Gurtrude(Xpos,Ypos) 

    pygame.display.flip()

pygame.quit()
