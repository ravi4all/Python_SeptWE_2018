import pygame
pygame.init()
red = 255,0,0
white = 255,255,255
black = 0,0,0

screen = pygame.display.set_mode((1000,500))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(red)
    # surface,color,[x,y,width,height]
    pygame.draw.rect(screen,black,[10,10,50,50])

    # surface, color, [x,y], radius
    pygame.draw.circle(screen,black,[100,100],50)

    pygame.display.update()
