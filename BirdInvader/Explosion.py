from pygame import mixer


class Explosion:
    sound = None

    def __init__(self, game):
        self.game = game

    @property
    def sound_file(self):
        return self.game.stage.folder_sound + 'explosion.wav'

    def load(self):
        self.sound = mixer.Sound(self.sound_file)

    def explode(self):
        self.sound.play()
