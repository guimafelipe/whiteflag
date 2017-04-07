import pygame
from bullet import *

class Tower:
    
    def __init__(self, x=0, y=0, range_base=70, size=100, color="red"):
        self.x = x
        self.y = y
        self.range_base = range_base
        self.size = size
        self.color = color
        self.list_bullets = []
        self.cooldown = 0
    
    def Draw(self, gameDisplay):
        pygame.draw.rect(gameDisplay, (250,0,0), [self.x - self.size/2, self.y-self.size/2,self.size,self.size])
        for bullet in self.list_bullets:
            bullet.Draw(gameDisplay)

    def Shoot(self, list_soldiers, list_bullets):
        n = len(list_soldiers)
        if n>0:
            min_distance=((list_soldiers[0].pos['x']-self.x)**2 + (list_soldiers[0].pos['y']-self.y)**2)**0.5
            ind = 0
            for i in range(1,n):
                aux = ((list_soldiers[i].pos['x']-self.x)**2 + (list_soldiers[i].pos['y']-self.y)**2)**0.5
                if aux < min_distance:
                    min_distance = aux
                    ind = i
            bullet_temporary = Bullet(self.x, self.y, list_soldiers[ind].pos['x'], list_soldiers[ind].pos['y'])
            self.list_bullets.append(bullet_temporary)
        self.cooldown = 2000
    

    def Update(self, list_soldiers):
        #atiro
        if self.cooldown <= 0:
            self.Shoot(list_soldiers, self.list_bullets)
            self.cooldown = 2000
        else:
            self.cooldown -= 30

        #elimino as que sumiram da tela
        bullet_dead = True
        max_distance = 1000
        while bullet_dead and 0<len(self.list_bullets):
            if (((self.list_bullets[0].x-self.x)**2 + (self.list_bullets[0].y-self.y)**2)**0.5)>max_distance:
                self.list_bullets.pop(0)
            else:
                bullet_dead = False 
        
        #movimento as balas
        n = len(self.list_bullets)
        for i in range(n):
            self.list_bullets[i].x = self.list_bullets[i].x + self.list_bullets[i].speed_x
            self.list_bullets[i].y = self.list_bullets[i].y + self.list_bullets[i].speed_y

        #check bullet collision
        for i in range(n):
            for j in range(len(list_soldiers)): 
                if 20 > (((self.list_bullets[i].x-list_soldiers[j].pos['x'])**2 + (self.list_bullets[i].y-list_soldiers[j].pos['y'])**2)**0.5):
                        print("Pew!!")
                        self.list_bullets.pop(i)
                        break
