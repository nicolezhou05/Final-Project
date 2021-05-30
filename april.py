#Enemy
enemyImg = pygame.image.load('ogre.png')
enemyxcord = 300
enemyycord = 500
enemyxcordchange = 0 

#determine if collided
def collided (monsterx, monstery, playerx, playery):
    distance = ((monsterx - playerx)**2 + (monstery - playery)**2)**0.5
    if distance < 54:
        return True
    else:
        return False
    
collision = collided(monsterx, monstery, playerx, playery)

# if collision:
# monster image turn highlighted
# if player hit monster take damage
# randomize monster hit or defend 
