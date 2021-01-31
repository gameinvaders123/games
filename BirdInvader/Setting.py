import json


class Setting:
    game = None
    data = None

    def __init__(self, game):
        self.game = game

    @property
    def file_path(self):
        return self.game.stage.folder_setting + "setting.json"

    def load(self):
        with open(self.file_path) as f:
            self.data = json.load(f)

    @property
    def num_of_pawns(self):
        return int(self.data["num_of_pawns"])
