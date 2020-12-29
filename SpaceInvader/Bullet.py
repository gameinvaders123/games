import pygame
from pygame import mixer


class Bullet:
    game = None
    image = None
    x = 0
    y = 0
    x_change = 0
    y_change = 0
    state = 'ready'

    def __init__(self, game):
        self.game = game

    @property
    def image_file(self):
        return self.game.stage.folder + 'images/bullet.png'

    @property
    def sound_file(self):
        return self.game.stage.folder + 'sound/laser.wav'

    def position(self, x, y):
        self.state = "fire"
        self.game.screen.blit(self.image, (x + 16, y + 10))

    def load(self):
        self.image = pygame.image.load(self.image_file)
        self.x = 0
        self.y = 480
        self.x_change = 0
        self.y_change = 10
        self.state = "ready"

    def fire(self):
        if self.state is "ready":
            sound = mixer.Sound(self.sound_file)
            sound.play()
            self.position(self.x, self.y)

    def move(self):
        if self.y <= 0:
            self.y = 480
            bullet_state = "ready"

        if self.state is "fire":
            self.position(self.x, self.y)
            self.y -= self.y_change
        if self.y <= 0:
            bullet_y = 480
            bullet_state = "ready"

        if self.state is "fire":
            self.position(self.x, self.y)
            self.y -= self.y_change

    def pause(self):
        pass

    def show_help(self):
        pass
