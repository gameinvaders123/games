import pygame


class GameOver:
    game = None
    over_font = None
    y = 0
    x = 0

    def __init__(self, game):
        self.game = game

    def show(self):
        over_text = self.over_font.render("GAME OVER", True, (255, 255, 255))
        self.game.screen.blit(over_text, (200, 250))

    def load(self):
        # Game Over
        self.over_font = pygame.font.Font('freesansbold.ttf', 64)

