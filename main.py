import pygame
pygame.init()
gamescreen = pygame.display.set_mode((400,400));
clock = pygame.time.Clock()
running = True
playerPos = pygame.Vector2(gamescreen.get_width()/2, gamescreen.get_height()/2)
playerVelocity = [0,0]
gravity = 100
dt = 0
ground = gamescreen.get_height()*3/4

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    gamescreen.fill("black")
    pygame.draw.circle(gamescreen,"red",playerPos,20)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        playerPos.y -= 300*dt
    if keys[pygame.K_DOWN]:
        if playerPos.y+20 < ground:
            playerPos.y += 300*dt
        else:
            playerPos.y = ground - 20
    if keys[pygame.K_LEFT]:
        playerPos.x -= 300*dt
    if keys[pygame.K_RIGHT]:
        playerPos.x += 300*dt
    if keys[pygame.K_SPACE]:
        playerVelocity[1] = -100

    #implement gravity and resistance here
        
    #gravity
    playerVelocity[1] += gravity*dt

    playerPos.y = playerVelocity[1]*dt + playerPos.y
    if playerPos.y+20 > ground:
        playerPos.y = ground - 20
        playerVelocity[1] = 0

    

    pygame.display.flip()

    dt = clock.tick(60)/1000
    

pygame.quit()