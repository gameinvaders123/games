import pygame
from Stage import Stage
from Caption import Caption
from Player import Player
from Enemy import Enemy
from Bullet import Bullet
from GameOver import GameOver
from Explosion import Explosion
from Background import Background
from pygame import mixer

class Game:
    screen = None
    stage = None
    background = None
    caption = None
    player = None
    enemy = None
    bullet = None
    game_over = None
    explosion = None
    running = True

    def start(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))

        self.stage = Stage(self, 1)
        self.stage.load()

        self.background = Background(self)
        self.background.load()

        self.caption = Caption(self)
        self.caption.load()

        self.player = Player(self)
        self.player.load()

        self.enemy = Enemy(self)
        self.enemy.load()

        self.bullet = Bullet(self)
        self.bullet.load()

        self.game_over = GameOver(self)
        self.game_over.load()

        self.explosion = Explosion(self)

        while self.running:
            self.screen.fill((0, 0, 0))
            self.background.show()
            self.handle_event()

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.x_change = -5
                if event.key == pygame.K_RIGHT:
                    self.player.x_change = 5
                if event.key == pygame.K_SPACE:
                    self.bullet.fire()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.player.x_change = 0

        self.player.show()
        self.enemy.move()
        self.bullet.move()

        pygame.display.update()

    def show_setting(self):
        pass
