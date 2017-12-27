import pygame
import math
import time
import random
from pygame.locals import*

count = 0
sadtimer = 60
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

class Pin(object):
        def __init__(self):
                self.image = pygame.image.load("Pin3.png").convert_alpha()
                self.body = pygame.transform.rotate(self.image, random.randint(0, 180))
                self.locationx = 0
                self.locationy = 0
                self.active = False


current = 0
Pin1 = Pin()
Pin2 = Pin()
Pin3 = Pin()
Pin4 = Pin()
Pin5 = Pin()
Pinlist =  [Pin1, Pin2, Pin3, Pin4, Pin5]
 
while not done:
        sadtimer -= 1
        if sadtimer < 0:
                sadtimer = 0
                screen.blit(Happy, (0,0))
                        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                                screen.blit(Happy, (0, 0))
                                for pin in Pinlist:
                                        pin.active = False
                elif event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        NEWPos = list(pos)
                        NEWPos[0] -=  82
                        NEWPos[1] -=  82
                        Pinlist[current].locationx = NEWPos[0]
                        Pinlist[current].locationy = NEWPos[1]
                        Pinlist[current].active = True
                        screen.blit(Sad, (0,0))
                        sadtimer = 60
                        current += 1
                        current %= 5
                        
        for pin in Pinlist:
                if pin.active == True:
                        screen.blit(pin.body, (pin.locationx, pin.locationy))
                                        
        pygame.display.flip()
        clock.tick(60)

if done:
    pygame.quit()



