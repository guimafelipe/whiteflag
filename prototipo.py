import pygame, sys
from pygame.locals import *
from sys import exit
import time
pygame.init()

#Display's size
sizex = 800
sizey = 600

gameDisplay = pygame.display.set_mode((sizex,sizey)) #creates a display
pygame.display.set_caption('Torre e nave')

#Colors
green = (4,200,4)
red = (200,0,0)
black = (0,0,0)
blue = (0,0,250)

#Ship and tower's sizes
ship_sizex = 15
ship_sizey = 15
tow_sizex = 50
tow_sizey = 50
bul_rad = 5

#Ship, tower and bullet's initial coordinates
ship_coord_x = 100
ship_coord_y = 100
x_change = 0
y_change = 0
tow_coord_x = sizex//2
tow_coord_y = sizey//2
bullet_ini_coord_x = tow_coord_x + tow_sizex//2
bullet_ini_coord_y = tow_coord_y + tow_sizey//2
bul_coord_x = bullet_ini_coord_x
bul_coord_y = bullet_ini_coord_y
bul_changex = 0
bul_changey = 0

#Time variable
tim = 50

#Ship's step size
sstep_x = 10
sstep_y = 10

#Bullet's step size
bstep = 10

font = pygame.font.SysFont(None, 30)

def message_to_screen (msg,color):
    screen_text = font.render(msg,True,color)
    gameDisplay.blit(screen_text,[sizex/2,0])
    
def Intro():
    gameDisplay.fill(green)
    message_to_screen("Press Space to start",blue)
    pygame.display.update()
    clock.tick(tim//2)
    

clock = pygame.time.Clock()

gameExit = False 
intr = True

while intr:
    Intro()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                intr = False
    

while not gameExit:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -sstep_x
            if event.key == pygame.K_RIGHT:
                x_change = sstep_x
            if event.key == pygame.K_UP:
                y_change = -sstep_y
            if event.key == pygame.K_DOWN:
                y_change = sstep_y
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0
    
    if bul_coord_x == bullet_ini_coord_x and bul_coord_y == bullet_ini_coord_y:
        bul_changex = ship_coord_x + ship_sizex//2 - bul_coord_x
        bul_changey = ship_coord_y + ship_sizey//2 - bul_coord_y
        a = bul_changex/(bul_changex**2 + bul_changey**2)**0.5
        b = bul_changey/(bul_changex**2 + bul_changey**2)**0.5
        bul_changex = int(bstep*a)
        bul_changey = int(bstep*b)
        bul_coord_x +=bul_changex
        bul_coord_y +=bul_changey
    
    else:
        bul_coord_x += bul_changex
        bul_coord_y += bul_changey
    
    #Boundary conditions
    
    if ship_coord_x+x_change > 0 and ship_coord_x + x_change < sizex - ship_sizex:
        ship_coord_x += x_change
    if ship_coord_y + y_change > 0 and ship_coord_y + y_change < sizey - ship_sizey:
        ship_coord_y += y_change
    if bul_coord_x < 0 or bul_coord_y < 0 or bul_coord_x > sizex or bul_coord_y > sizey:
        bul_coord_x = bullet_ini_coord_x
        bul_coord_y = bullet_ini_coord_y
        
    
    gameDisplay.fill(green)
    pygame.draw.rect(gameDisplay,red,[tow_coord_x,tow_coord_y,tow_sizex,tow_sizey])
    pygame.draw.rect(gameDisplay,black,[ship_coord_x,ship_coord_y,ship_sizex,ship_sizey])
    pygame.draw.circle(gameDisplay,blue,[bul_coord_x,bul_coord_y],bul_rad,0)
    
    #Conditions to lose
    if ship_coord_x > tow_coord_x - ship_sizex and ship_coord_x < tow_coord_x + tow_sizex and ship_coord_y > tow_coord_y - ship_sizey and ship_coord_y < tow_coord_y + tow_sizey :
        gameExit = True
    if bul_coord_x > ship_coord_x - bul_rad and bul_coord_x < ship_coord_x + ship_sizex + bul_rad and bul_coord_y > ship_coord_y - bul_rad and bul_coord_y < ship_coord_y + ship_sizey + bul_rad:
        gameExit = True
    pygame.display.update() 
    clock.tick(tim)

message_to_screen("You lose kkkk",black)
pygame.display.update()
time.sleep(1.5)

pygame.quit()
quit()