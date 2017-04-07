import pygame

class WhiteFlag:
    """Create a WhiteFlag, the game's main character"""
    
    epsilon = 10
    
    pos = {
        'x':0,
        'y':0
    }
    
    def __init__(self, coordinates):
        """Define the main features of the character"""
        self.size = 50
        self.hp = 100
        self.color = (0,255,255)
        self.speed = 2
        self.i = 0
        self.pos['x'] = coordinates[self.i][0]
        self.pos['y'] = coordinates[self.i][1]
        self.dir_x = 0
        self.dir_y = 0
        
    def Pos_x(self):
        return self.pos['x'] - self.size/2 ; 
    
    def Pos_y(self):
        return self.pos['y'] - self.size/2 ; 
    
    
    def Distance(self, point1, point2):
        return ((point1['x']-point2[0])**2 + (point1['y']-point2[1])**2)**0.5
    
    def Verify_distance(self,coordinates):
        
        if self.Distance(self.pos,coordinates[self.i]) < self.epsilon:
            return True
        else:
            return False
        
    
    def Move(self, coordinates):
        if(self.i < len(coordinates)): 
            if self.Verify_distance(coordinates):
                # Moves to the next point
                self.i += 1
                if(self.i < len(coordinates)):
                    self.dir_x = (coordinates[self.i][0] - self.pos['x'])/self.Distance(self.pos,coordinates[self.i])
                    self.dir_y = (coordinates[self.i][1] - self.pos['y'])/self.Distance(self.pos,coordinates[self.i])
                    print(self.dir_x)
                    print(self.dir_y)

                    self.pos['x'] += self.speed * self.dir_x
                    self.pos['y'] += self.speed * self.dir_y
                
            else:
                # Still trying to reach the point
                self.pos['x'] += self.speed * self.dir_x
                self.pos['y'] += self.speed * self.dir_y
            
        
   
    def Take_damage(self,x):
        self.hp -= x
    
        
    def Draw(self, gameDisplay):
        pygame.draw.rect(gameDisplay,self.color,[self.Pos_x(),self.Pos_y(),self.size,self.size])
        
            
        
    def Death(self):
        if self.hp <= 0:
            return True
        else:
            return False
        
    def Update(self,coordinates):
        self.Move(coordinates)
