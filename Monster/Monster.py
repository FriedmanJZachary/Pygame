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
seconds = 30
offset = 0
hitspecial = False


pygame.init()

BLACK =  (0, 0, 0)

#pygame.mixer.music.load("Music.mp3")
#pygame.mixer.music.play(-1,0.0)
#pygame.mixer.music.set_volume(1.0)

# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.SysFont(None, 100)
myotherfont = pygame.font.SysFont(None, 75)

# render text
#points = myfont.render(counter, 1, TEXTCOLOR)


#pointimg = pygame.image.load("Points.png").convert_alpha()
#pointimg = pygame.transform.scale(pointimg, (50, 50)

size = (1200, 700)

screen = pygame.display.set_mode(size)

done = False

clock = pygame.time.Clock()

pygame.draw.rect(screen, GREY, (50, 50, 600, 400))

pointimg = pygame.image.load("Points.png").convert_alpha()
pointimg =  pygame.transform.scale(pointimg, (140, 100))

timeimg = pygame.image.load("Time.png").convert_alpha()
timeimg =  pygame.transform.scale(timeimg, (140, 100))


#label = pygame.image.load("EtchLabel.png").convert_alpha()
#label = pygame.transform.scale(label, (600, 600))
    
distperkey = 8

locationx = 100
locationy = 100

speedx = 0
speedy = 0

recty = 400
rectx = 550


class Character(object):
        def __init__(self, image):
                self.image = image
                self.body = pygame.transform.scale(image, (120, 120))
                self.distperkey = 5
                self.locationx = 0
                self.locationy = 0
                self.speedx = 0
                self.speedy = 0

monster = Character(pygame.image.load("Monster.png").convert_alpha())

class Obstacle(object):
        def __init__(self, image):
                self.image = image
                self.body = pygame.transform.scale(image, (120, 120))
                self.locationy = random.randint(0,600)
                self.locationx = random.randint(150,1100)
                self.hit = False
                self.exists = False 
        def hitter(self, monster):
                global count
                if (abs(monster.locationx - self.locationx) < 100 and abs(monster.locationy - self.locationy) < 100):
                        self.hit = True
                if self.hit == True:
                        #Coin sound
                        self.locationy = random.randint(0,600)
                        self.locationx = random.randint(150,1100)
                        self.hit = False
                        self.exists = False
                        count += 1

class Pointloss(Obstacle):
                def __init__(self, image):
                        Obstacle.__init__(self, image)
                        self.exists = False
                def hitter(self, monster):
                        global count
                        if (abs(monster.locationx - self.locationx) < 75 and abs(monster.locationy - self.locationy) < 75):
                                self.hit = True
                        if self.hit == True:
                                #Coin sound
                                self.locationy = random.randint(0,600)
                                self.locationx = random.randint(150,1100)
                                self.hit = False
                                self.exists = False
                                count -= 1
                                
class Hourglass(Obstacle):
                def __init__(self, image):
                        Obstacle.__init__(self, image)
                        self.exists = False
                def hitter(self, monster):
                        global offset
                        if (abs(monster.locationx - self.locationx) < 100 and abs(monster.locationy - self.locationy) < 100):
                                self.hit = True
                        if self.hit == True:
                                #Coin sound
                                self.locationy = random.randint(0,600)
                                self.locationx = random.randint(150,1100)
                                offset += 900
                                self.hit = False
                                self.exists = False 
                                
class Skull(Obstacle):
                def __init__(self, image):
                        Obstacle.__init__(self, image)
                        self.exists = False
                def hitter(self, monster):
                        global offset
                        if (abs(monster.locationx - self.locationx) < 75 and abs(monster.locationy - self.locationy) < 75):
                                self.hit = True
                        if self.hit == True:
                                #Coin sound
                                self.locationy = random.randint(0,600)
                                self.locationx = random.randint(150,1100)
                                offset -= 30000
                                self.hit = False
                                self.exists = False
                                


