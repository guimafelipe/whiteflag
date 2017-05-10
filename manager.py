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
from gamecontroller import *
from win import *
from lose import *

class Manager:

	def __init__(self, screen):
		self.screen = screen
		self.mapArray = []
		mapa = Map1()
		self.mapArray.append(mapa)
		self.endedLvl = True
		self.onMenu = True
		self.currLvl = 0
		self.win = Win(self)
		self.lose = Lose(self)

	def CreateLvl(self, index):
		self.gcontroller = GameController(self.mapArray[index])
		self.currLvl = index
		self.endedLvl = False

	def Update(self, screen):
		if self.onMenu:
			self.MenuScene()
			pressed_keys = pygame.key.get_pressed()
			if pressed_keys[K_SPACE]:
				self.CreateLvl(self.currLvl)
				self.onMenu = False
		elif self.gcontroller and not self.endedLvl:
			self.gcontroller.Update(screen)
			self.gcontroller.Draw(screen)
			if(self.gcontroller.hasWon):
				self.endedLvl = True
				self.endAction = self.WinScene
			elif(self.gcontroller.hasLost):
				self.endedLvl = True
				self.endAction = self.LoseScene
		else:
			self.endAction()

	def MenuScene(self):
		menu_filename = "intro.jpg"
		self.onMenu = True
		self.currLvl = 0
		self.menu_scene = pygame.image.load(menu_filename).convert()
		self.screen.blit(self.menu_scene, (0, 0))

	def WinScene(self):
		self.win.Execute(self.screen, self.gcontroller)

	def LoseScene(self):
		self.lose.Execute(self.screen, self.gcontroller)

