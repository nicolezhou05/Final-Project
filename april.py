#Enemy
enemyImg = pygame.image.load('ogre.png')
enemyxcord = 300
enemyycord = 500
enemyxcordchange = 0 

#determine if collided
def collided (monsterxcord, monsterycord, playerxcord, playerycord):
    distance = ((monsterxcord - playerxcord)**2 + (monsterycord - playerycord)**2)**0.5
    if distance < 54:
        return True
    else:
        return False
    
collision = collided(monsterxcord, monsterycord, playerxcord, playerycord)

# if collision:
# monster image turn highlighted
# if player hit monster take damage
# randomize monster hit or defend 
