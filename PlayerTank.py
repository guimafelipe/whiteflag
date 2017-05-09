import pygame
from bullet import *
from PlayerUnit import *

class PlayerTank(PlayerUnit):
    # Criando o tanque-bomba do jogador
    
    def __init__(self,coord):
        self.epsilon = 10 # Range para o jogador mudar em direção à próxima coordenada do mapa
        self.epsilon2 = 20 # Range o qual o jogador que está caminhando irá parar caso fique a uma distância <20 de um dos enemies
        self.hp = 50 # Hp
        self.size = 30
        self.color = (0,225,0) #Green
        self.speed = 2.5
        self.damage = 40 # Quanto de dano ela dá
        self.damage_range = self.epsilon2*1.5
        self.cooldown = 500
        self.cooldown_explosion = 300
        self.already_exploded = False # Copiei do Uchida
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
    
    
    
    def Explosion(self, list_of_enemies, gameDisplay):
        if self.cooldown_explosion > 0:
            self.cooldown_explosion -= 30
        else:
            self.hp = -0 # Está morto, Is_Dead

            pygame.draw.rect(gameDisplay, (255,0,0), [self.posx - self.damage_range/2, self.posy - self.damage_range/2,self.damage_range,self.damage_range])
            n = len(list_of_enemies)
            for j in range(n):
                if self.range_base_explosion >= self.Distance((list_of_enemies[j].x,list_of_enemies[j].y),(self.posx,self.posy)):      
                    list_of_enemies[j].hp = list_of_enemies[j].hp - damage
    
    

    def Update(self, coord, list_of_enemies, gameDisplay):
        if self.Stop(list_of_enemies): # Se é preciso parar, vai explodir
            # Código abaixo copiei do Uchida
             
            if self.already_exploded == True:
                self.cooldown -= 30
            if self.cooldown < 0:
                Explosion(self, list_of_enemies, gameDisplay)
            else:
                #check range detection
                n = len(list_of_enemies)
                for i in range(n):
                    if self.damage_range >= self.Distance((self.posx,self.posy),(list_of_enemies[i].x,list_of_enemies[i].y)):  
                        print("Player tank explosion!")
                        self.already_exploded = True
                        break     
    
        else: # Estará movimentando
            self.Walk(coord)

    
    def Start(self):
        self.Update()