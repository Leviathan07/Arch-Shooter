import sys
import pygame as py
from scripts.utility import gen_background, spawn_enemy

class Player(py.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = py.image.load("./player.png").convert()
        self.width, self.height = py.display.get_window_size()
        self.rect = self.image.get_frect(center = (self.width // 2, self.height // 2))
        self.laser_rect = py.FRect((0, -40), (20, 25))

    def update(self, dt):
        #input
        keys = py.key.get_pressed()
        if keys[py.K_w] or keys[py.K_UP]:
            if self.rect.y > 0:
                if keys[py.K_d] or keys[py.K_a] or keys[py.K_LEFT] or keys[py.K_RIGHT]:
                    self.rect.y -= 250 * dt
                else:
                    self.rect.y -= 500 * dt
        if keys[py.K_s] or keys[py.K_DOWN]:
            if self.rect.bottom < self.height:
                if keys[py.K_d] or keys[py.K_a] or keys[py.K_LEFT] or keys[py.K_RIGHT]:
                    self.rect.y += 250 * dt
                else:
                    self.rect.y += 500 * dt
        if keys[py.K_a] or keys[py.K_LEFT]:
            if self.rect.left > 0:
                if keys[py.K_w] or keys[py.K_s] or keys[py.K_UP] or keys[py.K_DOWN]:
                    self.rect.x -= 400 * dt
                else:
                    self.rect.x -= 500 * dt
        if keys[py.K_d] or keys[py.K_RIGHT]:
            if self.rect.right < self.width:
                if keys[py.K_w] or keys[py.K_s] or keys[py.K_UP] or keys[py.K_DOWN]:
                    self.rect.x += 400 * dt
                else:
                    self.rect.x += 500 * dt
        key = py.key.get_just_pressed()
        if (key[py.K_SPACE] or key[py.K_z]): 
            Laser(self.rect.midtop, all_sprites)

class Laser(py.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = py.image.load("./laser.png").convert()
        self.rect = self.image.get_frect(midbottom = pos)

    def update(self, dt):
        self.rect.centery -= 900 * dt
        if self.rect.bottom < 0:
            self.kill()





py.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1400, 900
screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
all_sprites = py.sprite.Group()
player = Player(all_sprites)

stars = gen_background(500, SCREEN_WIDTH, SCREEN_HEIGHT)

can_shoot = True
dt = 0
clock = py.time.Clock()

score = 0

timer = py.event.custom_type()
py.time.set_timer(timer, 700)
while True:
    dt = clock.tick() / 1000
    screen.fill('black')
    for i in stars:
        py.draw.circle(screen, "white", i, 1)

    all_sprites.update(dt)
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

        if event.type == timer:
            #spawn_enemy(SCREEN_WIDTH, SCREEN_HEIGHT, 1, screen)
            score += 1

    all_sprites.draw(screen)
    py.display.update()

'''
Resources
pygame-ce:    https://pyga.me/docs/
Referance:    https://pyga.me/docs/
Referance:    https://www.w3schools.com/python/default.asp
Player image: https://github.com/joaofranciscoguarda/arch-pixel-icons?tab=readme-ov-file
Enemy images: https://icons8.com/icons/set/pixel-windows--style-color
'''
