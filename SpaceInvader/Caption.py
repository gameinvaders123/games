import pygame


class Caption:
    game = None

    def __init__(self, game):
        self.game = game

    @property
    def icon(self):
        return self.game.stage.folder + 'images/ufo.png'

    def load(self):
        pygame.display.set_caption("Space Invader")
        icon = pygame.image.load(self.icon)
        pygame.display.set_icon(icon)