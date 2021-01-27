import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, group, typ):
        pygame.sprite.Sprite.__init__(self)
        self.typ = typ
        if self.typ == 1:
            self.image = pygame.image.load('data\laserRed04.png')
            self.rect = self.image.get_rect()
            self.rect.x = x + 99 // 2 - 6.5
            self.rect.y = y - 75 // 2 - 0.5
        if self.typ == 2:
            self.image = pygame.image.load('data\laserGreen08.png')
            self.rect = self.image.get_rect()
            self.rect.x = x + 112 // 2 - 6.5
            self.rect.y = y - 75 // 2 - 0.5
        if self.typ == 3:
            self.image = pygame.image.load('data\laserBlue04.png')
            self.rect = self.image.get_rect()
            self.rect.x = x + 98 // 2 - 6.5
            self.rect.y = y - 75 // 2 - 0.5
        self.speed = speed
        if not pygame.sprite.spritecollideany(self, group):
            self.add(group)

    def update(self, *args):
        if self.rect[1] > -1 * self.speed:
            self.rect = self.rect.move(0, -1 * self.speed)
        else:
            self.kill()
