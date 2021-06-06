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
def collided(x1, y1, x2, y2, distance):
    distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    if distance < distance:
        return True
    else:
        return False

#Monster
monsteravatar = []
monsterxcord = []
monsterycord = []
monsterxcordchange = []
monsterycordchange = []
monsterhealth = []
monsternumber = 5

def randomlist(minimum, maximum):
    answer = []
    order = minimum
    while order < maximum:
        answer.append(order)
        order += 1
    return answer

order = 0
while order < monsternumber:
    avatar = pygame.image.load('ogre.png')
    monsteravatar.append(pygame.transform.scale(avatar, (60,55)))
    xcord = random.choice(randomlist(150, 720))
    ycord = random.choice(randomlist(50, 550))
#make sure monsters don't spawn in same area 
#    collide = True
#    while collide == True:
#        for x in monsterxcord:
#            if xcord = monsterxcord[x] 
#        xcord = random.choice(randomlist(150, 720))
#        ycord = random.choice(randomlist(50, 550))
    order = 0
    while order < len(monsterxcord):
        collided(xcord, ycord, monsterxcord[order], monsterycord[order], 100)      
        while collided == True:
            xcord = random.choice(randomlist(150, 720))
            ycord = random.choice(randomlist(50, 550))
            collided(xcord, ycord, monsterxcord[order], monsterycord[order], 100)      
        order += 1
        
    monsterxcord.append(xcord)
    monsterycord.append(xcord)
    monsterxcordchange.append(0)
    monsterycordchange.append(0)
    monsterhealth.append(10)
    order += 1

def monster(x, y, avatar):
    screen.blit(monsteravatar[avatar], (x,y))
    
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
                attack(monsterhealth[order], plyrattack)
            if event.key == pygame.K_d:
                defend()

#            order = 0
#            while order < monsternumber:
#                if event.key == pygame.K_a:
#                    attack(monsterhealth[order], plyrattack)
#                if event.key == pygame.K_d:
#                    defend()
#                order += 1

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
    order = 0
    while order < monsternumber:
        if monsterxcord[order] <= 0:
            monsterxcord[order] = 1
        if monsterxcord[order] >= 740:
            monsterxcord[order] = 739
        if monsterycord[order] <= 0:
            monsterycord[order] = 1
        if monsterycord[order] >= 546:
            monsterycord[order] = 544
    
        #Collision
        monstercollision = collided(monsterxcord[order], monsterycord[order], plyrxcord, plyrycord, 54)
#            if collision == True:
#                monster = 0
        # monster image turn highlighted
        # if player hit monster take damage
        # randomize monster hit or defend         
        
        monster(monsterxcord[order], monsterycord[order], order)
        order += 1

    doorcollision = collided(doorxcord, doorycord, plyrxcord, plyrycord, 50) 
    if doorcollision == True:
        plyrxcord = 75
        plyrycord = 300
        plyrhealth += 100
        plyrattack += 50
        plyrdefend += 50

    
    player(plyrxcord,plyrycord)
    door(doorxcord, doorycord)
    pygame.display.update()

