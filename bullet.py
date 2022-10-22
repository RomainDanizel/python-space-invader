import pygame
class Bullet:
    def __init__(self, game, player, x , y):
        self.player = player
        self.x = player.x
        self.y = player.y
        self.game = game
        self.player = player

    def draw(self):
        bullet = pygame.draw.rect(self.game.screen, ( 70, 0, 180),
        pygame.Rect(int(self.x + (self.player.size - self.player.size / 2) / 2),self.y, 10, 10))
        self.y -= 1