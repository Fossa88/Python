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
import col
ColourST = col.AQUA
ColourSetT = col.AQUA
ColourQT = col.AQUA

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
    surface.fill(col.AQUA)

    #Objects
    (Xpos1, Ypos1) = pygame.mouse.get_pos()
    MoRect = pygame.draw.rect(surface, col.GREEN, (Xpos1, Ypos1, 2, 2))
    Cursor = pygame.draw.rect(surface, col.AQUA, (Xpos1, Ypos1, 5,5), 0)
    Dope = pygame.draw.rect(surface, col.AQUA, (206, 150, 188, 32))
    SettingsRectangle = pygame.draw.rect(surface, col.AQUA, (206, 200, 188, 32))
    QuitRectangle = pygame.draw.rect(surface, col.AQUA, (206, 250, 188, 32))

    #Text
    draw_text("CapStone", text_font2, col.BLACK, width/3.1, 75)
    StartGame = draw_text("Start Game", text_font, col.BLACK, width/2.9, 150)
    draw_text(">                       <", text_font, ColourST, width/3.4, 148)
    SettingsTemp = draw_text("Settings", text_font, col.BLACK, width/2.9, 200)
    draw_text(">                       <", text_font, ColourSetT, width/3.4, 198)
    Quit = draw_text("Quit", text_font, col.BLACK, width/2.9, 250)
    draw_text(">                       <", text_font, ColourQT, width/3.4, 248)

    #Press Events
    if event.type == pygame.MOUSEBUTTONDOWN:
            MoRect = pygame.draw.rect(surface, col.GREEN, (Xpos1, Ypos1, 2, 2))
            if MoRect.colliderect(Dope):
                import Chapter1
            if MoRect.colliderect(SettingsRectangle):
                print("hi")
            if MoRect.colliderect(QuitRectangle):
                pygame.quit()

    #Collisions
    if Cursor.colliderect(Dope):
        ColourST = col.BLACK
    else:
        ColourST = col.AQUA

    if Cursor.colliderect(SettingsRectangle):
        ColourSetT = col.BLACK
    else:
        ColourSetT = col.AQUA

    if Cursor.colliderect(QuitRectangle):
        ColourQT = col.BLACK
    else:
        ColourQT = col.AQUA

    pygame.display.flip()
pygame.quit()
