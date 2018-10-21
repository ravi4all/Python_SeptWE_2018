import pygame
import random
pygame.init()

red = 255,0,0
blue = 0,0,255
green = 0,255,0
yellow = 255,255,0
white = 255,255,255
black = 0,0,0

width = 1000
height = 500

colors = [blue,green,white,yellow,black]
color = random.choice(colors)
screen = pygame.display.set_mode((width, height))
x = 10
y = 10
moveX = 1
moveY = 1
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(red)

    # surface,color,[x,y,width,height]
    pygame.draw.circle(screen,color,[x,y],50)
    x += moveX
    y += moveY
    if x > width - 50:
        moveX = -1
        color = random.choice(colors)
    elif x < 50:
        moveX = 1
        color = random.choice(colors)
    elif y > height - 50:
        moveY = -1
        color = random.choice(colors)
    elif y < 50:
        moveY = 1
        color = random.choice(colors)

    pygame.display.update()
