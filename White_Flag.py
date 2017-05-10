import pygame
from PlayerUnit import *

class WhiteFlag(PlayerUnit): # Cria a WhiteFlag

    def __init__(self,coord): # Principais características do personagem
        self.Awake(coord)
        self.epsilon = 10
        self.hp = 10  # HP da WhiteFlag
        self.size = 40 # Tamanho da Whiteflag (lado do quadrado)
        self.color = (255,255,255) #Cor da Whiteflag
        self.speed = 2 # Velocidade da whiteflag
        
        self.GetEnd = False
        self.sprite_name = "white flag.png"
        self.sprite = pygame.image.load(self.sprite_name).convert_alpha()
        
        
    def Stop(self,coord,list_of_enemies):
        # Não para
        return False
        
    def Got_End(self):
        return self.GetEnd
        
    def Start(self):
        self.Walk(coord)
        
        
    def Update(self, coord, list_of_enemies, gameDisplay):
        self.Walk(coord)
        if self.Is_Dead == False and self.Stop == False:
            self.Walk(coord)
            self.Draw(gameDisplay)
        if self.i == len(coord) - 1:
            self.GetEnd = True

    def Draw(self,gameDisplay):
        gameDisplay.blit(pygame.transform.scale(self.sprite, (self.size, self.size)), (self.Pos_x(), self.Pos_y()))

