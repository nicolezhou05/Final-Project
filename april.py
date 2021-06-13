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
plyrhealth = 25
plyrmaxhealth = 25
plyrattack = 5

def player(x,y):
    screen.blit(playeravatar, (x,y))

#determine if collided
def collided (monsterxcord1, monsterycord1, playerxcord, playerycord):
    distance = ((monsterxcord1 - plyrxcord)**2 + (monsterycord1 - plyrycord)**2)**0.5
    if distance < 54:
        return True
    else:
        return False

level = 1
monstersdead = 0

#Monsters dictionary
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
            if order < len(data[0])-3:
                sub_list.append(int(x[order]))
            else:
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
    i = 0
    while i < 3:
        temp_dict[monster_list[15]] = dictionary[monster_list[15]]
        i += 1
    answer[6] = temp_dict
    return answer
    
levels = [1,2,3,4,5]
monsterstats = make_levels(monster_combine, levels)

#Monsters
def randomlist(minimum, maximum):
    answer = []
    order = minimum
    while order < maximum:
        answer.append(order)
        order += 1
    return answer

monsteravatar1 = pygame.image.load(monsterstats[level][monster_list[0 + ((level - 1) * 3)]]['Image'])
monsteravatar1 = pygame.transform.scale(monsteravatar1, (60,55))
xcord = random.choice(randomlist(200, 700))
ycord = random.choice(randomlist(100, 500))
monsterxcord1 = xcord
monsterycord1 = xcord
monsterxcordchange1 = 0
monsterycordchange1 = 0
monsterhealth1 = monsterstats[level][monster_list[0 + ((level - 1) * 3)]]['Health']
monstermaxhealth1 = monsterstats[level][monster_list[0 + ((level - 1) * 3)]]['Health']
monsterdamage1 = monsterstats[level][monster_list[0 + ((level - 1) * 3)]]['Damage']
monsterspeed1 = monsterstats[level][monster_list[0 + ((level - 1) * 3)]]['Speed']                                 

monsteravatar2 = pygame.image.load(monsterstats[level][monster_list[1 + ((level - 1) * 3)]]['Image'])
monsteravatar2 = pygame.transform.scale(monsteravatar2, (60,55))
monsterxcord2 = random.choice(randomlist(200, 700))
monsterycord2 = random.choice(randomlist(100, 500))
monsterxcordchange2 = 0
monsterycordchange2 = 0
monsterhealth2 = monsterstats[level][monster_list[1 + ((level - 1) * 3)]]['Health']
monstermaxhealth2 = monsterstats[level][monster_list[1 + ((level - 1) * 3)]]['Health']
monsterdamage2 = monsterstats[level][monster_list[1 + ((level - 1) * 3)]]['Damage']
monsterspeed2 = monsterstats[level][monster_list[1 + ((level - 1) * 3)]]['Speed']

monsteravatar3 = pygame.image.load(monsterstats[level][monster_list[2 + ((level - 1) * 3)]]['Image'])
monsteravatar3 = pygame.transform.scale(monsteravatar3, (60,55))
monsterxcord3 = random.choice(randomlist(200, 700))
monsterycord3 = random.choice(randomlist(100, 500))
monsterxcordchange3 = 0
monsterycordchange3 = 0
monsterhealth3 = monsterstats[level][monster_list[2 + ((level - 1) * 3)]]['Health']
monstermaxhealth3 = monsterstats[level][monster_list[2 + ((level - 1) * 3)]]['Health']
monsterdamage3 = monsterstats[level][monster_list[2 + ((level - 1) * 3)]]['Damage']
monsterspeed3 = monsterstats[level][monster_list[2 + ((level - 1) * 3)]]['Speed']

def monster(avatar, x, y):
    screen.blit(avatar, (x,y))

#portal 
portalavatar = pygame.image.load('portal.png')
portalavatar = pygame.transform.scale(portalavatar, (60,55))
portalxcord = 730
portalycord = 545

def portal(x, y):
    screen.blit(portalavatar, (x,y))
    
