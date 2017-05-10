#! /usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit
from random import randrange

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0,238,255)

class Button:
	def __init__(self, x, y, w, h, action = None, ac = white, ic = black, image_name = "", qtd=0):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.ac = white
		self.ic = black
		self.qtd = qtd
		self.image_name = image_name
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

		size_font = 50
		font = pygame.font.SysFont(None,size_font)
		screen_text = font.render(self.image_name, True, blue)
		gameDisplay.blit(screen_text,[self.x-size_font*len(self.image_name)/6, self.y-size_font/1.5])
		screen_qtd = font.render(str(self.qtd), True, blue)
		gameDisplay.blit(screen_qtd,[self.x, self.y])

	def CheckMouse(self):
		mouse = pygame.mouse.get_pos()
		
		if self.x + self.w/2 > mouse[0] > self.x - self.w/2 and self.y + self.h/2 > mouse[1] > self.y - self.h/2:
			return True
		return False

	def MinusQtd(self):
		self.qtd -= 1