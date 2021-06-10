import pygame
import random
from pprint import pprint
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
def collided (monsterxcord, monsterycord, playerxcord, playerycord):
    distance = ((monsterxcord - plyrxcord)**2 + (monsterycord - plyrycord)**2)**0.5
    if distance < 54:
        return True
    else:
        return False

#Monsters
monsterstats_file = open('monsterstats.csv')
monsterstats_text = monsterstats_file.read()

def get_headers(s):
    s = s[:s.find("\n")]
    g = s.split(",")
    return g

def get_data(s):
    s = s[s.find("\n")+1:len(s)-1]
    data = s.split("\n")
    order = 0
    while order < len(data):
        data[order] = data[order].split(",")
        order += 1
    return data

def make_monster_dict(data):
    d = {}
    for x in data:
        y = x[0]
        sub_list = []
        order = 1
        while order < len(data[0]):
            sub_list.append(x[order])
            order += 1
        d[y] = sub_list
    return d
    
def combine_dict(d, headers):
    temp_dict = {}
    headers.remove(headers[0])
    for x in d:
        g = d[x]
        order = 0
        while order < len(g):
            temp_dict[headers[order]] = g[order]
            order += 1
        d[x] = temp_dict
        temp_dict = {}
    return d    

monster_headers = get_headers(monsterstats_text)
monster_data = get_data(monsterstats_text)
monster_dict = make_monster_dict(monster_data)
monster_combine = combine_dict(monster_dict, monster_headers)

monster_list = []
for x in monster_data:
    monster_list.append(x[0])

monsternumber = 5
order = 0
monsters = []
while order < monsternumber:
    monsters.append(random.choice(monster_list))
    order += 1

def make_levels(dictionary, levels):
    answer = {}
    temp_dict = {}
    order = 0
    while order < len(levels):
        i = 0
        while i < 3:
            temp_dict[monster_list[i + (order * 3)]] = dictionary[monster_list[i + (order * 3)]]
            i += 1
        answer[levels[order]] = temp_dict
        temp_dict = {}
        order += 1
    return answer
    
levels = [1,2,3,4,5]
monsterstats = make_levels(monster_combine, levels)

#monster
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
#make sure ogres don't spawn in same area 
#    collide = True
#    while collide == True:
#        for x in ogrexcord:
#            if xcord = ogrexcord[x] 
#        xcord = random.choice(randomlist(150, 720))
#        ycord = random.choice(randomlist(50, 550))
monsterxcord = xcord
monsterycord = xcord
monsterxcordchange = 0
monsterycordchange = 0
monsterhealth = 10
monstermaxhealth = 10

def monster(avatar, x, y):
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
    

#Text
font = pygame.font.Font('freesansbold.ttf', 16)
smallfont = pygame.font.Font('freesansbold.ttf',8)
healthx = 10
healthy = 10

def show_health(x,y):
    health = font.render("Health:" + str(plyrhealth) + '/' + str(plyrmaxhealth),True, black)
    screen.blit(health, (x, y))
def show_monsterhealth(x,y):
    monsterhealthdisplay = font.render(str(monsterhealth),True,black)
    screen.blit(monsterhealthdisplay, (x, y))

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
                attack(monsterhealth, plyrattack)
                monsterhealth -= plyrattack
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
    
    monsterxcord += monsterxcordchange
    
    #monster boundaries
    if -50 >= monsterxcord <= 0:
        monsterxcord = 1
    if 800 >= monsterxcord >= 740:
        monsterxcord = 739
    if -50 >= monsterycord <= 0:
        monsterycord = 1
    if 600 >= monsterycord >= 546:
        monsterycord = 544
    
    #Collision
    monstercollision = collided(monsterxcord, monsterycord, plyrxcord, plyrycord)
        
    doorcollision = collided(doorxcord, doorycord, plyrxcord, plyrycord) 
    if doorcollision == True:
        plyrxcord = 75
        plyrycord = 300
        plyrmaxhealth += 100
        plyrattack += 50
        plyrdefend += 50
        level += 1
    
    if monsterhealth <= 0:
        monsterxcord += 1000
        monsterycord += 1000
        monstersdead += 1 
        
        
    
#    if collision == True:
#        monster = 0
        # monster image turn highlighted
        # if player hit monster take damage
        # randomize monster hit or defend
        
    #chatlogs
    pygame.font.init
    pygame.font.quit
    show_monsterhealth(monsterxcord,monsterycord)
    show_health(healthx, healthy)
        
    player(plyrxcord,plyrycord)
    monster(monsterstats[level][monster_list[0]], monsterxcord, monsterycord)

    if monstersdead == level * 1:
        door(doorxcord, doorycord)
    pygame.display.update()
    if plyrhealth > plyrmaxhealth:
        plyrhealth = plyrmaxhealth
        
