import pygame
from sys import exit
from button import *
from button2 import *

color = (255, 255, 255)

class Lose:
    def __init__(self, manager):

        self.manager = manager
        self.sou = 0
        

    def YouLose (self, screen):
        size_font = 150
        font = pygame.font.SysFont(None, size_font)
        screen_text = font.render("You Lose!", True, (255,20,20))
        screen.blit(screen_text, [300, 250])
        
    def Execute(self, screen, gameController):
        self.button1 = Button2( 120, 400, 180, 90, action = self.manager.MenuScene, ac = color, ic = (0,255,0), image_name = "Return to main menu", size = 20)
        self.button2 = Button2( 650, 400, 180, 90, action = exit, ac = color, ic = (0,255,0), image_name = "QUIT", size = 20)
        gameController.Draw(screen)
        if self.sou == 0:
            sound = pygame.mixer.Sound("ulose.wav")
            pygame.mixer.Sound.play(sound)
            self.sou = 1
        self.YouLose(screen)
        self.button1.Update(screen)
        self.button2.Update(screen)