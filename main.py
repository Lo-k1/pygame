import pygame

from Bullets import Bullet
from Button import button
from Enemy import Enemy1, Enemybullet

global lev
lev = 0
k = 0
g = 0
speed = 3
speed_b = 10
d = 0
n = 0
pygame.init()
size = w, h = 512, 768
x = w // 2 - 99 // 2
y = h - 75 // 2
screen = pygame.display.set_mode(size)
start = False


def select():
    sel = pygame.transform.scale(pygame.image.load('data\\select.jpg'), (w, h))
    _1 = button(None, 0, 0, 512, 256, '')
    _2 = button(None, 0, 256, 512, 256, '')
    _3 = button(None, 0, 512, 512, 256, '')
    sh = True
    while sh:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.isOver(_1, event.pos):
                    return 1
                if button.isOver(_2, event.pos):
                    return 2
                if button.isOver(_3, event.pos):
                    return 3
        screen.blit(sel, (0, 0))
        _1.draw(screen)
        _2.draw(screen)
        _3.draw(screen)
        pygame.display.flip()


def wave(n):
    pygame.font.init()
    text = 'Волна ' + str(n)
    myfont = pygame.font.SysFont('bahnschrift', 50)
    textsurface = myfont.render(text, False, (52, 229, 235))
    screen.blit(textsurface, (128, 256))
    n += 1
    pygame.display.flip()
    pygame.time.delay(1500)


def level(lev):
    alive = False
    for i in spi:
        if len(i) != 0:
            alive = True
    if not alive:
        lev += 1
        if lev == 1:
            spawn(1, 0, 0, a1, 1)
            spawn(1, 400, 0, a2, 1)
        if lev == 2:
            spawn(5, 200, 75, a1, (1 / 2))
            spawn(1, 100, 0, a2, 1)
            spawn(1, 300, 0, a3, 1)
        if lev == 3:
            spawn(5, 200, 75, a1, (1 / 2))
            spawn(3, 100, 0, a2, 1)
            spawn(3, 300, 0, a3, 1)
        if lev == 4:
            spawn(5, 200, 75, a1, 1)
            spawn(5, 0, 0, a2, 1)
            spawn(5, 400, 0, a3, 1)
        if lev == 5:
            spawn(5, 200, 75, a1, (1 / 2))
            spawn(1, 100, 0, a2, 1)
            spawn(1, 300, 0, a3, 1)
        if lev != 1:
            wave(lev)
    return lev


def menu():
    start_button = button(None, 128, 256, 256, 128, 'Старт', (52, 229, 235), 'bahnschrift', 40)
    exit_button = button(None, 128, 384, 256, 128, 'Выход', (52, 229, 235), 'bahnschrift', 40)
    show = True
    men = pygame.transform.scale(pygame.image.load('data\\menu.jpg'), (w, h))
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.isOver(start_button, event.pos):
                    show = False
                if button.isOver(exit_button, event.pos):
                    quit()
        screen.blit(men, (0, 0))
        start_button.draw(screen)
        exit_button.draw(screen)
        pygame.display.flip()


def game_over():
    start_button = button(None, 128, 256, 256, 64, 'Играть', (52, 229, 235), 'bahnschrift', 40)
    start_button1 = button(None, 128, 300, 256, 64, 'с начала', (52, 229, 235), 'bahnschrift', 40)
    exit_button = button(None, 128, 384, 256, 128, 'Выход', (52, 229, 235), 'bahnschrift', 40)
    show = True
    men = pygame.transform.scale(pygame.image.load('data\\menu.jpg'), (w, h))
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.isOver(start_button, event.pos) or button.isOver(start_button1, event.pos):
                    show = False
                    break
                if button.isOver(exit_button, event.pos):
                    quit()
        screen.blit(men, (0, 0))
        start_button.draw(screen)
        start_button1.draw(screen)
        exit_button.draw(screen)
        pygame.display.flip()
        global __1
        __1 = True
    typ = select()
    for i in spi:
        i.empty()
    global x
    global y
    global lev
    global running
    if not running:
        x, y, lev, running = sbros()
    Player(group, typ)
    group.update(x, y)


