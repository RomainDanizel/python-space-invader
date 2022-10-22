import pygame
class Player:
    def __init__(self,game , x, y, size ):
        self.x = x
        self.y = y
        self.game = game
        self.size = size
    def draw(self):
        player = pygame.draw.rect(self.game.screen, ( 0, 0, 255),
        pygame.Rect(self.x,self.y, self.size, self.size))