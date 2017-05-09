#! /usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit
from random import randrange

white = (255, 255, 255)
black = (0, 0, 0)


class Button:
	def __init__(self, x, y, w, h, ac, ic, image_name, action = None):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.ac = white
		self.ic = black
		self.image = image_name
		self.action = action
		self.color = ic

	def Update(self):
		CheckMouse()

	def CheckMouse(self):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		if self.x + self.w > mouse[0] > self.x and self.y + self.w > mouse[1] > y:

			if click[0] == 1 and actcion != None:
				action()