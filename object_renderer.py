import pygame as pg
from settings import *

class Objectrenderer:
    def __init__(self, game):
        self.game = game
        self.screen = self.game.screen

    @staticmethod
    def get_texture_path(path, res = (TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

