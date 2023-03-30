import pygame
pygame.init()

running = True
background_colour = (255,200,100)
(width, height) = (600, 400)
surface = pygame.display.set_mode((width, height))
surface.fill(background_colour)
pygame.display.set_caption('Pygame Collision')

clock = pygame.time.Clock()
fps_limit = 60

    # Player Circle
colour = (50, 50 ,50)
Xpos = 300
Ypos = 200
player = pygame.draw.rect(surface, colour, pygame.Rect(30, 30, Xpos, Ypos))

    # Rectangle for collision detection
colour1 = (255, 0, 0)
Xpos1 = 500
Ypos1 = 200
circle = pygame.draw.rect(surface, colour1, pygame.Rect(60, 60, Xpos1, Ypos1))


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

        collide = pygame.Rect.colliderect(circle, player)

        if collide:
            print('hello')

    surface.fill(background_colour)
    pygame.draw.rect(surface, colour, pygame.Rect(30, 30, Xpos, Ypos))
    pygame.draw.rect(surface, colour1, pygame.Rect(60, 60, Xpos1, Ypos1))

    pygame.display.flip()

pygame.quit()