class Bluecoin(Obstacle):
                def __init__(self, image):
                        Obstacle.__init__(self, image)
                        self.exists = False
                def hitter(self, monster):
                        global count
                        global hitspecial
                        if (abs(monster.locationx - self.locationx) < 75 and abs(monster.locationy - self.locationy) < 75):
                                self.hit = True
                        if self.hit == True:
                                #Coin sound
                                self.locationy = random.randint(0,600)
                                self.locationx = random.randint(150,1100)
                                self.hit = False
                                self.exists = False
                                count += 5

skull = Skull(pygame.image.load("Skull.png").convert_alpha())               
bluecoin =Bluecoin(pygame.image.load("Coin2.png").convert_alpha())
hourglass1 = Hourglass(pygame.image.load("Hourglass.png").convert_alpha())
hourglass2 = Hourglass(pygame.image.load("Hourglass.png").convert_alpha())                       
coin1 = Obstacle(pygame.image.load("Coin.png").convert_alpha())
coin2 = Obstacle(pygame.image.load("Coin.png").convert_alpha())
coin3 = Obstacle(pygame.image.load("Coin.png").convert_alpha())
coin4 = Obstacle(pygame.image.load("Coin.png").convert_alpha())
coin5 = Obstacle(pygame.image.load("Coin.png").convert_alpha())
coin6 = Obstacle(pygame.image.load("Coin.png").convert_alpha())
coin7 = Obstacle(pygame.image.load("Coin.png").convert_alpha())
coin8 = Obstacle(pygame.image.load("Coin.png").convert_alpha())
bomb1 = Pointloss(pygame.image.load("Bomb.png").convert_alpha())
bomb2 = Pointloss(pygame.image.load("Bomb.png").convert_alpha())
bomb3 = Pointloss(pygame.image.load("Bomb.png").convert_alpha())
bomb4 = Pointloss(pygame.image.load("Bomb.png").convert_alpha())


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

        monster.locationx += speedx
        monster.locationy += speedy

        if monster.locationx < 150:
                monster.locationx = 150
        elif monster.locationx > 1100:
                monster.locationx = 1100
        if monster.locationy < 10:
                monster.locationy = 10
        elif monster.locationy > 600:
                monster.locationy = 600

        screen.fill(WHITE)

        stuff = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, hourglass1, hourglass2, bomb1, bomb2, bomb3, bomb4]
        special = [bluecoin, skull]
        
        screen.blit(monster.body, (monster.locationx, monster.locationy))
        pygame.draw.rect(screen, GREY, (0, 0, 150, 800))
        #screen.blit(points, (20,50))
        #screen.blit(pointimg, (20,50))

 
        for thing in stuff:
                if (random.randint(1, 100) == 1):
                        thing.exists = True
                if (thing.exists == True):
                        screen.blit(thing.body, (thing.locationx, thing.locationy))
                        thing.hitter(monster)
                                       
                
        for thing in special:
                if (random.randint(1, 1000) == 1):
                        thing.exists = True
                if (thing.exists == True):
                        screen.blit(thing.body, (thing.locationx, thing.locationy))
                        thing.hitter(monster)
                                               
                        
        screen.blit(pointimg, (5,5))
        score = myfont.render(str(count), 1, ( 200,200,200))
        screen.blit(score, (10, 35))

        #Gets countdown:
        time1 = pygame.time.get_ticks() - offset
        time2 =30000 - time1 
        time3 = int(time2/100)
        timetext = myfont.render(str((time3/10)), 1, ( 200,200,200))
        screen.blit(timeimg, (5,125))
                

        if((time3 / 10 ) >= 0):
                screen.blit(timetext, (10, 155))
        else:
                losetext = myotherfont.render("Over", 1, ( 255,30,30))
                screen.blit(losetext, (10, 175))
                losescreen = pygame.image.load("Lose5.png").convert_alpha()
                losescreen = pygame.transform.scale(losescreen, (1050, 700))
                screen.blit(losescreen, (150, 0))
                monster.locationx = 0
                monster.locationy = 0
                for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                        offset = pygame.time.get_ticks()
                                        count = 0
                                        speedx = 0
                                        speedy = 0


        pygame.display.flip()
        clock.tick(60)

if done:
    pygame.quit()



