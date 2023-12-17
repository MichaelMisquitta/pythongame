import pygame
class flappybird(pygame.sprite.Sprite):
    gravity = 400
    
    def __init__(self, gamescreen,ground):
        self.gamescreen = gamescreen
        self.ground = ground
        self.playerPos = pygame.Vector2(self.gamescreen.get_width()/2, self.gamescreen.get_height()/2)
        self.playerVelocity = pygame.Vector2(0,0)

    def updatePos(self,dt):
        self.playerPos.y += self.playerVelocity.y*dt
        if self.playerPos.y+20 > self.ground:
            self.playerPos.y = self.ground - 20
            self.playerVelocity.y = 0
    
    def setPos(self,x,y):
        self.playerPos.x = x
        self.playerPos.y = y

    def draw(self,):
        pygame.draw.circle(self.gamescreen,"red",self.playerPos,20)

    def bounceUp(self,vy,dt):
        self.playerVelocity.y = vy
        

    def updateVelocity(self,dt):
        self.playerVelocity.y += self.gravity*dt

    