def attack(attackedhealth, attacker_attackstat):
    if (monstercollision1 == True) or (monstercollision2 == True) or (monstercollision3 == True):
        attackedhealth -= attacker_attackstat
    
#Text
font = pygame.font.Font('freesansbold.ttf', 16)
smallfont = pygame.font.Font('freesansbold.ttf',8)
healthx = 10
healthy = 10
levelx = 710
levely = 10


def show_health(x,y):
    health = font.render("Health:" + str(plyrhealth//1) + '/' + str(plyrmaxhealth),True, black)
    screen.blit(health, (x, y))
    
def show_level(x,y):
    showlevel = font.render("Level " + str(level),True, black)
    screen.blit(showlevel, (x, y))
    
def show_monsterhealth1(x,y):
    monsterhealthdisplay1 = font.render(str(monsterhealth1),True,black)
    screen.blit(monsterhealthdisplay1, (x - 15, y))
    
def show_monsterhealth2(x,y):
    monsterhealthdisplay2 = font.render(str(monsterhealth2),True,black)
    screen.blit(monsterhealthdisplay2, (x - 15, y))

def show_monsterhealth3(x,y):
    monsterhealthdisplay3 = font.render(str(monsterhealth3),True,black)
    screen.blit(monsterhealthdisplay3, (x - 15, y))

totalmonstersdead = 0

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
                print(totalmonstersdead)
                if monstercollision1 == True:
                    attack(monsterhealth1, plyrattack)
                    monsterhealth1 -= plyrattack
                if monstercollision2 == True:
                    attack(monsterhealth2, plyrattack)
                    monsterhealth2 -= plyrattack
                if monstercollision3 == True:
                    attack(monsterhealth3, plyrattack)
                    monsterhealth3 -= plyrattack
     
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
    
    monsterxcord1 += monsterxcordchange1
    monsterxcord2 += monsterxcordchange2
    monsterxcord3 += monsterxcordchange3

    
    #monster boundaries
    if -5000 <= monsterxcord1 <= 0:
        monsterxcord1 = 1
    if 8000 >= monsterxcord1 >= 740:
        monsterxcord1 = 739
    if -5000 <= monsterycord1 <= 0:
        monsterycord1 = 1
    if 6000 >= monsterycord1 >= 546:
        monsterycord1 = 544
    
    #Collision
    monstercollision1 = collided(monsterxcord1, monsterycord1, plyrxcord, plyrycord)
    monstercollision2 = collided(monsterxcord2, monsterycord2, plyrxcord, plyrycord)
    monstercollision3 = collided(monsterxcord3, monsterycord3, plyrxcord, plyrycord)
        
    portalcollision = collided(portalxcord, portalycord, plyrxcord, plyrycord)
        
    if plyrxcord > monsterxcord1:
        monsterxcord1 += int(monsterspeed1)/500
    if plyrxcord < monsterxcord1:
        monsterxcord1 -= int(monsterspeed1)/500
    if plyrycord > monsterycord1:
        monsterycord1 += int(monsterspeed1)/500
    if plyrycord < monsterycord1:
        monsterycord1 -= int(monsterspeed1)/500
    if plyrxcord > monsterxcord2:
        monsterxcord2 += int(monsterspeed2)/500
    if plyrxcord < monsterxcord2:
        monsterxcord2 -= int(monsterspeed2)/500
    if plyrycord > monsterycord2:
        monsterycord2 += int(monsterspeed2)/500
    if plyrycord < monsterycord2:
        monsterycord2 -= int(monsterspeed2)/500
    if plyrxcord > monsterxcord3:
        monsterxcord3 += int(monsterspeed3)/500
    if plyrxcord < monsterxcord3:
        monsterxcord3 -= int(monsterspeed3)/500
    if plyrycord > monsterycord3:
        monsterycord3 += int(monsterspeed3)/500
    if plyrycord < monsterycord3:
        monsterycord3 -= int(monsterspeed3)/500
    
    if monstercollision1 == True:
        plyrhealth -= monsterdamage2/600
    if monstercollision2 == True:
        plyrhealth -= monsterdamage2/600
    if monstercollision3 == True:
        plyrhealth -= monsterdamage3/600

    
    if monsterhealth1 <= 0:
        monsterxcord1 += 1000
        monsterycord1 += 1000
        monstersdead += 1
        if level == 6:
            endmessage = font.render(("GG! You won!"),True,black)
            screen.blit(endmessage, (400, 300))

    if monsterhealth2 <= 0:
        monsterxcord2 += 1000
        monsterycord2 += 1000
        monstersdead += 1

    if monsterhealth3 <= 0:
        monsterxcord3 += 1000
        monsterycord3 += 1000
        monstersdead += 1
    
    if plyrhealth <= 0:
        deathmessage = font.render(("You Lose!"),True,black)
        screen.blit(deathmessage, (400,300))
#    if collision == True:
#        monster = 0
        # monster image turn highlighted
        # if player hit monster take damage
        
    #chatlogs
    pygame.font.init
    pygame.font.quit
    show_monsterhealth1(monsterxcord1,monsterycord1)
    show_monsterhealth2(monsterxcord2,monsterycord2)
    show_monsterhealth3(monsterxcord3,monsterycord3)

    show_health(healthx, healthy)
    show_level(levelx, levely)
        
    player(plyrxcord,plyrycord)
    monster(monsteravatar1, monsterxcord1, monsterycord1)
    monster(monsteravatar2, monsterxcord2, monsterycord2)
    monster(monsteravatar3, monsterxcord3, monsterycord3)
    
    
    if monstersdead == 3:
        portal(portalxcord, portalycord)
        if portalcollision == True:
            plyrxcord = 75
            plyrycord = 300
            plyrmaxhealth += 10
            plyrhealth += 10
            plyrattack += random.randint(1,5)
            level += 1
            totalmonstersdead += monstersdead
#if multiple of 7 increase loop by 1
            
#            if level == 7:
            
#                pygame.display.quit()
#                active = False
#                quit()
                
            #Monster Setups
            monsteravatar1 = pygame.image.load(monsterstats[level][monster_list[0 + ((level - 1) * 3)]]['Image'])
            monsteravatar1 = pygame.transform.scale(monsteravatar1, (60,55))
            monsterxcord1 = random.choice(randomlist(200, 700))
            monsterycord1 = random.choice(randomlist(100, 500))
            monsterhealth1 = monsterstats[level][monster_list[0 + ((level - 1) * 3)]]['Health']
            monstermaxhealth1 = monsterstats[level][monster_list[0 + ((level - 1) * 3)]]['Health']
            monsterdamage1 = monsterstats[level][monster_list[0 + ((level - 1) * 3)]]['Damage']
        
            if level != 6:
                monsteravatar2 = pygame.image.load(monsterstats[level][monster_list[1 + ((level - 1) * 3)]]['Image'])
                monsteravatar2 = pygame.transform.scale(monsteravatar2, (60,55))
                monsterxcord2 = random.choice(randomlist(200, 700))
                monsterycord2 = random.choice(randomlist(100, 500))
                monsterhealth2 = monsterstats[level][monster_list[1 + ((level - 1) * 3)]]['Health']
                monstermaxhealth2 = monsterstats[level][monster_list[1 + ((level - 1) * 3)]]['Health']
                monsterdamage2 = monsterstats[level][monster_list[1 + ((level - 1) * 3)]]['Damage']

                monsteravatar3 = pygame.image.load(monsterstats[level][monster_list[2 + ((level - 1) * 3)]]['Image'])
                monsteravatar3 = pygame.transform.scale(monsteravatar3, (60,55))
                monsterxcord3 = random.choice(randomlist(200, 700))
                monsterycord3 = random.choice(randomlist(100, 500))
                monsterhealth3 = monsterstats[level][monster_list[2 + ((level - 1) * 3)]]['Health']
                monstermaxhealth3 = monsterstats[level][monster_list[2 + ((level - 1) * 3)]]['Health']
                monsterdamage3 = monsterstats[level][monster_list[2 + ((level - 1) * 3)]]['Damage']
    
    pygame.display.update()
    if plyrhealth > plyrmaxhealth:
        plyrhealth = plyrmaxhealth
        
