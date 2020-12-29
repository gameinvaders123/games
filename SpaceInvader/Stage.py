from Setting import Setting


class Stage:

    number = 0
    setting = None
    game = None

    def __init__(self, game, number):
        self.number = number
        self.game = game

    def load(self):
        self.setting = Setting(self.folder + "setting/setting.json")
        self.setting.load()

    @property
    def folder(self):
        return "./stages/" + str(self.number) + "/"

    @property
    def explosion_sound(self):
        return self.game.stage.folder + 'sound/explosion.wav'
