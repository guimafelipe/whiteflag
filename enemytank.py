import pygame
from bullet import *

class EnemyTank:
    def __init__(self, x=0, y=0, range_base=70, size=100, color="red"):
        self.size = 50
        self.hp = 100
        self.damage = 70
        self.color = (0,0,0)
        self.x = x
        self.y = y
        self.range_base_detection = 70
        self.range_base_explosion = self.range_base_detection*1.5
        self.already_exploded = False
        self.isDead = False
        self.cooldown = 500
        self.cooldown_explosion = 300
        
    def Draw(self, gameDisplay):
        pygame.draw.rect(gameDisplay, self.color, [self.x - self.size/2, self.y-self.size/2,self.size,self.size])
        
    def Is_Dead(self):
        if self.hp <= 0: # morreu
            return True
        else: # still breathing
            return False
    
    def Explosion(self, list_soldiers, gameDisplay):
        if self.cooldown_explosion > 0:
            self.cooldown_explosion -= 30
        else:
            self.hp = 0
            red = (250,0,0)
            pygame.draw.rect(gameDisplay, red, [self.x - self.range_base_explosion/2, self.y - self.range_base_explosion/2,self.range_base_explosion,self.range_base_explosion])
            n = len(list_soldiers)
            for j in range(n):
                if self.range_base_explosion >= (((list_soldiers[j].posx-self.x)**2 + (list_soldiers[j].posy-self.y)**2)**0.5):      
                    list_soldiers[j].hp = list_soldiers[j].hp - damage
    
    def Update(self, list_soldiers, gameDisplay):
        if self.already_exploded:
            self.cooldown -= 30
            if self.cooldown < 0:
                Explosion(self, list_soldiers, gameDisplay)
        else:
            #check range detection
            n = len(list_soldiers)
            for i in range(n):
                if self.range_base_detection >= (((list_soldiers[i].posx-self.x)**2 + (list_soldiers[i].posy-self.y)**2)**0.5):  
                    print("Enemy tank explosion!")
                    self.already_exploded = True
                    break
        