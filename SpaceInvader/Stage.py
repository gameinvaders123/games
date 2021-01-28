from Setting import Setting


class Stage:
    number = 3
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
    def folder_sound(self):
        return self.folder + "/sound"

    @property
    def folder_image(self):
        return self.folder + "/images"
