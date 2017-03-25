#! /usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit
from random import randrange

pygame.init()

screen = pygame.display.set_mode((956, 560), 0, 32)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()