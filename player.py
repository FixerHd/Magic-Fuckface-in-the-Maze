from settings import *
import sys
import pygame as pg
import math


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.shot = False
        self.health = PLAYER_MAX_HEALTH
        self.rel = 0
        self.health_recovery_delay = 1400
        self.time_prev = pg.time.get_ticks()

    def recover_health(self):
        if self.check_health_recovery_delay() and self.health < PLAYER_MAX_HEALTH:
            self.health += 1

    def check_health_recovery_delay(self):
        time_now = pg.time.get_ticks()
        if time_now - self.time_prev > self.health_recovery_delay:
            self.time_prev = time_now
            return True

    def check_game_over(self):
        if self.health < 1:
            self.game.object_renderer.game_over()
            pg.display.flip()
            self.game.sound.stop_music()
            pg.time.delay(5000)
            pg.quit()
            sys.exit()

    def get_damage(self, damage):
        self.health -= damage
        self.game.sound.player_pain.play()
        self.check_game_over()

    def single_fire_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == TECLA_DISPARO and not self.shot and not self.game.power.reloading:
                self.game.sound.beam.play()
                self.shot = True
                self.game.power.reloading = True

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        num_key_pressed = -1
        if keys[TECLA_ARRIBA]:
            num_key_pressed += 1
            dx += speed_cos
            dy += speed_sin
        if keys[TECLA_ABAJO]:
            num_key_pressed += 1
            dx += -speed_cos
            dy += -speed_sin
        if keys[TECLA_IZQUIERDA]:
            num_key_pressed += 1
            dx += speed_sin
            dy += -speed_cos
        if keys[TECLA_DERECHA]:
            num_key_pressed += 1
            dx += -speed_sin
            dy += speed_cos


        self.check_wall_collision(dx, dy)

        if keys[TECLA_ROTARIZQUIERDA]:
             self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[TECLA_ROTARDERECHA]:
             self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        scale = PLAYER_SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def update(self):
        self.movement()
        self.recover_health()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)
