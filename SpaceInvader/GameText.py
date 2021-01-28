import pygame


class GameText:
    game = None
    over_font = None
    y = 0
    x = 0

    def __init__(self, game):
        self.game = game

    def show_win(self):
        over_text = self.over_font.render("YOU WIN", True, (0, 0, 255))
        self.game.screen.blit(over_text, (200, 250))

    def show_loose(self):
        over_text = self.over_font.render("YOU LOOSE!", True, (255, 0, 0))
        self.game.screen.blit(over_text, (200, 250))

    def load(self):
        self.over_font = pygame.font.Font('freesansbold.ttf', 64)