def spawn(type, x1, y1, name, t):
    name.add(Enemybullet(type, x1, y1, name, t))
    name.add(Enemy1(0, type, x1, y1, name, bullets))


def sbros():
    x = w // 2 - 99 // 2
    y = h - 75 // 2
    return x, y, 0, True


def anim(d):
    d += 1
    fon = pygame.transform.scale(pygame.image.load('data\\black1.jpg'), (w, h))
    screen.blit(fon, (0, d))
    screen.blit(fon, (0, -768 + d))
    if d == 768:
        return 0
    return d


menu()
typ = select()
start = True


class Player(pygame.sprite.Sprite):

    def __init__(self, group, typ):
        global speed
        global ty
        ty = typ
        self.typ = typ
        if self.typ == 1:
            self.hp = 2
            self.c = 'red'
            speed = 4
        elif self.typ == 2:
            self.hp = 3
            self.c = 'green'
            speed = 3
        else:
            self.hp = 4
            speed = 2
            self.c = 'blue'
        screen.blit(pygame.image.load("data/playerLife_" + self.c + ".png"), (0, 0))
        super().__init__(group)
        self.image = pygame.transform.scale(pygame.image.load("data/" + self.c + "d" + str(self.hp) + ".png"), (99, 75))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.is_dmg = False
        self.is_dmg1 = False
        self.rect.y = y

    def update(self, x, y):
        self.hp1 = self.hp
        self.rect.x = x
        self.rect.y = y
        self.is_dmg1 = self.is_dmg
        for i in spi:
            if pygame.sprite.spritecollideany(self, i):
                self.is_dmg = True
                break
            else:
                self.is_dmg = False
        if self.is_dmg != self.is_dmg1 and self.is_dmg == False:
            self.hp -= 1
        if self.hp1 != self.hp and self.hp != 0:
            self.image = pygame.transform.scale(pygame.image.load("data/" + self.c + "d" + str(self.hp) + ".png"),
                                                (99, 75))
        screen.blit(pygame.image.load("data/playerLife_" + self.c + ".png"), (0, 0))
        if self.hp == 1:
            screen.blit(pygame.image.load("data/numeral1.png"), (37, 0))

        if self.hp == 2:
            screen.blit(pygame.image.load("data/numeral2.png"), (37, 0))

        if self.hp == 3:
            screen.blit(pygame.image.load("data/numeral3.png"), (37, 0))

        if self.hp == 4:
            screen.blit(pygame.image.load("data/numeral4.png"), (37, 0))
        if self.hp <= 0:
            global running
            running = False
            self.kill()
            game_over()
        global hp
        hp = self.hp


group = pygame.sprite.Group()
a0 = pygame.sprite.Group()
a1 = pygame.sprite.Group()
a2 = pygame.sprite.Group()
a3 = pygame.sprite.Group()
a4 = pygame.sprite.Group()
a5 = pygame.sprite.Group()
a6 = pygame.sprite.Group()
a7 = pygame.sprite.Group()
a8 = pygame.sprite.Group()
a9 = pygame.sprite.Group()
spi = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]
bullets = pygame.sprite.Group()
bul_kd = 0
Player(group, typ)
running = True
__1 = True
if start:
    while running:
        if lev == 1 and __1:
            anim(d)
            wave(lev)
            __1 = False
        bul_kd += 1
        if bul_kd == 20:
            bul_kd = 0
        d = anim(d)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 0:
            x -= speed
        if keys[pygame.K_RIGHT] and x < w - 112:
            x += speed
        if keys[pygame.K_UP] and y > 0:
            y -= speed
        if keys[pygame.K_DOWN] and y < h - 75:
            y += speed
        if keys[pygame.K_SPACE] and hp > 0 and bul_kd == 0:
            Bullet(x, y, speed_b, bullets, ty)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        group.draw(screen)
        for i in spi:
            if len(i) == 2:
                i.update(x, y)
                i.draw(screen)
            else:
                i.empty()
        bullets.update()
        bullets.draw(screen)
        group.update(x, y)
        pygame.display.flip()
        lev = level(lev)

pygame.quit()
