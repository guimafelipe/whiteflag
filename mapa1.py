#! /usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit
from random import randrange


class Map1:
	wayPoints = [(108, 105), (108, 466), (317, 466), (317, 110), (758, 110), (758, 475)]
	# image = pygame.load_image()
	towerPositions = [(540, 110)]
	tankPositions = [(755, 250)]

	playerTankQnt = 3
	playerTowerQnt = 3
	def getWayPoints(self):
		return self.wayPoints

	def __getitem__(self, index):
		return self.wayPoints[index]

	def __len__(self):
		return len(self.wayPoints)