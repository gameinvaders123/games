from Background import Background
import pygame
from Player import Player
from Bullet import Bullet
from Enemies import Enemies
from Explosion import Explosion
from Caption import Caption
from GameText import GameText
from Score import Score
from Stage import Stage


class Game:
    running = True
    screen = None
    background = None
    player = None
    bullet = None
    enemies = None
    explosion = None
    caption = None
    game_text = None
    score = None
    stage = None

    def start(self):
        pygame.init()

        self.stage = Stage(self, 1)
        self.screen = pygame.display.set_mode((800, 600))

        self.background = Background(self)
        self.background.load()

        self.player = Player(self)
        self.player.load()

        self.bullet = Bullet(self)
        self.bullet.load()

        self.enemies = Enemies(self)
        self.enemies.load()

        self.game_text = GameText(self)
        self.game_text.load()

        self.explosion = Explosion(self)
        self.explosion.load()

        self.caption = Caption(self)
        self.caption.load()

        self.score = Score(self)
        self.score.load()

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
                    self.player.move_left()
                if event.key == pygame.K_RIGHT:
                    self.player.move_right()
                if event.key == pygame.K_SPACE:
                    self.bullet.fire(self.player.x, self.player.y)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.player.stop_move()

        self.player.move()
        self.bullet.move()
        self.enemies.move()
        self.score.show()
        self.win()

        pygame.display.update()

    def win(self):
        if self.enemies.finished():
            self.game_text.show_win()

    def loose(self):
        self.game_text.show_loose()

    def pause(self):
        pass

    def show_help(self):
        pass
