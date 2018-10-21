import pygame
pygame.init()

white = 255,255,255

width = 1000
height = 600

screen = pygame.display.set_mode((width, height))

ball = pygame.image.load("ball_2.png")
bg = pygame.image.load("game_bg.jpg")

hit = pygame.mixer.Sound("hit.wav")

x = 10
y = 10
moveX = 5
moveY = 5

clock = pygame.time.Clock()
FPS = 150

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # screen.fill(white)
    screen.blit(bg, (0,0))
    screen.blit(ball, (x,y))

    x += moveX
    y += moveY
    if x > width - 150:
        moveX = -5
        hit.play()
    elif x < 0:
        moveX = 5
        hit.play()
    elif y > height - 155:
        moveY = -5
        hit.play()
    elif y < 0:
        moveY = 5
        hit.play()

    pygame.display.update()
    clock.tick(FPS)
