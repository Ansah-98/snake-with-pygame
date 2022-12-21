import sys
import random as rd 
import os
import pygame 
from pygame.locals import *

class Position:
    def __init__(self,x, y):
        self.x = x       
        self.y = y
    def ret(self):
        return (self.x , self.y)

class Snake:
    def __init__(self) :
        self.frame = 0
        self.length = []
        self.direction = 0
        self.position = Position(20*16,15*16)
        self.length.append(self.position)
        self.start = False 
        self.eat = False
          
class Berry:
    x = rd.randint(1,38)
    y = rd.randint(1,28)
    def __init__(self):
        self.position = Position(self.x , self.y)
        self.is_touched  = False

class Wall:
    def __init__(self,x , y):
        self.x = x
        self.y = y
    
    def wall_object(self):
        f = open('map.txt','w')
        valueX = int(self.x/16)
        valueY = int(self.y/16) 
        for i in range( valueY):
            if i == 0 or i == self.y/16-1:
                f.write('1'*valueX +'\n')
            else :
                f.write('1' + '0'*(valueX-2) + '1' + '\n')
        f.close()

        f = open('map.txt')
        content = f.readlines()
        f.close()
        return content

        
surface = pygame.display.set_mode((640,480))

def direct(snakedata,key):
        snakedata.start = True
        if key[K_RIGHT] and snakedata.direction != 1:
            snakedata.direction = 0
            return snakedata.direction
        elif  key[K_LEFT] and snakedata.direction != 0:
            snakedata.directon = 1
            return snakedata.direction
        elif key[K_DOWN] and snakedata.direction !=2 :
            snakedata.direction = 3
            return snakedata.direction 
        elif  key[K_UP] and snakedata.direction !=3 :
            snakedata.direction = 2  
            return snakedata.direction
def loadImages():
    loading = pygame.image.load('player64.png')
    wall  = pygame.image.load('wall.png')
    snake = pygame.image.load('snake.png')
    return {'loading':loading,'wall':wall, 'snake':snake}

def show_splash(surface,img):
    global notplaying
    keys = pygame.key.get_pressed()
    if keys[K_SPACE]:
        notplaying = False
    return  surface.blit(img,(320,140))
def eat(snakedata,berry):

    s_position = snakedata.length[0]
    
    b_position = berry.position
    lenInx =len(snakedata.length)
    last = snakedata.length[lenInx-1]
    x = last.ret()[0]
    y = last.ret()

    if s_position == b_position:
        snakedata.eat = True
        snakedata.length.append(Position(x,y))
        return True
    
def drawWall(wall,surface):
    z = 0
    for i in wall.wall_object():
        c = 0 
        for b in i:               
            if b == '1':
                surface.blit(imaging['wall'],(c*16, z * 16))
            
            c += 1 
        z += 1
def drawSnake(snakedata,surface):
    img = loadImages()['snake']

    for i in snakedata.length:
        x,y = i.x,i.y
        if snakedata.eat == False and snakedata.length[0] == i:
            snakedata.frame =0
            surface.blit(img, (x,y) , (snakedata.direction * 16 ,0,16,16 ))
        elif snakedata.eat == True and snakedata.length[0] ==i:
            snakedata.frame = 1
            snakedata.eat =False
            return surface.blit(img, (x,y), ((snakedata.direction + 1)*16,0,16,16))
        else:
            return surface.blit(img, (x,y), (8*16,0,16,16))
def move(snakedata):
        if snakedata.start:
            if snakedata.direction == 0:
                x = 0
                for i in (snakedata.length):
                    b = i.x + 1
                    
                    new_pos =(b , i.y) 
                    snakedata.length[x] = Position(new_pos[0],new_pos[1])
                    x+=1
            elif snakedata.direction == 1:
                x = 0
                for i in snakedata.length:
                    b = i.x - 1
                    
                    new_pos =(b ,i.y) 
                    snakedata.length[x] = Position(new_pos[0],new_pos[1])
                    x += 1
            elif snakedata.direction == 2:
                x=0
                for i in (snakedata.length):
                    new_pos =(i.x,i.y - 1 )
                    snakedata.length[x] = Position(new_pos[0],new_pos[1])
                    x+=1 
            else:
                x = 0
                for i in (snakedata.length):
                    new_pos = (i.x, i.y + 1 )
                    snakedata.length[x] = Position(new_pos[0],new_pos[1])
                    x+=1
def crashedWall(snakedata,wall):
    head  = (snakedata.length[0].x, snakedata.length[0].y)
    row  = 0
    for i in wall:
        print(head)
        col = 0
        for b in i:
            if b =='1'  :
                if head[0]/16 == col and head[1]/16 == row:
                    return True                
            col += 1
        row += 1  
    return False
def crashed_body(snakedata):
    head  = snakedata.length[0]
    for i in snakedata.length:
        if head == i:
            return False
wall = Wall(640,480)
pygame.init()
running  = True 
notplaying =    True
snake = Snake()
berry  = Berry()
imaging = loadImages()

while running:
    for event in pygame.event.get():

        if notplaying:
            show_splash(surface,imaging['loading'])
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        surface.fill((0,0,0))
        drawWall( wall , surface)
        key = pygame.key.get_pressed()
        direct(snake , key)
        eats = eat(snake,berry)
        if eats:
            berry.position = Position(rd.randint(1,38), rd.randint(1,28))
    if crashedWall(snake, wall.wall_object()):
            show_splash(surface,imaging['loading'])
    snake.start = True
    move(snake) 
    drawSnake(snake,surface)
    pygame.display.update()