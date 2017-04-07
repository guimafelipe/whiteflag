#! /usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit
from random import randrange
from mapa1 import *
from whiteFlag import *
from tower import *

class Level1Controller:
	player = []
	enemies = []

	def __init__(self):
		self.mapLane = Map1()

	def sendWhiteFlag(self):
		white_flag = WhiteFlag(self.mapLane)
		self.player.append(white_flag)

	def createTower(self, x, y):
		tower = Tower(x,y)
		self.enemies.append(tower)

	def Update(self):
		for enemy in self.enemies:
			enemy.Update(self.player)
		for unity in self.player:
			unity.Update(self.mapLane)

	def Draw(self, screen):
		for enemy in self.enemies:
			enemy.Draw(screen)
		for unity in self.player:
			unity.Draw(screen)