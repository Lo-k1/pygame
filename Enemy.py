import pygame


class Enemy1(pygame.sprite.Sprite):
    def __init__(self, level, type, x, y, group, group1):
        self.group1 = group1
        if type == 1:
            self.image = pygame.image.load('data/enemyBlack1.png')
            self.health = 1
        elif type == 2:
            self.image = pygame.image.load('data/enemyBlack2.png')
            self.health = 2
        elif type == 3:
            self.image = pygame.image.load('data/enemyBlack3.png')
            self.health = 3
        elif type == 4:
            self.image = pygame.image.load('data/enemyBlack4.png')
            self.health = 4
        elif type == 5:
            self.image = pygame.image.load('data/enemyBlack5.png')
            self.health = 5
        pygame.sprite.Sprite.__init__(self)
        self.level = level
        self.type = type
        self.group = group
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.add(group)

    def update(self, *args):
        if pygame.sprite.spritecollide(self, self.group1, True):
            self.health -= 1
        if self.health == 0:
            self.kill()


class Enemybullet(pygame.sprite.Sprite):
    def __init__(self, type, x, y, group, t):
        pygame.sprite.Sprite.__init__(self)
        self.t = t
        self.type = type
        self.image = pygame.image.load('data/laserRed07.png')
        self.rect = self.image.get_rect()
        if self.type == 1:
            self.rect.x = x + 42
            self.rect.y = y + 84
        if self.type == 2:
            self.rect.x = x + 47
            self.rect.y = y + 84
        if self.type == 3:
            self.rect.x = x + 47
            self.rect.y = y + 84
        if self.type == 4:
            self.rect.x = x + 36
            self.rect.y = y + 84
        if self.type == 5:
            self.rect.x = x + 44
            self.rect.y = y + 84

        self.group = group
        self.add(self.group)
        self.x = x
        self.y1 = y

    def update(self, x, y):
        self.x = self.rect.x
        self.y = self.rect.y
        if self.x >= x and self.x < x + 98 and self.y <= y + 75 and self.y > y:
            self.rect = self.rect.move(0, -31 * self.t * 50)
        if self.rect[1] < 731:
            self.rect = self.rect.move(0, 10)
        else:
            self.rect = self.rect.move(0, -31 * self.t * 50)
        if self.rect[1] > -74 and self.rect[1] < 0:
            self.rect = self.rect.move(0, self.y1 + abs(self.rect[1]) + 30)
