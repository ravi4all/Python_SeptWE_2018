import pygame
pygame.init()

# red = 255,0,0
white = 255,255,255
black = 0,0,0

height = 500
width = 1000

screen = pygame.display.set_mode((width, height))

myShip = pygame.image.load("images/ship_1.png")
shipWidth = myShip.get_width()
shipHeight = myShip.get_height()
# print(shipWidth, shipHeight)
image = pygame.Surface((shipWidth, shipHeight))
rect = image.get_rect()
rect.x = (width / 2) - 50
rect.y = height - 100

bulletImage = pygame.Surface((10,20))
bulletRect = bulletImage.get_rect()
bulletRect.y = rect.y + shipWidth / 2 - 40

moveX = 0
moveY = 0

clock = pygame.time.Clock()
FPS = 100
fire = False
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keypressed = pygame.key.get_pressed()
    if keypressed[pygame.K_RIGHT]:
        moveX = 4
    elif keypressed[pygame.K_LEFT]:
        moveX = -4
    elif keypressed[pygame.K_SPACE]:
        fire = True
    else:
        moveX = 0

    if fire:
        bulletRect.y -= 10

    screen.fill(white)

    bulletRect.x = rect.x + shipWidth / 2
    pygame.draw.rect(screen,black,bulletRect)
    screen.blit(myShip,(rect.x, rect.y))
    rect.x += moveX

    if rect.x < 0:
        rect.x = 0
    elif rect.x > width - shipWidth:
        rect.x = width - shipWidth
    elif bulletRect.y < 0:
        bulletRect.y = rect.y + shipWidth / 2 - 40
        fire = False

    pygame.display.update()
    clock.tick(FPS)
