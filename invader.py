import pygame
class Invader: 
    def __init__(self, game, x, y, size):
        self.x = x
        self.game = game
        self.y = y
        self.size = size
    def draw(self):
        invader = pygame.draw.rect(self.game.screen, ( 45, 20, 80),
        pygame.Rect(self.x,self.y, self.size, self.size))
        # Faire la vitesse des ennemis
        if len(self.game.invaders) >= 60 :
            self.y += 0.02
        if self.game.level >= 6:
            self.y += 0.05
        if self.game.level >= 4 and self.game.level < 6:
            self.y += 0.04
        if self.game.level >= 2 and self.game.level < 4:
            self.y += 0.03
        if self.game.level < 2:
            self.y += 0.02

