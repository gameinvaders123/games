from EnemyType import EnemyType
from Enemy import Enemy


class Enemies:
    game = None
    num_of_pawns = 6
    enemy_list = []

    def __init__(self, game):
        self.game = game

    def load(self):
        self.add(EnemyType.King)
        self.add(EnemyType.Queen)

        for i in range(self.num_of_pawns):
            self.add(EnemyType.Pawn)

    def add(self, enemy_type):
        enemy = Enemy(self.game, enemy_type)
        self.enemy_list.append(enemy)
        enemy.load()

    def remove(self, enemy):
        self.enemy_list.remove(enemy)

    def finished(self):
        if len(self.enemy_list) == 0:
            return True
        else:
            return False

    def move(self):
        for enemy in self.enemy_list:
            if enemy.has_reached_player():
                self.game_loose()
                break
            else:
                enemy.move()

    def game_loose(self):
        for enemy in self.enemy_list:
            enemy.hide()

        self.game.loose()

