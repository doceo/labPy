import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = False
run = True
Sprinting = False
while run:
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        print("Click")
    elif event.type == pygame.MOUSEBUTTONUP:
           print("release")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
   
pygame.quit()


