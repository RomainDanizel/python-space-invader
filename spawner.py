import pygame
import random
from invader import Invader
class Spawner:
    def __init__(self, game, size):
        margin = 50 
        space = random.randint(size, size * 3)
        self.size = size
        for x in range(margin, game.width - margin, space):
            for y in range(margin, int(game.height / 2), space):
                game.invaders.append(Invader(game,x, y, size))