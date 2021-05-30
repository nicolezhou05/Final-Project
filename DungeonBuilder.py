import pygame

#This initializes PyGame
pygame.init()

#Creates the display screen
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Infinite Tower")
icon = pygame.image.load('sword.png')
pygame.display.set_icon(icon)


#Game Loop
active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
            
    screen.fill((220, 220, 220))
    pygame.display.update()