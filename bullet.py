import pygame

class Bullet:
    
    def __init__(self, x_base, y_base, x_soldier=0, y_soldier=0, size=3, color=(0,255,0), speed_module=10):
        self.x = x_base
        self.y = y_base
        self.size = size
        self.color = color
        self.speed_x = speed_module*(x_soldier-x_base)/((x_soldier-x_base)**2 + (y_soldier-y_base)**2)**0.5
        self.speed_y = speed_module*(y_soldier-y_base)/((x_soldier-x_base)**2 + (y_soldier-y_base)**2)**0.5
        sprite_name = "cannonball.png"
        self.sprite = pygame.image.load(sprite_name).convert_alpha()
        
    def Draw(self, gameDisplay):
        # pygame.draw.rect(gameDisplay, self.color, [self.x, self.y,self.size,self.size])
        
        gameDisplay.blit(pygame.transform.scale(self.sprite, (10, 10)), (self.x, self.y))