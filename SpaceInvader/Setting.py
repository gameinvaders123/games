import json

class Setting:

    path = None
    data = None

    def __init__(self, path):
        self.path = path

    def load(self):
        with open(self.path) as f:
            self.data = json.load(f)

    @property
    def num_of_enemies(self):
        return self.data["num_of_enemies"]


