import pygame
import math
pygame.init()

running = True
(width, height) = (600, 400)
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Title Screen')

clock = pygame.time.Clock()
fps_limit = 60

    # Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0,)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
AMARANTH = (159, 43, 104)
AQUA = (0, 255, 255)
ColourRe = AQUA

    #Object
text_font = pygame.font.SysFont("Roboto", 50)
text_font2 = pygame.font.SysFont("Roboto", 75, bold = True)

def draw_text(Text, Font, Tcolour, xpos, ypos):
    img = Font.render(Text, True, Tcolour)
    surface.blit(img, (xpos, ypos))

def Rectangle(surface, Colour, Xpos2, Ypos2, Length, Height1):
    pygame.draw.rect(surface, Colour, (Xpos2, Ypos2, Length, Height1))

    # Game Function
while running:
    clock.tick(fps_limit)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #BG colour
    surface.fill(AQUA)

    #Objects
    (Xpos1, Ypos1) = pygame.mouse.get_pos()
    MoRect = pygame.draw.rect(surface, GREEN, (Xpos1, Ypos1, 2, 2))
    Cursor = pygame.draw.rect(surface, AQUA, (Xpos1, Ypos1, 5, 5), 0)
    ReturnBox = pygame.draw.rect(surface, AQUA, (120, 200, 400, 32))

    #Text
    draw_text("Settings", text_font2, BLACK, width/2.9, 75)
    StartGame = draw_text("Setting stuff to be dealt with later", text_font, BLACK, 2.9, 150)
    ReturnGame = draw_text("Return to Main Menu", text_font, BLACK, width/4.2, 200)
    draw_text(">                                       <", text_font, ColourRe, width/5, 198)

    if event.type == pygame.MOUSEBUTTONDOWN:
            MoRect = pygame.draw.rect(surface, GREEN, (Xpos1, Ypos1, 2, 2))
    if MoRect.colliderect(ReturnBox):
        import TitleScreenTemplate
        
    
    if Cursor.colliderect(ReturnBox):
        ColourRe = BLACK
    else:
        ColourRE = AQUA

    pygame.display.flip()
pygame.quit()