import pygame
from pygame import mixer


class Background:
    game = None
    image = None
    sound = None

    def __init__(self, game):
        self.game = game

    @property
    def image_file(self):
        return self.game.stage.folder_image + 'background.png'

    @property
    def sound_file(self):
        return self.game.stage.folder_sound + 'background.wav'

    def load(self):
        self.image = pygame.image.load(self.image_file)

        self.sound = mixer.Sound(self.sound_file)
        self.sound.play(-1)

    def show(self):
        self.game.screen.blit(self.image, (0, 0))
