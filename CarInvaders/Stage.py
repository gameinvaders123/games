from Setting import Setting

class Stage:
    number = 0
    setting = None
    game = None
    max = 3

    def __init__(self, game):
        self.game = game
        self.setting = Setting(self.game)

    @property
    def folder(self):
        return "./stages/" + str(self.number) + "/"

    @property
    def folder_sound(self):
        return self.folder + "sound/"

    @property
    def folder_image(self):
        return self.folder + "image/"

    @property
    def folder_setting(self):
        return self.folder + "setting/"

    def next(self):
        if self.number < self.max:
            self.number += 1
            self.setting.load()
            return True
        else:
            return False

    def show(self):
        self.game.game_text.show(650, 10, "Stage : " + str(self.number), (255, 255, 255), 32)