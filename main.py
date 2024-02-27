import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycast import *
from object_renderer import *
from sprite_object import *
from object_handler import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.newgame()

    def newgame(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = Objectrenderer(self)
        self.raycasting = Raycasting(self)
        self.static_sprite = SpriteObject(self)
        self.animated_sprite = AnimatedSprite(self)
        self.object_handler = ObjectHandler(self)
    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        #self.static_sprite.update()
        #self.animated_sprite.update()

        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption('FPS (folladas por segundo): ' + f'{self.clock.get_fps() :.1f}')

    def draw(self):
        #self.screen.fill('black')
        self.object_renderer.draw()
        #self.map.draw()
        #self.player.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type==pg.KEYDOWN and event.type==pg.K_ESCAPE):
                pg.quit()
                sys.exit()


    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()