import sys
import pygame as py
from scripts.utility import gen_background

py.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1400, 850
screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

stars = gen_background(500, SCREEN_WIDTH, SCREEN_HEIGHT)
player_pos = py.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

dt = 0
clock = py.time.Clock()

while True:
    screen.fill('black')
    for i in stars:
        py.draw.circle(screen, "white", i, 1)
    py.draw.circle(screen, "white", player_pos, 20)

    keys = py.key.get_pressed()
    if keys[py.K_w] or keys[py.K_UP]: 
        if player_pos.y > 20:
            player_pos.y -= 500 * dt
    if keys[py.K_s] or keys[py.K_DOWN]:
        if player_pos.y < SCREEN_HEIGHT - 20:
            player_pos.y += 500 * dt
    if keys[py.K_a] or keys[py.K_LEFT]:
        if player_pos.x > 20:
            player_pos.x -= 500 * dt
    if keys[py.K_d] or keys[py.K_RIGHT]:
        if player_pos.x < SCREEN_WIDTH -20:
            player_pos.x += 500 * dt

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
    dt = clock.tick(60) / 1000
    py.display.flip()
