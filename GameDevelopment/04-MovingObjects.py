import pygame
pygame.init()
red = 255,0,0
white = 255,255,255
black = 0,0,0

width = 1000
height = 500

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
    pygame.draw.rect(screen,black,[x,y,50,50])
    x += moveX
    y += moveY
    if x > width - 50:
        moveX = -1
    elif x < 0:
        moveX = 1
    elif y > height - 50:
        moveY = -1
    elif y < 0:
        moveY = 1

    pygame.display.update()
