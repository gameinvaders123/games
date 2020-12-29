import random
import pygame
from pygame import mixer
import math


class Enemy:

    game = None
    images = []
    x = []
    y = []
    x_change = []
    y_change = []

    def __init__(self, game):
        self.game = game

    @property
    def image_file(self):
        return self.game.stage.folder + 'images/enemy.png'

    def show(self, x, y, i):
        self.game.screen.blit(self.images[i], (x, y))

    def load(self):
        self.images = []
        self.x = []
        self.y = []
        self.x_change = []
        self.y_change = []

        num_of_enemies = self.game.stage.setting.num_of_enemies

        for i in range(num_of_enemies):
            self.images.append(pygame.image.load(self.image_file))
            self.x.append(random.randint(0, 736))
            self.y.append(random.randint(50, 150))
            self.x_change.append(4)
            self.y_change.append(40)

    def move(self):
        for i in range(self.game.stage.setting.num_of_enemies):
            if self.y[i] > 440:
                for j in range(self.game.stage.setting.num_of_enemies):
                    self.y[j] = 2000
                self.game.game_over.show()
                break

            self.x[i] += self.x_change[i]
            if self.x[i] <= 0:
                self.x_change[i]=4
                self.y[i] += self.y_change[i]
            elif self.x[i] >= 736:
                self.x_change[i] =- 4
                self.y[i] += self.y_change[i]

            # Collision
            collision = self.isCollision(self.x[i], self.y[i], self.game.bullet.x, self.game.bullet.y)
            if collision:
                self.game.explosion.explode()
                self.game.bullet.y = 480
                self.game.bullet.state = "ready"
                self.game.score.value += 1
                self.x[i] = random.randint(0, 736)
                self.y[i] = random.randint(50, 150)

            self.show(self.x[i], self.y[i], i)

    def isCollision(self, enemy_x, enemy_y, bullet_x, bullet_y):
        distance = math.sqrt(math.pow(enemy_x - bullet_x, 2) + (math.pow(enemy_y - bullet_y, 2)))
        if distance < 27:
            return True
        else:
            return False
