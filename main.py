import pygame
from enemy import enemy
from bird import flappybird
pygame.init()
gamescreen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()
running = True
playerPos = pygame.Vector2(gamescreen.get_width()/2, gamescreen.get_height()/2)
playerVelocity = [0,0]
gravity = 100
dt = 0
ground = gamescreen.get_height()*3/4

flappybird = flappybird(playerPos)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    gamescreen.fill("black")
    flappybird.draw()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        flappybird.updatePos(0,-300*dt) 
    if keys[pygame.K_DOWN]:
        if playerPos.y+20 < ground:
            flappybird.updatePos(0,300*dt) 
        else:
            flappybird.setPos(0,ground-20) 
   
    if keys[pygame.K_SPACE]:
        flappybird.updateVelocity(0,-100)

    flappybird.updateVelocity(dt,ground)
   

    pygame.display.flip()

    dt = clock.tick(60)/1000
    

pygame.quit()