import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycast import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from powers import *
from sound import *
from pathfinding import *

class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        pg.event.set_grab(True)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = Raycasting(self)
        self.object_handler = ObjectHandler(self)
        self.power = Power(self)
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self)
        pg.mixer.music.play(-1)
    
    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.power.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption('FPS (folladas por segundo): ' + f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.object_renderer.draw()
        self.power.draw()

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_6):
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)


    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

