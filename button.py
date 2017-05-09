#! /usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit
from random import randrange

white = (255, 255, 255)
black = (0, 0, 0)


class Button:
	def __init__(self, x, y, w, h, action = None, ac = white, ic = black, image_name = ""):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.ac = white
		self.ic = black
		#self.image = image_name
		self.action = action
		self.color = ic
	
	def Update(self, gameDisplay):
		if self.CheckMouse():
			pygame.draw.rect(gameDisplay, self.ac, [self.x - self.w/2, self.y-self.h/2,self.w,self.h])
			click = pygame.mouse.get_pressed()
			if click[0] == 1 and self.action != None:
				self.action()
		else:
			pygame.draw.rect(gameDisplay, self.ic, [self.x - self.w/2, self.y-self.h/2,self.w,self.h])

	def CheckMouse(self):
		mouse = pygame.mouse.get_pos()
		
		if self.x + self.w/2 > mouse[0] > self.x - self.w/2 and self.y + self.h/2 > mouse[1] > self.y - self.h/2:
			return True
		return False
