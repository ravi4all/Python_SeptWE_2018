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

snakeList = []
snakeLength = 1

def snake(snakeList):
    for i in range(len(snakeList)):
        pygame.draw.rect(screen, black, [snakeList[i][0],
                                         snakeList[i][1],
                                         50,50])

clock = pygame.time.Clock()
FPS = 100

snakeHeadImage = pygame.image.load("image1.png")

def gameOver():
    font = pygame.font.SysFont(None, 80)
    text = font.render("Game Over", True, black)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(text, (300,200))
        pygame.display.update()



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveX = 5
                moveY = 0
            elif event.key == pygame.K_LEFT:
                moveX = -5
                moveY = 0
            elif event.key == pygame.K_DOWN:
                moveY = 5
                moveX = 0
            elif event.key == pygame.K_UP:
                moveY = -5
                moveX = 0

    screen.fill(red)

    # surface,color,[x,y,width,height]
    # rect_1 = pygame.draw.rect(screen,black,[x,y,50,50])
    rect_1 = pygame.Rect(x,y,50,50)
    screen.blit(frog, (frogX, frogY))
    frogRect = pygame.Rect(frogX, frogY, frog.get_width(), frog.get_height())

    if rect_1.colliderect(frogRect):
        frogX = random.randint(0, width - frog.get_width())
        frogY = random.randint(0, height - frog.get_height())
        snakeLength += 10

    x += moveX
    y += moveY

    snakeHead = []
    snakeHead.append(x)
    snakeHead.append(y)
    snakeList.append(snakeHead)

    if len(snakeList) > snakeLength:
        del snakeList[0]

    snake(snakeList)
    screen.blit(snakeHeadImage, (x, y))

    for each in snakeList[:-1]:
        if each == snakeList[-1]:
            gameOver()

    if x > width:
        x = -50
    elif x < -50:
        x = width
    elif y > height:
        y  = -50
    elif y < -50:
        y = height

    pygame.display.update()
    clock.tick(FPS)
