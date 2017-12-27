import pygame
import math
import random
from pygame.locals import*

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (10, 255, 10)
BLUE = (10, 10, 255)
RED = (255, 10, 10)
GREY = (100, 100, 100)

Prompt = input("Pick a color to draw with: \n a) Blue \n b) Green \n c) Red \n d) Confuse Me \n")

if Prompt == "a":
    COLOR1 = BLUE
    COLOR2 = BLUE
    COLOR3 = BLUE 
elif Prompt == "b":
    COLOR1 = GREEN
    COLOR2 = GREEN
    COLOR3 = GREEN
elif Prompt == "c":
    COLOR1 = RED
    COLOR2 = RED
    COLOR3 = RED
elif Prompt == "d":
    COLOR1 = GREEN
    COLOR2 = RED
    COLOR3 = BLUE

pygame.init()

BLACK =  (0, 0, 0)
size = (700, 500)
screen = pygame.display.set_mode(size)
#pygame.mixer.music.load("Music.mp3")
#pygame.mixer.music.play(-1,0.0)
#pygame.mixer.music.set_volume(1.0)

# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.SysFont(None, 30)

# render text
instructions = myfont.render("Instructions: move with arrow keys, press space bar to clear.", 1, ( 200,200,200))

size = (700, 500)

screen = pygame.display.set_mode(size)

done = False

clock = pygame.time.Clock()

screen.fill(BLACK)
pygame.draw.rect(screen, GREY, (50, 50, 600, 400))
screen.blit(instructions, (50,465))

label = pygame.image.load("EtchLabel.png").convert_alpha()
label = pygame.transform.scale(label, (600, 600))
    
distperkey = 2

locationx = 100
locationy = 100

speedx = 0
speedy = 0

recty = 400
rectx = 550

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speedx -= distperkey
            elif event.key == pygame.K_RIGHT:
                speedx += distperkey
            elif event.key == pygame.K_UP:
                speedy -= distperkey
            elif event.key == pygame.K_DOWN:
                speedy += distperkey
            elif event.key == pygame.K_SPACE:
                pygame.draw.rect(screen, GREY, (50, 50, 600, 400))


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                speedx = 0
            elif event.key == pygame.K_RIGHT:
                speedx = 0
            elif event.key == pygame.K_UP:
                speedy = 0 
            elif event.key == pygame.K_DOWN:
                speedy = 0

        #Shapes, Clock, and Colors:

    locationx += speedx
    locationy += speedy

    if locationx < 60:
        locationx = 60
    elif locationx > 640:
        locationx = 640
    if locationy < 60:
        locationy = 60
    elif locationy > 440:
        locationy = 440
    
    pygame.draw.circle(screen, COLOR1, (locationx, locationy), 8)
    pygame.draw.circle(screen, COLOR2, (locationx, locationy), 7)
    pygame.draw.circle(screen, COLOR3, (locationx, locationy), 6)

    screen.blit(label, (50,0))
    
    pygame.display.flip()
    
    clock.tick(60)


if done:
    pygame.quit()



