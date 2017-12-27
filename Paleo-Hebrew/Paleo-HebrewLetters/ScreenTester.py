import pygame
import math
import random
from pygame.locals import*

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (10, 255, 10)
BLUE = (10, 10, 150)
RED = (255, 10, 10)
GREY = (100, 100, 100)

counter = 0 

pygame.init()

BLACK =  (0, 0, 0)
size = (700, 500)
screen = pygame.display.set_mode(size)

# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.SysFont(None, 30)

# render text
#label = myfont.render("Instructions: move with arrow keys, press space bar to clear.", 1, ( 200,200,200))

size = (1150, 750)

screen = pygame.display.set_mode(size)

done = False

clock = pygame.time.Clock()

screen.fill(BLUE)
pygame.draw.rect(screen, WHITE, (50, 50, 1050, 650))
#screen.blit(label, (50,465))

#label = pygame.image.load("EtchLabel.png").convert_alpha()
#label = pygame.transform.scale(label, (600, 600))

#def locationx(counter):
    
    
   # pygame.draw.circle(screen, COLOR1, (locationx, locationy), 8)
#    pygame.draw.circle(screen, COLOR2, (locationx, locationy), 7)
#    pygame.draw.circle(screen, COLOR3, (locationx, locationy), 6)

 #   screen.blit(label, (50,0))
    
pygame.display.flip()
    
clock.tick(60)


if done:
    pygame.quit()



