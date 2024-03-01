import pygame as pg


class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound/'
        self.beam = pg.mixer.Sound(self.path + 'beam.mp3')
        self.npc_pain = pg.mixer.Sound(self.path + 'npc_pain.wav')
        self.npc_death = pg.mixer.Sound(self.path + 'npc_death.wav')
        self.npc_shot = pg.mixer.Sound(self.path + 'npc_attack.wav')
        self.game_over = pg.mixer.Sound(self.path + 'game_over_yeah.mp3')
        self.game_over.set_volume(1)
        self.npc_shot.set_volume(0.2)
        self.npc_pain.set_volume(0.3)
        self.npc_death.set_volume(1)
        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.mp3')
        self.theme = pg.mixer.music.load(self.path + 'theme.mp3')
        pg.mixer.music.set_volume(0.5)

    def stop_music(self):
        pg.mixer.music.set_volume(0)

