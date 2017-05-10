import pygame
from bullet import *

class EnemyTower:
    
    def __init__(self, x=0, y=0, range_base=200, size=100, color="red"):
        self.x = x
        self.y = y
        self.hp = 100
        self.range_base = range_base
        self.size = size
        self.damage = 40
        self.color = color
        self.list_bullets = []
        self.cooldown = 0
    
    def Draw(self, gameDisplay):
        pygame.draw.rect(gameDisplay, (250,0,0), [self.x - self.size/2, self.y-self.size/2,self.size,self.size])
        for bullet in self.list_bullets:
            bullet.Draw(gameDisplay)

    def Is_Dead(self):
        if self.hp <= 0: # morreu
            return True
        else: # still breathing
            return False

    def Distance(self, x, y): # Calcula a distância entre dois pontos quaisquer x = (x1,x2) e y = (y1,y2)
        return ((x[0]-y[0])**2 + (x[1]-y[1])**2)**0.5

    def Verify_distance(self, criteria, x,y): # Verifica se dois pontos estão suficientemente próximos:
        if self.Distance(x,y) < criteria: # Suficientemente próximos
            return True
        else:
            return False

    def CanShoot(self, list_of_soldiers): #list_of_enemies contem as coordenadas de onde estao localizadas os inimigos 
        inimigo_proximo = False
        n = len(list_of_soldiers)
        for i in range (0,n): #Verificará se não há algum inimigo vivo próximo com relacao ao centro do jogador
            if self.Verify_distance(self.range_base,(self.x,self.y),(list_of_soldiers[i].posx,list_of_soldiers[i].posy)):
                #Guima, aqui eu encarei a list_of_enemies como a lista de objetos inimigos. Tem que ver se a posição deles
                # é dada pelo .x e .y ali tbm (tem q ver no pgm do Uchida), além de verificar se a torre do Uchida tem
                # o método Is_Dead (supus que tenha)
                inimigo_proximo = True
                
        return inimigo_proximo

    def Shoot(self, list_soldiers, list_bullets):
        n = len(list_soldiers)
        if n>0:
            min_distance=((list_soldiers[0].posx-self.x)**2 + (list_soldiers[0].posy-self.y)**2)**0.5
            ind = 0
            for i in range(1,n):
                aux = ((list_soldiers[i].posx-self.x)**2 + (list_soldiers[i].posy-self.y)**2)**0.5
                if aux < min_distance:
                    min_distance = aux
                    ind = i
            bullet_temporary = Bullet(self.x, self.y, list_soldiers[ind].posx, list_soldiers[ind].posy)
            self.list_bullets.append(bullet_temporary)
        self.cooldown = 2000
    
    def TakeDamage(self,x): # Caso o Whiteflag seja atingido, ele perderá hp
        self.hp -=x
        print("tomei dano e sou torre do mau")

    def Update(self, list_soldiers, gameDisplay):
        #atiro

        if self.cooldown <= 0 and self.CanShoot(list_soldiers):
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
                if 20 > (((self.list_bullets[i].x-list_soldiers[j].posx)**2 + (self.list_bullets[i].y-list_soldiers[j].posy)**2)**0.5):
                        print("Pew!!")
                        list_soldiers[j].TakeDamage(self.damage)
                        self.list_bullets.pop(i)
                        break
