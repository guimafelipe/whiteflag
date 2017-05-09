# Criando a torre do jogador
import pygame
from bullet import *
from PlayerUnit import *


class PlayerTower(PlayerUnit):
    
    
    def __init__(self,coord):
        self.epsilon = 10 # Range para o jogador mudar em direção à próxima coordenada do mapa
        self.epsilon2 = 150 # Range o qual o jogador que está caminhando irá parar caso fique a uma distância <20 de um dos enemies
        self.hp = 50 # Hp
        self.size = 30
        self.color = (0,0,225) #Blue
        self.speed = 3
        self.damage = 40
        self.list_bullets = []
        self.cooldown = 0 # Copiei do Uchida, não sei o que isso faz kk
        self.Awake(coord)
        
    def Stop(self,list_of_enemies): #list_of_enemies contem as coordenadas de onde estao localizadas os inimigos 
        inimigo_proximo = False
        n = len(list_of_enemies)
        for i in range (0,n): #Verificará se não há algum inimigo vivo próximo com relacao ao centro do jogador
            if self.Verify_distance(self.epsilon2,(self.posx,self.posy),(list_of_enemies[i].x,list_of_enemies[i].y)):
                #Guima, aqui eu encarei a list_of_enemies como a lista de objetos inimigos. Tem que ver se a posição deles
                # é dada pelo .x e .y ali tbm (tem q ver no pgm do Uchida), além de verificar se a torre do Uchida tem
                # o método Is_Dead (supus que tenha)
                inimigo_proximo = True
                
        return inimigo_proximo
    
    def Draw(self,gameDisplay):
        pygame.draw.rect(gameDisplay,self.color,[self.Pos_x(),self.Pos_y(),self.size,self.size])
        for bullet in self.list_bullets: # Copiei da parte do Uchida esse trecho tb
            bullet.Draw(gameDisplay)
            
    def Shoot(self, list_of_enemies):
        # Primeiro passo: Achar o inimigo mais próximo
        n = len(list_of_enemies)
        if n>0:
            min_distance= self.Distance((list_of_enemies[0].x,list_of_enemies[0].y),(self.posx,self.posy))
            ind = 0
            for i in range(1,n):
                if self.Verify_distance(min_distance,(list_of_enemies[ind].x,list_of_enemies[ind].y),(self.posx,self.posy)):
                    min_distance = self.Distance((list_of_enemies[i].x,list_of_enemies[i].y),(self.posx,self.posy))
                    ind = i
            # Após achar, faz essa parada que tava no código do Uchida
            
            bullet_temporary = Bullet(self.posx, self.posy, list_of_enemies[ind].x, list_of_enemies[ind].y)
            self.list_bullets.append(bullet_temporary)
        self.cooldown = 2000
    

    def Update(self, coord, list_of_enemies, gameDisplay):
        if self.Stop(list_of_enemies): # Se é preciso parar
            # Código abaixo copiei do Uchida
             
            #atiro
            if self.cooldown <= 0:
                self.Shoot(list_of_enemies)
                self.cooldown = 2000
            else:
                self.cooldown -= 30
    
            #elimino as que sumiram da tela
            bullet_dead = True
            max_distance = 1000
            while bullet_dead and 0 < len(self.list_bullets):
                if self.Distance(self.list_bullets[0], (self.posx, self.posy)) > max_distance:
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
                for j in range(len(list_of_enemies)): 
                    if 20 > self.Distance((self.list_bullets[i].x,self.list_bullets[i].y),(list_of_enemies[j].x,list_of_enemies[j].y)):
                            print("Pew!!")
                            list_of_enemies[j].TakeDamage(self.damage)
                            self.list_bullets.pop(i)
                            break
    
        else: # Estará movimentando
            self.Walk(coord)
        if self.i == len(coord) - 1:
            self.hp = -1

    
    def Start(self):
        self.Update()
