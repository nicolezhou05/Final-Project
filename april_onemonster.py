import pygame
import turtle
import random

#This initializes PyGame
pygame.init()

#Display
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Infinite Dungeon")
icon = pygame.image.load('sword.png')
pygame.display.set_icon(icon)

#Player
playeravatar = pygame.image.load('knight.png')
playeravatar = pygame.transform.scale(playeravatar, (60,55))

plyrxcord = 75
plyrycord = 300
plyrhealth = 100
plyrattack = 20
plyrdefend = 10

def player(x,y):
    screen.blit(playeravatar, (x,y))

#determine if collided
def collided (monsterxcord, monsterycord, playerxcord, playerycord):
    distance = ((monsterxcord - plyrxcord)**2 + (monsterycord - plyrycord)**2)**0.5
    if distance < 54:
        return True
    else:
        return False

#Monster
def randomlist(minimum, maximum):
    answer = []
    order = minimum
    while order < maximum:
        answer.append(order)
        order += 1
    return answer

monsteravatar = pygame.image.load('ogre.png')
monsteravatar = pygame.transform.scale(monsteravatar, (60,55))
xcord = random.choice(randomlist(150, 720))
ycord = random.choice(randomlist(50, 550))
#make sure monsters don't spawn in same area 
#    collide = True
#    while collide == True:
#        for x in monsterxcord:
#            if xcord = monsterxcord[x] 
#        xcord = random.choice(randomlist(150, 720))
#        ycord = random.choice(randomlist(50, 550))
monsterxcord = xcord
monsterycord = xcord
monsterxcordchange = 0
monsterycordchange = 0
monsterhealth = 10

def monster(x, y):
    screen.blit(monsteravatar, (x,y))
    
#Door 
dooravatar = pygame.image.load('door.png')
dooravatar = pygame.transform.scale(dooravatar, (60,55))
doorxcord = 730
doorycord = 545

def door(x, y):
    screen.blit(dooravatar, (x,y))
    
def attack(attackedhealth, attacker_attackstat):
    if monstercollision == True and defend != True:
        attackedhealth -= attacker_attackstat
        print("attack")

def defend():
    if monstercollision == True:
        defend = True 
        print("defend")
    
#Info
font = pygame.font.Font.render

def health():
    health = font.render("Player Health: " + plyrhealth )


#Game Loop
active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            active = False
            quit()
        
        #Player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                plyrxcord -= 50
            if event.key == pygame.K_RIGHT:
                plyrxcord += 50
            if event.key == pygame.K_UP:
                plyrycord -= 50
            if event.key == pygame.K_DOWN:
                plyrycord += 50
        #Player attack
            if event.key == pygame.K_a:
                attack(monsterhealth, plyrattack)
            if event.key == pygame.K_d:
                defend()

    screen.fill((220, 220, 220))

    #Player boundaries
    if plyrxcord <= 0:
        plyrxcord = 1
    if plyrxcord >= 740:
        plyrxcord = 739
    if plyrycord <= 0:
        plyrycord = 1
    if plyrycord >= 546:
        plyrycord = 544
    
    monsterxcord += monsterxcordchange
    
    #Monster boundaries
    if monsterxcord <= 0:
        monsterxcord = 1
    if monsterxcord >= 740:
        monsterxcord = 739
    if monsterycord <= 0:
        monsterycord = 1
    if monsterycord >= 546:
        monsterycord = 544
    
        #Collision
    monstercollision = collided(monsterxcord, monsterycord, plyrxcord, plyrycord)
        
    monster(monsterxcord, monsterycord)

    doorcollision = collided(doorxcord, doorycord, plyrxcord, plyrycord) 
    if doorcollision == True:
        plyrxcord = 75
        plyrycord = 300
        plyrhealth += 100
        plyrattack += 50
        plyrdefend += 50
        
    
#    if collision == True:
#        monster = 0
        # monster image turn highlighted
        # if player hit monster take damage
        # randomize monster hit or defend 

    
    player(plyrxcord,plyrycord)
    door(doorxcord, doorycord)
    pygame.display.update()

