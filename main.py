import pygame
pygame.init()
gamescreen = pygame.display.set_mode((400,400));
clock = pygame.time.Clock()
running = True
playerPos = pygame.Vector2(gamescreen.get_width()/2, gamescreen.get_height()/2)
dt = 0
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
        playerPos.y += 300*dt
    if keys[pygame.K_LEFT]:
        playerPos.x -= 300*dt
    if keys[pygame.K_RIGHT]:
        playerPos.x += 300*dt
    
    pygame.display.flip()

    dt = clock.tick(60)/1000
    

pygame.quit()