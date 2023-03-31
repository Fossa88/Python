import pygame
pygame.init()

running = True
(width, height) = (600, 400)
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Title Screen')

clock = pygame.time.Clock()
fps_limit = 120

    # Colours
WHITE = (255, 255, 255)
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

def Rectangle(surface, Colour, Xpos2, Ypos2, Length, Height1):
    pygame.draw.rect(surface, Colour, pygame.Rect(Xpos2, Ypos2, Length, Height1))

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
    (Xpos1, Ypos1) = pygame.mouse.get_pos()
    Cursor = pygame.draw.rect(surface, colour, pygame.Rect(Xpos1, Ypos1, 5, 5))
    StartRectangle = Rectangle(surface, AQUA, width/2.9, 150, 188, 32)
    SettingsRectangle = Rectangle(surface, WHITE, width/2.9, 200, 188, 32)
    QuitRectangle = Rectangle(surface, WHITE, width/2.9, 250, 188, 32)

    #Text
    draw_text("Title", text_font2, BLACK, width/2.9, 75)
    StartGame = draw_text("Start Game", text_font, BLACK, width/2.9, 150)
    Settings = draw_text("Settings", text_font, BLACK, width/2.9, 200)
    Quit = draw_text("Quit", text_font, BLACK, width/2.9, 250)

    #Collisions

    pygame.display.flip()
pygame.quit()
