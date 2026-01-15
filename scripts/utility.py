import pygame as py
import random as rand

def gen_background(x, SCREEN_WIDTH, SCREEN_HEIGHT):
    stars = []
    for i in range(x):
        stars.append(py.Vector2(rand.randint(0, SCREEN_WIDTH), rand.randint(0, SCREEN_HEIGHT)))
    return stars

def spawn_enemy(SCREEN_WIDTH, SCREEN_HEIGHT):
    print('works')
