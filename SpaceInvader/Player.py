import pygame


class Player:
    stage = None
    img = None
    x = 0
    y = 0
    x_change = 0

    def __init__(self, game):
        self.game = game

    @property
    def image_file(self):
        return self.game.stage.folder + 'images/player.png'

    def show(self):
        self.game.screen.blit(self.img, (self.x, self.y))

    def load(self):
        self.img = pygame.image.load(self.image_file)
        self.x = 370
        self.y = 480
        self.x_change = 0
        self.show()

    def move(self):
        self.x += self.x_change
        if self.x <= 0:
            self.x = 0
        elif self.x >= 736:
            self.x = 736

        self.show()
