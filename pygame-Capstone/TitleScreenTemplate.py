import pygame
pygame.init()

running = True
(width, height) = (600, 400)
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Title Screen')

clock = pygame.time.Clock()
fps_limit = 60

    # Colours
BLACK = (0, 0, 0,)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
AMARANTH = (159, 43, 104)
AQUA = (0, 255, 255)

    #Object Creation
text_font = pygame.font.SysFont("Roboto", 50)
text_font2 = pygame.font.SysFont("Roboto", 75, bold = True)

def draw_text(Text, Font, Tcolour, xpos, ypos):
    img = Font.render(Text, True, Tcolour)
    surface.blit(img, (xpos, ypos))

    # Game Function
while running:
    clock.tick(fps_limit)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #BG colour
    surface.fill(AQUA)

    #Objects
    colour = GREEN
    (Xpos, Ypos) = pygame.mouse.get_pos()
    Cursor = pygame.draw.rect(surface, colour, pygame.Rect(Xpos, Ypos, 5, 5))

    #Text
    draw_text("Title", text_font2, BLACK, width/2.9, 75)
    StartGame = draw_text("Start Game", text_font, BLACK, width/2.9, 150)
    Settings = draw_text("Settings", text_font, BLACK, width/2.9, 200)
    Quit = draw_text("Quit", text_font, BLACK, width/2.9, 250)

    #Collisions

    pygame.display.flip()
pygame.quit()