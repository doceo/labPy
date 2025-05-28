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

    for event in pygame.get():
        if event.type == pygame.QUIT:
 
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                running = True
            elif event.key == pygame.K_a and pygame.K_b:
                Sprinting == True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                running = False
            elif event.key == pygame.K_a and pygame.K_b:
                Sprinting = False
    
    if Sprinting == True:
        print("Sprinting")
    
    if running == True:
        print("Running")

pygame.quit()