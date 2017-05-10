#! /usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit
from random import randrange

class Map:
	def getWayPoints(self):
		return self.wayPoints

	def __getitem__(self, index):
		return self.wayPoints[index]

	def __len__(self):
		return len(self.wayPoints)

	def DrawBg(self, screen):
		screen.blit(self.background, (0, 0))


class Map1(Map):
	wayPoints = [(108, 105), (108, 466), (317, 466), (317, 110), (758, 110), (758, 475)]
	# image = pygame.load_image()
	towerPositions = [(540, 110)]
	tankPositions = [(755, 250)]
	def __init__(self):
		self.background_filename = 'background.png'
		self.background = pygame.image.load(self.background_filename).convert()

	playerTankQnt = 1
	playerTowerQnt = 1

class Map2(Map):
	pass