#! /usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit
from random import randrange

from gamecontroller import *
from tower import *
from bullet import *
from mapa1 import *

pygame.init()

screen = pygame.display.set_mode((956, 650), 0, 32)

background_filename = 'background.png'
background = pygame.image.load(background_filename).convert()

gcontroller = GameController()
##Okgcontroller.createTower(540, 330)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    pressed_keys = pygame.key.get_pressed()

    screen.blit(background, (0, 0))
    gcontroller.Update(screen)
    gcontroller.Draw(screen)

    pygame.display.update()
    time_passed = clock.tick(30)
