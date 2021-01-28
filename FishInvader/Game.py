import pygame
from Background import Background
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
        self.screen = pygame.display.set_mode((800, 600))

        self.stage = Stage(self)
        self.background = Background(self)
        self.player = Player(self)
        self.bullet = Bullet(self)
        self.enemies = Enemies(self)
        self.game_text = GameText(self)
        self.explosion = Explosion(self)
        self.caption = Caption(self)
        self.score = Score(self)

        self.next_stage()

        while self.running:
            self.screen.fill((0, 0, 0))
            self.background.show()
            self.handle_event()

            self.player.move()
            self.bullet.move()
            self.enemies.move()
            self.score.show()
            self.stage.show()
            self.check_win()

            pygame.display.update()

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
                if event.key == pygame.K_RETURN:
                    self.next_stage()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.player.stop_move()

    def check_win(self):
        if self.enemies.finished():
           self.game_text.show_win()

           self.game_text.show_enter()

    def loose(self):
        self.game_text.show_loose()

    def next_stage(self):
        if not self.enemies.finished():
            return

        if not self.stage.next():
            return

        self.background.load()
        self.player.load()
        self.bullet.load()
        self.enemies.load()
        self.game_text.load()
        self.explosion.load()
        self.caption.load()
        self.score.load()
