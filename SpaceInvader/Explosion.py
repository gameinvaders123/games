from pygame import mixer


class Explosion:
    def __init__(self, game):
        self.game = game

    def explode(self):
        explosionSound = mixer.Sound(self.game.stage.explosion_sound)
        explosionSound.play()

