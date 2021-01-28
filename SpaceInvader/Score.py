import pygame


class Score:
    game = None
    font = None
    value = 0

    def __init__(self, game):
        self.game = game

    def show(self):
        score = self.font.render("Score : " + str(self.value), True, (255, 255, 255))
        self.game.screen.blit(score, (10, 10))

    def load(self):
        # Score
        self.value = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        self.show()
