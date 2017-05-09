#! /usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit
from random import randrange
from mapa1 import *
from White_Flag import *
from tower import *
from PlayerTower import *
from PlayerTank import *
from enemytower import *
from enemytank import *

class GameController:
	player = []
	enemies = []
	spawnedWhiteFlag = False

	level = 1

	buttons = []

	def __init__(self):
		self.mapLane = Map1()
		for tower in self.mapLane.towerPositions:
			self.createTower(tower[0], tower[1])
		#createButtons()
		for tank in self.mapLane.tankPositions:
			self.createTank(tank[0], tank[1])

	def createButtons(self):
		pass

	def getLevel(self, lvlNum):
		pass

	def sendWhiteFlag(self):
		white_flag = WhiteFlag(self.mapLane)
		self.player.append(white_flag)
		self.spawnedWhiteFlag = True
		self.white_flag = white_flag

	def sendPlayerTower(self):
		player_tower = PlayerTower(self.mapLane)
		self.player.append(player_tower)

	def sendPlayerTank(self):
		player_tank = PlayerTank(self.mapLane)
		self.player.append(player_tank)

	def createTower(self, x, y):
		tower = EnemyTower(x,y)
		self.enemies.append(tower)

	def createTank(self, x, y):
		tank = EnemyTank(x,y)
		self.enemies.append(tank)

	def getCommand(self):
		pressed_keys = pygame.key.get_pressed()
		if pressed_keys[K_SPACE]:
			self.sendWhiteFlag()
		if pressed_keys[K_1]:
			self.sendPlayerTower()
		if pressed_keys[K_2]:
			self.sendPlayerTank()

	def Update(self, screen):
		self.getCommand()

		foundDead = True
		while foundDead:
			foundDead = False
			for i in range(len(self.enemies)):
				if(self.enemies[i].Is_Dead()):
					self.enemies.pop(i)
					foundDead = True
					break
			for i in range(len(self.player)):
				if(self.player[i].Is_Dead()):
					self.player.pop(i)
					foundDead = True
					break

		for enemy in self.enemies:
			enemy.Update(self.player, screen)
		for unit in self.player:
			unit.Update(self.mapLane, self.enemies, screen)

		if self.spawnedWhiteFlag:
			if self.white_flag.Is_Dead():
				#game lost
				print("Lose")
			if self.white_flag.Got_End():
				#game win
				print("Win")

	def Draw(self, screen):
		for enemy in self.enemies:
			enemy.Draw(screen)
		for unit in self.player:
			unit.Draw(screen)