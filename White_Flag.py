import pygame
from PlayerUnit import *

class WhiteFlag(PlayerUnit): # Cria a WhiteFlag

    def __init__(self,coord): # Principais características do personagem
        self.epsilon = 10
        self.hp = 10  # HP da WhiteFlag
        self.size = 20 # Tamanho da Whiteflag (lado do quadrado)
        self.color = (255,255,255) #Cor da Whiteflag
        self.speed = 2 # Velocidade da whiteflag
        self.Awake(coord)
        self.GetEnd = False
        
        
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
