import pygame
from pygame import mixer


class Background:
    game = None
    image = None

    def __init__(self, game):
        self.game = game

    @property
    def image_file(self):
        return self.game.stage.folder + 'images/background.png'

    @property
    def sound(self):
        return self.game.stage.folder + 'sound/background.wav'

    def load(self):
        self.image = pygame.image.load(self.image_file)

        mixer.music.load(self.sound)
        mixer.music.play(-1)

    def show(self):
        self.game.screen.blit(self.image, (0, 0))
