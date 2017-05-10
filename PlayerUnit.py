import pygame

class PlayerUnit: # Ter� fun��es comuns a todas as unidades do jogador
    def Awake(self,coord):
        self.hp = 10 # Este hp ir� ser atualizado dependendo da unidade do jogador considerada
        self.size = 10 # Tamanho do quadrado considerado: A ser implementando em cada unidade espec�fica
        self.color = (0,0,0) #Cor a ser alterada dependendo da unidade do jogador
        self.i = 0 # indice da lista de posicoes que ele quer atingir
        self.posx = coord[self.i][0] # posicao inicial x (centro do quadrado)
        self.posy = coord[self.i][1] # posicao inicial y (centro do quadrado)
        self.dir_x = 0 # vetor direcao que o jogador ira seguir
        self.dir_y = 0 # vetor direcao que o jogador ira seguir

    def Distance(self, x, y): # Calcula a dist�ncia entre dois pontos quaisquer x = (x1,x2) e y = (y1,y2)
        return ((x[0]-y[0])**2 + (x[1]-y[1])**2)**0.5

    def Verify_distance(self, criteria, x,y): # Verifica se dois pontos est�o suficientemente pr�ximos:
        if self.Distance(x,y) < criteria: # Suficientemente pr�ximos
            return True
        else:
            return False
        
    def Walk(self, coord): # A Whiteflag ir� andar pelo mapa atrav�s dessa fun��o
        
        # Primeiramente ele ir� verificar se o centro do quadrado est� suficiente pr�ximo do pr�ximo ponto da lista de coordenadas
        
        if (self.i < len(coord) - 1): # Enquanto tivermos pontos a atingir:
            
            if self.Verify_distance(self.epsilon, (self.posx, self.posy), coord[self.i + 1]):
                self.i += 1 # O quadrado ir� se mover em direcao ao proximo ponto da lista
            
        # Criando o vetor dire��o unit�rio
            if (self.i < len(coord) -1):
                self.dir_x = (coord[self.i + 1][0] - self.posx)/self.Distance(coord[self.i + 1],(self.posx,self.posy))
                self.dir_y = (coord[self.i + 1][1] - self.posy)/self.Distance(coord[self.i + 1],(self.posx,self.posy))
            
                self.posx = self.posx + self.speed * self.dir_x
                self.posy = self.posy + self.speed * self.dir_y


    def Stop(self, list_of_something):
        pass
    
    def TakeDamage(self,x): # Caso o Whiteflag seja atingido, ele perder� hp
        self.hp -=x
        
        
    def Is_Dead(self): # Verifica que o Whiteflag morreu
        if self.hp <= 0: # morreu
            return True
        else: # still breathing
            return False

    def Pos_x(self): # Queremos que a posicao utilizada seja com respeito ao canto superior esquerdo da unidade do jogador
        return self.posx - self.size/2
    
    
    def Pos_y(self):
        return self.posy - self.size/2
    
    def Start(self):
        pass
    
    def Update(self):
        pass
    
    def Draw(self, gameDisplay):
        pygame.draw.rect(gameDisplay,self.color,[self.Pos_x(),self.Pos_y(),self.size,self.size])