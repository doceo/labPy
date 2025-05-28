#per il click del mouse con event handler
#mentre con get pressed è:

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
    
    mouse = pygame.mouse.get_pressed()
    print(mouse)
    print(type(mouse))
    print(pygame.MOUSEBUTTONDOWN)
    if mouse[pygame.MOUSEBUTTONDOWN] == True:
        print("click")
    if mouse[pygame.MOUSEBUTTONUP] == True:
        print("relase")

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
   
pygame.quit()
