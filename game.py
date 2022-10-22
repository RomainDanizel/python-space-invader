
import pygame
import time
from player import Player
from invader import Invader
from spawner import Spawner
from bullet import Bullet

class Game: 
    # Array du canvas
    invaders = []
    bullets = []
    score = 0
    level = 0
    def __init__(self, width, height):
        module_charge = pygame.init()
        # Mettre en place le visuel
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width,height))
        pygame.display.set_caption('8Space Invader')
        # Savoir si la partie est finis ou non
        end = False

        # Appeler les classes
        player = Player(self, width / 2, height - 40, 30)
        invader = Invader(self, 300, 290, 30)
        spawner = Spawner(self, invader.size)
        bullet = Bullet(self, player, 300,200 )
        # Lancer la partie
        while not end:     
            self.showtext(self.score, width / 2, 0) 
            self.showtext('Niveau :' + ' ' + str(self.level), width / 10, 0)
            keyhold = pygame.key.get_pressed()
            #  Créer les mouvements du joueur
            for event in pygame.event.get():
                if keyhold[pygame.K_d]:
                    if  player.x <= width - 40:
                        player.x = player.x + 10
            
                if keyhold[pygame.K_q]:
                    if player.x >= 10:
                        player.x = player.x - 10
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        self.bullets.append(Bullet(self,player, player.x, player.y))
                       
                if event.type == pygame.QUIT:
                    end = True
            # Visuel du jeu 
            pygame.display.flip()
            self.screen.fill((2, 2, 2))
            player.draw()
            for bullet in self.bullets:
                bullet.draw()
                if bullet.y < 0:
                    self.bullets.remove(bullet)
            for invader in self.invaders:
                invader.draw()
                if (invader.y + invader.size > height or player.x < invader.x + invader.size and
                    player.x > invader.x - invader.size and
                    player.y < invader.y + invader.size and
                    player.y > invader.y - invader.size):
                    end = True
                    time.sleep(1)
            for invader in self.invaders:
                for bullet in self.bullets:
                    if (bullet.x < invader.x + invader.size and
                    bullet.x > invader.x - invader.size and
                    bullet.y < invader.y + invader.size and
                    bullet.y > invader.y - invader.size):
                        self.score += 1
                        self.bullets.remove(bullet)      
                        self.invaders.remove(invader)
            if len(self.invaders) == 0:
                invader.y += 1
                self.level += 1
                Spawner(self, invader.size)
            
    def showtext(self, text, x, y ):
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 48)
        textsurface = font.render(str(text), True, (44, 0, 62))
        self.screen.blit(textsurface, (x, y))