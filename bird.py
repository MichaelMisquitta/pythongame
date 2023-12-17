import pygame
class flappybird(pygame.sprite.Sprite):
    gravity = 100
    
    def __init__(self):
        
        
        self.playerPos = pygame.Vector2(pygame.display.get_width()/2, pygame.display.get_height()/2)
        self.playerVelocity = pygame.Vector2(0,0)

    def updatePos(self,x,y):
        self.playerPos.x += x
        self.playerPos.y += y
    
    def setPos(self,x,y):
        self.playerPos.x = x
        self.playerPos.y = y

    def draw(self):
        pygame.draw.circle(pygame.display,"red",self.playerPos,20)

    def updateVelocity(self,dt,ground):
        self.playerVelocity.y += self.gravity*dt
        self.playerPos.y += self.playerVelocity.y*dt
        if self.playerPos.y+20 > ground:
            self.playerPos.y = ground - 20
            self.playerVelocity.y = 0