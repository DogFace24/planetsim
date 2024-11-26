import pygame   
import sys
import math

import time

pygame.init()

f = pygame.font.Font(None, 30)

start_t = time.time()
last_t = 0

YELLOW = (255,255,51)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (30, 144, 255)
RED = (156, 46, 43)
DARK_GRAY = (50, 50, 50) #used to make orbits

a_earth = 0
r_earth = 150
cex, cey = 300, 300

a_moon = 0
r_moon = 20

a_mars = 0
r_mars = (228/150)*r_earth


#variable parameters
global sp_rat, lps, moon_vis, empat
sp_rat = - 1#speed ratio
lps = 0.01 #lines per second
moon_vis = True #moon visibility
empat = False #earth mars pattern

def show_moon(moon_vis):
    if moon_vis is True:
        pygame.draw.circle(window, WHITE, (int(cirx_m), int(ciry_m)),2)

def show_empat(empat):
    if empat is True:
        pygame.draw.line(window, WHITE, (int(cirx), int(ciry)), (int(cirx_ma), int(ciry_ma)))
        pygame.draw.line(window, (100, 100, 100), coord[0], coord[1], 1)


window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("PLANET SIM")

def midp(p1, p2):
    return (int((p1[0]+p2[0])/2), int((p1[1]+p2[1])/2))

global coords
coords = []

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    window.fill(BLACK)

    pygame.draw.circle(window, YELLOW, (300, 300), 20)

    a_earth += 0.03 * sp_rat 

    d = (abs(a_earth)/6.28)*365
    text_s = f.render(f"{d:.2f} Earth Days", True, WHITE)
    text_rect = text_s.get_rect()
    text_rect.topright = (595, 10)

    window.blit(text_s, text_rect)

    a_moon += 0.05*13.37*sp_rat

    a_mars += (687/365)*0.03*sp_rat

    cirx = cex + r_earth*math.cos(a_earth)
    ciry = cey + r_earth*math.sin(a_earth)

    cirx_ma = cex + r_mars*math.cos(a_mars)
    ciry_ma = cey + r_mars*math.sin(a_mars)

    cex_m, cey_m = cirx, ciry

    cirx_m = cex_m + r_moon*math.cos(a_moon)
    ciry_m = cey_m - r_moon*math.sin(a_moon)


    pygame.draw.circle(window, DARK_GRAY, (300, 300), r_earth, 1)
    pygame.draw.circle(window, DARK_GRAY, (300, 300), r_mars, 1)

    pygame.draw.circle(window, BLUE, (int(cirx), int(ciry)), 5)
    show_moon(moon_vis)
    pygame.draw.circle(window, RED, (int(cirx_ma), int(ciry_ma)),5)

    now_t = time.time()
    elapsed_t = (now_t - start_t)


    if elapsed_t >= last_t + lps:
        coords.append(((int(cirx), int(ciry)), (int(cirx_ma), int(ciry_ma))))
        last_t += lps

    for coord in coords:
        show_empat(empat)

    pygame.display.flip()
    pygame.time.Clock().tick(60)
    
