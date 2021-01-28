import pygame
from pygame import mixer
from BulletState import BulletState


class Bullet:
    game = None
    image = None
    sound = None
    x = 0
    y = 480
    x_change = 0
    y_change = 0
    state = 'ready'

    def __init__(self, game):
        self.game = game

    @property
    def image_file(self):
        return './bullet.png'

    @property
    def sound_file(self):
        return './bullet.wav'

    def load(self):
        self.image = pygame.image.load(self.image_file)
        self.sound = mixer.Sound(self.sound_file)
        self.x = 0
        self.y = 480
        self.x_change = 0
        self.y_change = 10
        self.state = BulletState.Ready

    def position(self, x, y):
        self.game.screen.blit(self.image, (x + 10, y + 10))

    def fire(self, x, y):
        if self.state is BulletState.Ready:
            self.state = BulletState.Fire
            self.x = x
            self.y = y
            self.sound.play()
            self.position(self.x - 10, self.y + 10)

    def move(self):
        if self.y <= 0:
            self.ready()

        if self.state is BulletState.Fire:
            self.position(self.x, self.y)
            self.y -= self.y_change

    def ready(self):
        self.y = 480
        self.state = BulletState.Ready
