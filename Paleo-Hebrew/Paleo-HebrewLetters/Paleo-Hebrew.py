import pygame
import math
import random
from pygame.locals import*

BLACK = (0, 0, 0)
WHITE = (250, 250, 250)
GREEN = (10, 255, 10)
BLUE = (10, 10, 150)
RED = (255, 10, 10)
GREY = (100, 100, 100)
BRICK = (130, 70, 10)

i = 1

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

screen.fill(BRICK)
pygame.draw.rect(screen, BLACK, (45, 45, 1060, 660))
pygame.draw.rect(screen, WHITE, (50, 50, 1050, 650))


#Load and scale all letters
a = pygame.image.load("Aleph.png").convert_alpha()
a = pygame.transform.scale(a, (50, 50))

b = pygame.image.load("Bet.png").convert_alpha()
b = pygame.transform.scale(b, (50, 50))

g = pygame.image.load("Gimmel.png").convert_alpha()
g = pygame.transform.scale(g, (50, 50))

d = pygame.image.load("Daled.png").convert_alpha()
d = pygame.transform.scale(d, (50, 50))

h = pygame.image.load("Hey.png").convert_alpha()
h = pygame.transform.scale(h, (50, 50))

w = pygame.image.load("Vav.png").convert_alpha()
w = pygame.transform.scale(w, (50, 50))

z = pygame.image.load("Zayin.png").convert_alpha()
z = pygame.transform.scale(z, (50, 50))

j = pygame.image.load("Chet.png").convert_alpha()
j = pygame.transform.scale(j, (50, 50))

f = pygame.image.load("Tet.png").convert_alpha()
f = pygame.transform.scale(f, (50, 50))

y = pygame.image.load("Yud.png").convert_alpha()
y = pygame.transform.scale(y, (50, 50))

k = pygame.image.load("Kaf.png").convert_alpha()
k = pygame.transform.scale(k, (50, 50))

l = pygame.image.load("Lamed.png").convert_alpha()
l = pygame.transform.scale(l, (50, 50))

m = pygame.image.load("Mem.png").convert_alpha()
m = pygame.transform.scale(m, (50, 50))

n = pygame.image.load("Nun.png").convert_alpha()
n = pygame.transform.scale(n, (50, 50))

s = pygame.image.load("Samech.png").convert_alpha()
s = pygame.transform.scale(s, (50, 50))

u = pygame.image.load("Ayin.png").convert_alpha()
u = pygame.transform.scale(u, (50, 50))

p = pygame.image.load("Pey.png").convert_alpha()
p = pygame.transform.scale(p, (50, 50))

x = pygame.image.load("Tzadi.png").convert_alpha()
x = pygame.transform.scale(x, (50, 50))

q = pygame.image.load("Kuf.png").convert_alpha()
q = pygame.transform.scale(q, (50, 50))

r = pygame.image.load("Raish.png").convert_alpha()
r = pygame.transform.scale(r, (50, 50))

c = pygame.image.load("Shin.png").convert_alpha()
c = pygame.transform.scale(c, (50, 50))

t = pygame.image.load("Taf.png").convert_alpha()
t = pygame.transform.scale(t, (50, 50))

def locationy(counter):
    spoty = 50
    while (counter > 21):
        counter -= 21 
        spoty += 50
    return spoty

def locationx(counter):
    spoty = 50
    spotx = 0
    while (counter > 21):
        counter -= 21
        spoty += 50
    while (counter > 0):
        counter -= 1
        spotx += 50
    return spotx
        
    
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if i < 273:
                    screen.blit(a, (locationx(i), locationy(i)))
                    i += 1
            elif event.key == pygame.K_b:
                if i < 273:
                    screen.blit(b, (locationx(i), locationy(i)))
                    i += 1
            elif event.key == pygame.K_g:
                if i < 273:
                    screen.blit(g, (locationx(i), locationy(i)))
                    i += 1
            elif event.key == pygame.K_d:
                if i < 273:
                    screen.blit(d, (locationx(i), locationy(i)))
                    i += 1
            elif event.key == pygame.K_h:
                if i < 273:
                    screen.blit(h, (locationx(i), locationy(i)))
                    i += 1
            elif event.key == pygame.K_w:
                if i < 273:
                    screen.blit(w, (locationx(i), locationy(i)))
                    i += 1
            elif event.key == pygame.K_z:
                if i < 273:
                    screen.blit(z, (locationx(i), locationy(i)))
                    i += 1
            elif event.key == pygame.K_j:
                if i < 273:
                    screen.blit(j, (locationx(i), locationy(i)))
                    i += 1
            elif event.key == pygame.K_f:
                if i < 273:
                    screen.blit(f, (locationx(i), locationy(i)))
                    i += 1
            elif event.key == pygame.K_y:
                if i < 273:
                    screen.blit(y, (locationx(i), locationy(i)))
                    i += 1
            elif event.key == pygame.K_k:
                if i < 273:
                    screen.blit(k, (locationx(i), locationy(i)))
                    i += 1
            elif event.key == pygame.K_l:
                if i < 273:
                    screen.blit(l, (locationx(i), locationy(i)))
                    i += 1
            elif event.key == pygame.K_m:
                if i < 273:
                    screen.blit(m, (locationx(i), locationy(i)))
                    i += 1
            elif event.key == pygame.K_n:
                if i < 273:
                    screen.blit(n, (locationx(i), locationy(i)))
                    i += 1
            elif event.key == pygame.K_s:
                if i < 273:
                    screen.blit(s, (locationx(i), locationy(i)))
                    i += 1
            elif event.key == pygame.K_u:
                if i < 273:
                    screen.blit(u, (locationx(i), locationy(i)))
                    i += 1
            elif event.key == pygame.K_p:
                if i < 273:
                    screen.blit(p, (locationx(i), locationy(i)))
                    i += 1
            elif event.key == pygame.K_x:
                if i < 273:
                    screen.blit(x, (locationx(i), locationy(i)))
                    i += 1
            elif event.key == pygame.K_q:
                if i < 273:
                    screen.blit(q, (locationx(i), locationy(i)))
                    i += 1
            elif event.key == pygame.K_r:
                if i < 273:
                    screen.blit(r, (locationx(i), locationy(i)))
                    i += 1
            elif event.key == pygame.K_c:
                if i < 273:
                    screen.blit(c, (locationx(i), locationy(i)))
                    i += 1
            elif event.key == pygame.K_t:
                if i < 273:
                    screen.blit(t, (locationx(i), locationy(i)))
                    i += 1
            elif event.key == pygame.K_SPACE:
                    if i < 273:
                        i += 1
            elif event.key == pygame.K_BACKSPACE:
                if (i > 1):
                    i -= 1
                pygame.draw.rect(screen, WHITE, (locationx(i), locationy(i), 50, 50))
    
    pygame.display.flip()
    
    clock.tick(60)


if done:
    pygame.quit()



