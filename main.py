from turtle import heading
import pygame
from game import Game
from player import Player
from invader import Invader
from spawner import Spawner
from bullet import Bullet

windowwith = input('Longueur de la fenêtre (conseillés 600) :')
windowheight = input('Hauteur de la fenêtre (conseillés 500) :')
Game(int(windowwith), int(windowheight))