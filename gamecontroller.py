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
from button import *

class GameController:
	player = []
	enemies = []
	spawnedWhiteFlag = False

	level = 1

	buttons = []

	def __init__(self, mapObj):
		self.mapLane = mapObj
		for tower in self.mapLane.towerPositions:
			self.createTower(tower[0], tower[1])
		
		for tank in self.mapLane.tankPositions:
			self.createTank(tank[0], tank[1])
		
		self.playerTankQnt = self.mapLane.playerTankQnt
		self.playerTowerQnt = self.mapLane.playerTowerQnt
		
		self.createButtons()
		self.commandTicker = 10

		self.hasLost = False
		self.hasWon = False

	def createButtons(self):
		
		self.button1 = Button(100, 600, 180, 90,  self.sendPlayerTower, image_name = 'Tower', qtd = self.playerTowerQnt)
		self.button2 = Button(300, 600, 180, 90,  self.sendPlayerTank, image_name = 'Tank', qtd = self.playerTankQnt)
		self.button3 = Button(510, 600, 200, 90,  self.sendWhiteFlag, image_name = 'White Flag', qtd = 1)
		self.buttons.append(self.button1)
		self.buttons.append(self.button2)
		self.buttons.append(self.button3)


	def sendWhiteFlag(self):
		if not self.spawnedWhiteFlag and self.commandTicker < 0:
			white_flag = WhiteFlag(self.mapLane)
			self.player.append(white_flag)
			self.spawnedWhiteFlag = True
			self.white_flag = white_flag
			self.commandTicker = 10
			self.button3.MinusQtd()

	def sendPlayerTower(self):
		if self.playerTowerQnt > 0 and self.commandTicker < 0:
			player_tower = PlayerTower(self.mapLane)
			self.player.append(player_tower)
			self.playerTowerQnt -= 1
			self.commandTicker = 10
			self.button1.MinusQtd()

	def sendPlayerTank(self):
		if self.playerTankQnt > 0 and self.commandTicker < 0:
			player_tank = PlayerTank(self.mapLane)
			self.player.append(player_tank)
			self.playerTankQnt -= 1
			self.commandTicker = 10
			self.button2.MinusQtd()

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
		self.commandTicker -= 1

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
				self.hasLost = True
			if self.white_flag.Got_End():
				#game win
				print("Win")
				self.hasWon = True
		
	def Draw(self, screen):
		self.mapLane.DrawBg(screen)
		for enemy in self.enemies:
			enemy.Draw(screen)
		for unit in self.player:
			unit.Draw(screen)
		for button in self.buttons:
			button.Update(screen)
