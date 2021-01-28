import pygame


class GameText:
    game = None
    font64 = None
    font32 = None

    def __init__(self, game):
        self.game = game

    def show_win(self):
        self.show(230, 250, "YOU WIN!", (0, 0, 255), 64)

    def show_loose(self):
        self.show(200, 250, "YOU LOOSE!", (255, 0, 0), 64)

    def show_enter(self):
            self.show(170, 350, "Press Enter For Next Stage", (0, 255, 0), 32)

    def show(self, x, y, msg, color, size):
        text = None

        if size == 64:
            text = self.font64.render(msg, True, color)
        elif size == 32:
            text = self.font32.render(msg, True, color)

        self.game.screen.blit(text, (x, y))

    def load(self):
        self.font32 = pygame.font.Font('freesansbold.ttf', 32)

        self.font64 = pygame.font.Font('freesansbold.ttf', 64)
