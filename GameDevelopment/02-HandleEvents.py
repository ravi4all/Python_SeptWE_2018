import pygame
pygame.init()
red = 255,0,0
white = 255,255,255
black = 0,0,0

screen = pygame.display.set_mode((1000,500))

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(red)
    pygame.display.update()
