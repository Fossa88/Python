import pygame

running = True
background_colour = (255,200,100)
(width, height) = (600, 400)
surface = pygame.display.set_mode((width, height))
surface.fill(background_colour)
pygame.display.set_caption('Pygame Collision')

clock = pygame.time.Clock()
fps_limit = 60

colour = (50, 50 ,50)
Xpos = 300
Ypos = 200
circle = pygame.draw.circle(surface, colour, (Xpos,Ypos), 20)

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

    surface.fill(background_colour)
    pygame.draw.circle(surface, colour, (Xpos,Ypos), 20, 0,)

    pygame.display.flip()

pygame.quit()

