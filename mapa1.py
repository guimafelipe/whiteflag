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
	towerPositions = [(540, 110)]
	tankPositions = [(755, 250)]
	def __init__(self):
		self.background_filename = 'background.png'
		self.background = pygame.image.load(self.background_filename).convert()

	playerTankQnt = 2
	playerTowerQnt = 2

class Map2(Map):
	wayPoints = [(108, 105), (108, 466), (317, 466), (317, 110), (538, 110), (538, 466), (758, 466), (758, 110)]
	towerPositions = [(108, 466), (108, 466), (670, 466)]
	tankPositions = [(108, 250), (390, 110)]
	def __init__(self):
		self.background_filename = 'background2.png'
		self.background = pygame.image.load(self.background_filename).convert()

	playerTankQnt = 3
	playerTowerQnt = 5

class Map3(Map):
	wayPoints = [(108, 105), (108, 466), (317, 466), (317, 110), (538, 110), (538, 466), (758, 466), (758, 110)]
	towerPositions = [(108, 150), (108, 466), (317, 400), (108, 466), (670, 466), (758, 300)]
	tankPositions = [(108, 250), (390, 110), (317, 466), (538, 466)]
	def __init__(self):
		self.background_filename = 'background3.png'
		self.background = pygame.image.load(self.background_filename).convert()

	playerTankQnt = 5
	playerTowerQnt = 6