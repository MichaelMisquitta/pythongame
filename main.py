import pygame
from enemy import enemy
from bird import flappybird
pygame.init()
pygame.display.init()
pygame.display.set_mode((400,400))
gamescreen = pygame.display.get_surface()
clock = pygame.time.Clock()
running = True
playerPos = pygame.Vector2(gamescreen.get_width()/2, gamescreen.get_height()/2)
playerVelocity = [0,0]
dt = 0
ground = gamescreen.get_height()*3/4

flappybird = flappybird(gamescreen,ground)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    gamescreen.fill("black")
    flappybird.draw()

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]:
        flappybird.bounceUp(-200,dt)

    flappybird.updateVelocity(dt)
    flappybird.updatePos(dt)
    
   

    pygame.display.flip()

    dt = clock.tick(60)/1000
    

pygame.quit()