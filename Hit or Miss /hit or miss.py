import pygame, sys, random

class Crosshair(pygame.sprite.Sprite):
    def __init__(self,  picture):
        super().__init__()
        self.image = pygame.image.load(picture)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Target(pygame.sprite.Sprite):
    def __init__(self, picture, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

pygame.init()
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

crosshair = Crosshair("crosshair.png")
group = pygame.sprite.Group()
group.add(crosshair)

tgroup = pygame.sprite.Group()
for target in range(20):
    new_target = Target("target.png", random.randint(0, 500), random.randint(0, 500))
    tgroup.add(new_target)

pygame.mouse.set_visible(False)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.sprite.spritecollide(crosshair, tgroup, True)



    screen.fill((173, 216, 230))
    tgroup.draw(screen)
    group.draw(screen)
    group.update()
    pygame.display.flip()
    clock.tick(60)
