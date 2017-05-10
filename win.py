import pygame
from sys import exit
from button import *

white = (255, 255, 255)

class Win:
    def __init__(self):

        self.sou = 0
        self.button1 = Button( 120, 400, 180, 90, action = None, ac = white, ic = (0,255,0), image_name = "Return to main menu", qtd=0)
        self.button2 = Button( 650, 400, 180, 90, action = exit, ac = white, ic = (0,255,0), image_name = "QUIT", qtd=0)

    def YouWin (self, screen):
        size_font = 150
        font = pygame.font.SysFont(None,size_font)
        screen_text = font.render("You win!", True, (255,255,255))
        screen.blit(screen_text, [300, 250])
        
    def Execute(self, screen, gameController):
        
        gameController.Draw(screen)
        if self.sou == 0:
            sound = pygame.mixer.Sound("uwin.wav")
            pygame.mixer.Sound.play(sound)
            self.sou = 1
        self.YouWin(screen)
        self.button1.Update(screen)
        self.button2.Update(screen)
        
        
        
                                  