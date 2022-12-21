from pygame.locals import *
mapped = (1,2,3,4,5)
print(mapped[1] + 1)
import pygame 

pygame.init()
surface = pygame.display.set_mode((640,480))
running = True 
snake = pygame.image.load('snake.png')
x = 20
y = 15
while running:

    surface.fill((0,0,0))
    surface.blit(snake,(x,y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        keys = pygame.key.get_pressed()
    

        keys[K_SPACE ]
    
    
    x+= 1 
    y+= 0

    pygame.display.update()