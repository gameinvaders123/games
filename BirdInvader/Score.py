class Score:
    game = None
    value = 0

    def __init__(self, game):
        self.game = game

    def show(self):
        self.game.game_text.show(10, 10, "Score : " + str(self.value), (255, 255, 255), 32)

    def load(self):
        self.value = 0
        self.show()
