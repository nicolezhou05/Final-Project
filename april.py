import pygame
import random
#Colors
white = (255,255,255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
gray = (220,220,220)

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
plyrmaxhealth = 100
plyrattack = 5
plyrdefend = 10



def player(x,y):
    screen.blit(playeravatar, (x,y))

#determine if collided
def collided (ogrexcord, ogreycord, playerxcord, playerycord):
    distance = ((ogrexcord - plyrxcord)**2 + (ogreycord - plyrycord)**2)**0.5
    if distance < 54:
        return True
    else:
        return False

#ogre
def randomlist(minimum, maximum):
    answer = []
    order = minimum
    while order < maximum:
        answer.append(order)
        order += 1
    return answer


ogreavatar = pygame.image.load('ogre.png')
ogreavatar = pygame.transform.scale(ogreavatar, (60,55))
xcord = random.choice(randomlist(150, 720))
ycord = random.choice(randomlist(50, 550))
#make sure ogres don't spawn in same area 
#    collide = True
#    while collide == True:
#        for x in ogrexcord:
#            if xcord = ogrexcord[x] 
#        xcord = random.choice(randomlist(150, 720))
#        ycord = random.choice(randomlist(50, 550))
ogrexcord = xcord
ogreycord = xcord
ogrexcordchange = 0
ogreycordchange = 0
ogrehealth = 10
ogremaxhealth = 10

def ogre(x, y):
    screen.blit(ogreavatar, (x,y))
    
#Door 
dooravatar = pygame.image.load('door.png')
dooravatar = pygame.transform.scale(dooravatar, (60,55))
doorxcord = 730
doorycord = 545

def door(x, y):
    screen.blit(dooravatar, (x,y))
    
def attack(attackedhealth, attacker_attackstat):
    if ogrecollision == True and defend != True:
        attackedhealth -= attacker_attackstat
        print("attack")
        

def defend():
    if ogrecollision == True:
        defend = True 
        print("defend")
    

#Text
font = pygame.font.Font('freesansbold.ttf', 16)
smallfont = pygame.font.Font('freesansbold.ttf',8)
healthx = 10
healthy = 10

def show_health(x,y):
    health = font.render("Health:" + str(plyrhealth) + '/' + str(plyrmaxhealth),True, black)
    screen.blit(health, (x, y))
def show_ogrehealth(x,y):
    ogrehealthdisplay = font.render(str(ogrehealth),True,black)
    screen.blit(ogrehealthdisplay, (x, y))

level = 1
monstersdead = 0

#Game Loop
active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or plyrhealth <= 0:
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
                attack(ogrehealth, plyrattack)
                ogrehealth -= plyrattack
            if event.key == pygame.K_d:
                defend()
     
    #add while loop before screen fill. have list/dictioanry to refer to new monsters. list within list for order 0 equal to all monsters in first floor and order 2 to have list of all monsters in 3rd floor and then spawn in corresponding mosnters
    screen.fill(gray)
    monstersdead = 0

    #Player boundaries
    if plyrxcord <= 0:
        plyrxcord = 1
    if plyrxcord >= 740:
        plyrxcord = 739
    if plyrycord <= 0:
        plyrycord = 1
    if plyrycord >= 546:
        plyrycord = 544
    
    ogrexcord += ogrexcordchange
    
    #ogre boundaries
    if -50 >= ogrexcord <= 0:
        ogrexcord = 1
    if 800 >= ogrexcord >= 740:
        ogrexcord = 739
    if -50 >= ogreycord <= 0:
        ogreycord = 1
    if 600 >= ogreycord >= 546:
        ogreycord = 544
    
    #Collision
    ogrecollision = collided(ogrexcord, ogreycord, plyrxcord, plyrycord)
        
    doorcollision = collided(doorxcord, doorycord, plyrxcord, plyrycord) 
    if doorcollision == True:
        plyrxcord = 75
        plyrycord = 300
        plyrmaxhealth += 100
        plyrattack += 50
        plyrdefend += 50
        level += 1
    
    if ogrehealth <= 0:
        ogrexcord += 1000
        ogreycord += 1000
        monstersdead += 1 
        
        
    
#    if collision == True:
#        ogre = 0
        # ogre image turn highlighted
        # if player hit ogre take damage
        # randomize ogre hit or defend
        
    #chatlogs
    pygame.font.init
    pygame.font.quit
    show_ogrehealth(ogrexcord,ogreycord)
    show_health(healthx, healthy)
        
    player(plyrxcord,plyrycord)
    ogre(ogrexcord, ogreycord)

    if monstersdead == level * 1:
        door(doorxcord, doorycord)
    pygame.display.update()
    if plyrhealth > plyrmaxhealth:
        plyrhealth = plyrmaxhealth
