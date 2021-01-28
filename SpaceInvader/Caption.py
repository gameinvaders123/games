import pygame


class Caption:
    game = None

    def __init__(self, game):
        self.game = game

    @property
    def icon(self):
        return './ufo.png'

    def load(self):
        pygame.display.set_caption("Fish Invader")
        icon = pygame.image.load(self.icon)
