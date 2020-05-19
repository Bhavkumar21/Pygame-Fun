import pygame
import math
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
background = pygame.image.load("background.png")

# player
playerimg = pygame.image.load("gaming.png")
playerX = 378
playerY = 504
changeX = 0
changeY = 0

# enemy
enemyImg = pygame.image.load("game.png")
enemyX = []
enemyY = []
echangeX = []
echangeY = []
enemy = 6
for i in range(enemy):
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    echangeX.append(4)
    echangeY.append(20)

# bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 504
bchangeX = 0
bchangeY = 10
bulletFired = False

score = 0
font = pygame.font.Font("freesansbold.ttf", 32)


def fireBullet(x, y):
    global bulletFired
    bulletFired = True
    screen.blit(bulletImg, (x + 16, y + 10))


def collision(X, Y, x, y):
    distance = math.sqrt(math.pow(X - x, 2) + math.pow(Y - y, 2))
    if distance < 30:
        return True
    return False

lose = False
run = True
while run:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                changeX = 5
            if event.key == pygame.K_LEFT:
                changeX = -5
            if event.key == pygame.K_UP:
                changeY = -5
            if event.key == pygame.K_DOWN:
                changeY = 5
            if event.key == pygame.K_SPACE:
                if not bulletFired:
                    bulletX = playerX
                    fireBullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                changeX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                changeY = 0
    for i in range(enemy):

        enemyX[i] += echangeX[i]
        if enemyX[i] > 742:
            echangeX[i] = -echangeX[i]
            enemyY[i] += echangeY[i]
        if enemyX[i] < -9:
            echangeX[i] = -echangeX[i]
            enemyY[i] += echangeY[i]
        screen.blit(enemyImg, (enemyX[i], enemyY[i]))

        if collision(bulletX, bulletY, enemyX[i], enemyY[i]):
            bulletFired = False
            enemyX[i] = (random.randint(0, 735))
            enemyY[i] = (random.randint(50, 150))
            score += 1

        if collision(playerX, playerY, enemyX[i], enemyY[i]):
            lose = True;

    playerX += changeX
    playerY += changeY
    if playerX > 805:
        playerX = -60
    if playerX < -61:
        playerX = 804

    if bulletY < -71:
        bulletY = playerY
        bulletFired = False

    if bulletFired:
        fireBullet(bulletX, bulletY)
        bulletY -= 10

    display = font.render("Score:" + str(score), True, (255, 255, 255))
    screen.blit(display, (10, 10))

    screen.blit(playerimg, (playerX, playerY))

    if score == 50:
        for i in range(enemy):
            enemyY[i] = 2000
        screen.fill((0,0,0))
        end = font.render("You win!", True, (255,255,255))
        screen.blit(end, (325,300))

    if lose:
        for i in range(enemy):
            enemyY[i] = 2000
            screen.fill((0, 0, 0))
            end = font.render("You Lose!", True, (255, 255, 255))
            screen.blit(end, (325, 300))

    pygame.display.update()
