from settings import *
import pygame as pg
import math


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = 2, 2
        self.angle = PLAYER_ANGLE

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            self.x += speed_cos
            self.y += speed_sin
        if keys[pg.K_s]:
            self.x += -speed_cos
            self.y += -speed_sin
        if keys[pg.K_a]:
            self.x += speed_cos
            self.y += -speed_sin
        if keys[pg.K_d]:
            self.x += -speed_cos
            self.y += speed_sin

        self.x = self.x
        self.y = self.y

        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROTSPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROTSPEED * self.game.delta_time
        self.angle %= math.tau

    def draw(self):
        pg.draw.line(self.game.screen, 'green', (self.x * 55, self.y * 37),
                     (self.x * 55 + WIDTH * math.cos(self.angle),
                      self.y * 37 + WIDTH * math.sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'blue', (self.x * 55, self.y * 37), 15)


    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)
