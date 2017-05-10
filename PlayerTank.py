import pygame
from bullet import *
from PlayerUnit import *

class PlayerTank(PlayerUnit):
    # Criando o tanque-bomba do jogador
    
    def __init__(self,coord):
        self.Awake(coord)
        self.epsilon = 10 # Range para o jogador mudar em direção à próxima coordenada do mapa
        self.epsilon2 = 20 # Range o qual o jogador que está caminhando irá parar caso fique a uma distância <20 de um dos enemies
        self.hp = 100 # Hp
        self.size = 30
        self.color = (0,225,0) #Green
        self.speed = 2.5
        self.damage = 30 # Quanto de dano ela dá
        self.damage_range = 100
        self.cooldown = 300
        self.cooldown_explosion = 400
        self.already_exploded = False # Copiei do Uchida
        self.range_base_explosion =  self.damage_range*1.5
        self.sprite_name = "green2.png"
        self.sprite = pygame.image.load(self.sprite_name).convert_alpha()
        self.showExplosion = False
       
        
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
            pygame.draw.rect(gameDisplay, (163,54,38), [self.posx - self.damage_range/2, self.posy - self.damage_range/2,self.damage_range,self.damage_range])
            sound = pygame.mixer.Sound("explosion.wav")
            pygame.mixer.Sound.play(sound)
        else:
            self.hp = 0 # Está morto, Is_Dead

            n = len(list_of_enemies)
            for j in range(n):
                if self.range_base_explosion/2 >= self.Distance((list_of_enemies[j].x,list_of_enemies[j].y),(self.posx,self.posy)):      
                    list_of_enemies[j].hp = list_of_enemies[j].hp - self.damage
    
    

    def Update(self, coord, list_of_enemies, gameDisplay):
        if self.Stop(list_of_enemies): # Se é preciso parar, vai explodir
            # Código abaixo copiei do Uchida
             
            if self.already_exploded == True:
                self.cooldown -= 30
            if self.cooldown < 0:
                self.Explosion(list_of_enemies, gameDisplay)
                self.showExplosion = True
            else:
                #check range detection
                n = len(list_of_enemies)
                for i in range(n):
                    if self.damage_range/2 >= self.Distance((self.posx,self.posy),(list_of_enemies[i].x,list_of_enemies[i].y)):  
                        print("Player tank explosion!")
                        self.already_exploded = True
                        break     
    
        else: # Estará movimentando
            self.Walk(coord)
        if self.i == len(coord) - 1:
            self.hp = -1
    
    def Start(self):
        self.Update()

    def Draw(self,gameDisplay):
        gameDisplay.blit(pygame.transform.scale(self.sprite, (self.size, self.size)), (self.Pos_x(), self.Pos_y()))
        if self.showExplosion:
            pygame.draw.rect(gameDisplay, (163,54,38), [self.posx - self.damage_range/2, self.posy - self.damage_range/2,self.damage_range,self.damage_range])
            self.showExplosion = False