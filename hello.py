#! /usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit
from random import randrange

pygame.init()


screen = pygame.display.set_mode((956, 560), 0, 32)

background_filename = 'bg_big.png'
background = pygame.image.load(background_filename).convert()

ship_filename = 'ship.png'
ship = pygame.image.load(ship_filename).convert_alpha()
ship_position = [randrange(956), randrange(560)]
speed = {
	'x':0,
	'y':0
	}
pygame.display.set_caption('Jogo Foda')

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_UP]:
    	ship_position[1] -= 10
    if pressed_keys[K_DOWN]:
    	ship_position[1] += 10
    if pressed_keys[K_RIGHT]:
    	ship_position[0] += 10
    if pressed_keys[K_LEFT]:
    	ship_position[0] -= 10

    screen.blit(background, (0, 0))
    ship_position[0] += speed['x']
    ship_position[1] += speed['y']
    screen.blit(ship, ship_position)
    pygame.display.update()
    time_passed = clock.tick(30)
