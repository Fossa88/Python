import pygame
pygame.init()

running = True
(width, height) = (800, 600)
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('SquareSync')

clock = pygame.time.Clock()
fps_limit = 60

    # Colours
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0,)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
AMARANTH = (159, 43, 104)
AQUA = (0, 255, 255)

    # Rectangle for collision detection
Xpos = 300
Ypos = 400
Size = 25
pygame.draw.rect(surface, RED, pygame.Rect(Ypos, Xpos, Size, Size))

while running:
    clock.tick(fps_limit)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    surface.fill(GRAY)
    # Rectangles
    Sync = pygame.draw.rect(surface, RED, pygame.Rect(Ypos, Xpos, Size, Size))


    pygame.display.flip()
pygame.quit()
