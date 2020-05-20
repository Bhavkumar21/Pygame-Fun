import pygame, sys

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.Font("freesansbold.ttf", 32)

screen_height = 780
screen_width = 1280
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

ball = pygame.Rect(screen_width/2 - 10, screen_height/2 - 10, 20, 20)
ball_speed_x = 7
ball_speed_y = 7

player = pygame.Rect(screen_width - 60, screen_height/2 - 85, 40, 170)
pVelo = 0

opponent = pygame.Rect(30, screen_height/2 - 85, 40, 170)
oVelo = 0

color = (200,200,200)

player_score = 0
opponent_score = 0

restart = False
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pVelo = -7
            if event.key == pygame.K_DOWN:
                pVelo = 7
            if event.key == pygame.K_w:
                oVelo = -7
            if event.key == pygame.K_s:
                oVelo = 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                pVelo = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                oVelo = 0


    screen.fill((0,0,0))
    pygame.draw.aaline(screen, color, (screen_width / 2, 0), (screen_width / 2, screen_height))
    pygame.draw.ellipse(screen, color, ball)
    pygame.draw.rect(screen, color, player)
    pygame.draw.rect(screen, color, opponent)
    displayp = font.render("Score:" + str(opponent_score), True, (255, 255, 255))
    screen.blit(displayp, (10, 10))
    displayo = font.render("Score:" + str(player_score), True, (255, 255, 255))
    screen.blit(displayo, (screen_width - 130, 10))

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    if ball.left <= 0 :
        player_score += 1
        restart = True
    if ball.right >= screen_width:
        opponent_score += 1
        restart = True

    if player.y >= screen_height:
        player.y = 1
    if player.y <= 0:
        player.y =  screen_height - 1

    if opponent.y >= screen_height:
        opponent.y = 1
    if opponent.y <= 0:
        opponent.y =  screen_height - 1

    ball.x += ball_speed_x
    ball.y += ball_speed_y
    player.y += pVelo
    opponent.y += oVelo

    if restart:
        ball.x = screen_width/2 - 10
        ball.y = screen_height/2 - 10
        restart = False

    clock.tick(60)
    pygame.display.flip()