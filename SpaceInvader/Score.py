import pygame


class Score:
    game = None
    font = None
    value = 0
    x = 0
    y = 0

    def __init__(self, game):
        self.game = game

    def show(self, x, y):
        score = self.font.render("Score : " + str(self.value), True, (255, 255, 0))
        self.game.screen.blit(score, (x, y))

    def load(self):
        # Score
        score_value = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        self.show_score(self.x, self.y)