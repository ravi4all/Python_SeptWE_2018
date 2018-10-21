import random
import pygame

pygame.init()
red = 255,0,0
white = 255,255,255
black = 0,0,0

width = 1000
height = 500

screen = pygame.display.set_mode((width, height))

frog = pygame.image.load("frog.png")

frogX = random.randint(0,width - frog.get_width())
frogY = random.randint(0,height - frog.get_height())

x = 10
y = 10
moveX = 0
moveY = 0
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveX = 1
                moveY = 0
            elif event.key == pygame.K_LEFT:
                moveX = -1
                moveY = 0
            elif event.key == pygame.K_DOWN:
                moveY = 1
                moveX = 0
            elif event.key == pygame.K_UP:
                moveY = -1
                moveX = 0

    screen.fill(red)

    # surface,color,[x,y,width,height]
    rect_1 = pygame.draw.rect(screen,black,[x,y,50,50])
    screen.blit(frog, (frogX, frogY))
    frogRect = pygame.Rect(frogX, frogY, frog.get_width(), frog.get_height())

    if rect_1.colliderect(frogRect):
        frogX = random.randint(0, width - frog.get_width())
        frogY = random.randint(0, height - frog.get_height())

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
