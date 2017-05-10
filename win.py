import pygame
from sys import exit
from button import *
from button2 import *

white = (255, 255, 255)

class Win:
    def __init__(self, manager):

        self.manager = manager
        self.sou = 0
       

    def YouWin (self, screen):
        size_font = 150
        font = pygame.font.SysFont(None,size_font)
        screen_text = font.render("You Win!", True, (255,255,255))
        screen.blit(screen_text, [300, 250])
        
    def Execute(self, screen, gameController): 
        self.button1 = Button2( 120, 400, 180, 90, action = self.manager.CreateLvl, ac = white, ic = (0,255,0), image_name = "Return to main menu", size = 20, argument = (self.manager.currLvl + 1))
        self.button2 = Button2( 650, 400, 180, 90, action = exit, ac = white, ic = (0,255,0), image_name = "QUIT", size = 20)
        
        gameController.Draw(screen)
        if self.sou == 0:
            sound = pygame.mixer.Sound("uwin.wav")
            pygame.mixer.Sound.play(sound)
            self.sou = 1
        self.YouWin(screen)
        self.button1.Update(screen)
        self.button2.Update(screen)
