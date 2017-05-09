import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Base Shooting')

pygame.display.update()

block_size = 10
FPS = 60

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 25)

def base(randBaseX,randBaseY,block_size):
    pygame.draw.rect(gameDisplay, red, [randBaseX,randBaseY,block_size,block_size])
    
def player(lead_x,lead_y,block_size):
    pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,block_size,block_size])
    
def bullet(bullet_x,bullet_y,block_size):
    pygame.draw.rect(gameDisplay, black, [bullet_x,bullet_y,block_size/2,block_size/2])
    
def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])
    pygame.display.update()

def gameLoop():
    gameOver = False
    gameExit = False
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0
    min_distance = 100
    
    randBaseX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
    randBaseY = round(random.randrange(0, display_height-block_size)/10.0)*10.0
    distance = ((lead_x-randBaseX)**2 + (lead_y-randBaseY)**2)**0.5
    while distance < min_distance:
        randBaseX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
        randBaseY = round(random.randrange(0, display_height-block_size)/10.0)*10.0
        distance = ((lead_x-randBaseX)**2 + (lead_y-randBaseY)**2)**0.5
    
    bullet_x = randBaseX
    bullet_y = randBaseY
    speed_bullet = block_size/2
    bullet_x_change = speed_bullet*(lead_x-randBaseX)/(((lead_x-randBaseX)**2 + (lead_y-randBaseY)**2)**0.5)
    bullet_y_change = speed_bullet*(lead_y-randBaseY)/(((lead_x-randBaseX)**2 + (lead_y-randBaseY)**2)**0.5)
    
    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit", red)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
                        
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                gameExit = True
                message_to_screen("Bye!", red)
                time.sleep(2)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size 
                if event.key == pygame.K_UP:
                    lead_y_change = -block_size
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    lead_x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    lead_y_change = 0
        
        if lead_x >= display_width-block_size and lead_x_change>0:
            lead_x_change = 0
        if lead_x <= 0 and lead_x_change<0:
            lead_x_change = 0
        if lead_y >= display_height-block_size and lead_y_change>0:
            lead_y_change = 0
        if lead_y <= 0 and lead_y_change<0:
            lead_y_change = 0


        lead_x += lead_x_change
        lead_y += lead_y_change         
        bullet_x += bullet_x_change
        bullet_y += bullet_y_change
        
        gameDisplay.fill(white)
        
        base(randBaseX,randBaseY,block_size)
        player(lead_x,lead_y,block_size)
        bullet(bullet_x,bullet_y,block_size)
        
        distance_player_bullet = ((lead_x-bullet_x)**2 + (lead_y-bullet_y)**2)**0.5
        if distance_player_bullet < 5:
            gameOver = True
        
        pygame.display.update()

        clock.tick(FPS)
    pygame.quit()
    quit()
    
gameLoop()