import pygame
import math
import time
import random
from pygame.locals import*

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (10, 255, 10)
BLUE = (10, 10, 255)
RED = (255, 10, 10)
GREY = (150, 150, 150)
TEXTCOLOR = (90, 90, 90)

count = 0
seconds = 60
offset = 0
pincount = 0


pygame.init()
size = (360, 500)
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()


Happy = (pygame.image.load("Happy.png").convert_alpha())
Sad = (pygame.image.load("Sad.png").convert_alpha())


screen.blit(Happy, (0, 0))


####
####class Pin(object):
####        def __init__(self, image):
####                self.image = image
####                self.body = pygame.transform.scale(image, (120, 120))
####                self.locationx = 0
####                self.locationy = 0



                        
#Make a pin blit to every click location
#If Pin was recently clicked, make/keep face sad and play sound (boolean + timer)
while not done:
        Pin = (pygame.image.load("Pin3.png").convert_alpha())
        rand = random.randint(0, 360)
        Pin = pygame.transform.rotate(Pin, rand)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                        print("event1 occured")
                elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                                screen.blit(Happy, (0, 0))
                elif event.type == pygame.MOUSEBUTTONUP:
                        print("event2 occured")
                        pos = pygame.mouse.get_pos()
                        print("Pos: ")
                        print(pos)
                        NEWPos = list(pos)
                        print(NEWPos[1])
                        NEWPos[0] -=  72
                        NEWPos[1] -=  72
                        print("NEW Pos: ")
                        print(NEWPos)
                        screen.blit(Pin, (NEWPos))
                        

                        
                        
                      


        pygame.display.flip()
        clock.tick(60)

if done:
    pygame.quit()



