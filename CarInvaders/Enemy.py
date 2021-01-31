import pygame
import math
import random
from EnemyType import EnemyType


class Enemy:
    game = None
    enemy_type = None
    image = None
    x = 0
    y = 0
    x_change = 4
    y_change = 40

    def __init__(self, game, enemy_type):
        self.game = game
        self.enemy_type = enemy_type

    @property
    def image_file(self):
        return self.game.stage.folder_image + str(self.enemy_type) + '.png'

    @property
    def points(self):
        if self.enemy_type == EnemyType.King:
            return 100
        elif self.enemy_type == EnemyType.Queen:
            return 45
        elif self.enemy_type == EnemyType.Pawn:
            return 10
        else:
            return 0

    def show(self, x, y):
        self.game.screen.blit(self.image, (x, y))

    def load(self):
        self.image = pygame.image.load(self.image_file)
        self.x = random.randint(0, 736)
        self.y = random.randint(50, 150)

    def move(self):
        self.x += self.x_change
        if self.x <= 0:
            self.x_change = 4
            self.y += self.y_change
        elif self.x >= 736:
            self.x_change = -4
            self.y += self.y_change

        self.check_collision()
        self.show(self.x, self.y)

    def check_collision(self):
        distance = math.sqrt(math.pow(self.x - self.game.bullet.x, 2) + (math.pow(self.y - self.game.bullet.y, 2)))

        if distance < 268:
            self.game.explosion.explode()
            self.game.bullet.ready()

            self.game.score.value += self.points
            self.game.enemies.remove(self)

    def has_reached_player(self):
        return self.y > 440

    def hide(self):
        self.y = 2000
