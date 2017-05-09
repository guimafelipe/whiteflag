#! /usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit
from random import randrange

pygame.init()
green = (4,200,4)
blue = (0,0,250)
screen = pygame.display.set_mode((956, 560), 0, 32)

class WayPoint:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def getX(self):
		return self.x

	def getY(self):
		return self.y

class WayPointsList:
	def __init__(self):
		self.wayPoints = []

	def add_wayPoint(self, x, y):
		self.wayPoints.append(WayPoint(x,y)) 

	def __len__(self):
		return len(self.wayPoints)

	def get_wayPoint(self, i):
		return [self.wayPoints[i].getX(), self.wayPoints[i].getY()]

class Player:
	position = {
		'x':0,
		'y':0
	}

	velocity = {
		'x':0,
		'y':0
	}

	speed = 5

	def move(self):
		self.position['x'] += self.velocity['x']*self.speed
		self.position['y'] += self.velocity['y']*self.speed

def dist(player, target):
	return ((player.position['x']-target.x)**2 + (player.position['y'] - target.y)**2)**0.5


class LevelMaster:
	i = 0
	def Update(self, player):
		norma = dist(player, lane.wayPoints[self.i])
		player.velocity['x'] = (lane.wayPoints[self.i].x - player.position['x'])/norma
		player.velocity['y'] = (lane.wayPoints[self.i].y - player.position['y'])/norma
		if(dist(player, lane.wayPoints[self.i]) > 20):
			player.move()
		elif self.i < len(lane.wayPoints) - 1:
			self.i = self.i + 1
		pygame.draw.circle(screen,blue,[round(player.position['x']),round(player.position['y'])],20,0)

lane = WayPointsList()
lane.add_wayPoint(50, 250)
lane.add_wayPoint(250, 350)
lane.add_wayPoint(450, 150)
lane.add_wayPoint(52, 20)
lane.add_wayPoint(50, 200)
lane.add_wayPoint(450, 211)
lane.add_wayPoint(0, 0)

charr = Player()

clock = pygame.time.Clock()
levelmaster = LevelMaster()

print("Chegou aqui")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
	
    screen.fill(green)
    levelmaster.Update(charr)
    #printThings()
    pygame.display.update()
    time_passed = clock.tick(30)
    # print("{0}, {1}", charr.position['x'], charr.position['y'])

