import pygame
pygame.init()
red = 255,0,0
white = 255,255,255
black = 0,0,0

screen = pygame.display.set_mode((1000,500))

while True:
    screen.fill(red)
    pygame.display.update()
