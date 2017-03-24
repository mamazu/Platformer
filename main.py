import pygame
import time

from mechanics.Level import Level
from mechanics.Player import Player
from tools.Debugger import Debug
from tools.VecMath import Vec2D

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()


class Game:
    level = Level()
    player = Player()
    debugger = Debug()

    def __init__(self, size=None):
        if isinstance(size, Vec2D):
            self.size = size
        else:
            self.size = Vec2D(900, 800)
        self.screen = pygame.display.set_mode(self.size.get_tuple())
        self.running = True
        self.is_game_over = False
        self.setup()
        self.run()

    def setup(self):
        from tools.GUI import GUI
        from tools.GUI import Healthbar
        self.player = Game.player
        self.level = Game.level
        self.enemies = self.level.get_ememies()
        self.GUI = GUI()
        self.GUI.add(Healthbar(Vec2D(20, 20), Vec2D(200, 20)))

    def run(self):
        while self.running:
            start = time.time()
            # Event loop
            for event in pygame.event.get():
                self.handle_event(event)
            # Movement
            self.player.move()
            self.player.damage(self.enemies)
            self.GUI.elements[0].set_health(self.player.health)
            if not self.player.check_bounds(self.screen.get_rect()) or self.player.health == 0:
                self.gameover()
            self.level.move()
            self.draw()
            clock.tick(60)
            end = time.time()
            self.debugger.set_draw_call(end - start)

    def draw(self):
        # Drawing
        if not self.is_game_over:
            self.screen.fill((142, 193, 231))
            self.player.draw(self.screen)
            self.level.draw(self.screen)
            self.GUI.draw(self.screen)
        # Updating
        self.debugger.draw(self.screen)
        pygame.display.update()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            print("End of program")
            self.running = False
        elif event.type == pygame.KEYDOWN:
            key = event.key
            if key == pygame.K_ESCAPE:
                print("End of program")
                self.running = False
            elif key == pygame.K_SPACE or key == pygame.K_UP:
                self.player.jump()
            elif key == pygame.K_RIGHT:
                self.player.control(1)
            elif key == pygame.K_LEFT:
                self.player.control(-1)
            elif key == pygame.K_DOWN:
                self.player.control(0)
            elif key == pygame.K_d:
                self.debugger.toggle_debug()
            if self.is_game_over and key == pygame.K_r:
                self.setup()
                self.is_game_over = False

    def gameover(self):
        font = pygame.font.SysFont("monospace", 80)
        text = font.render("Game over", 1, (0, 0, 0))
        text_rect = Vec2D(vec=text.get_size())
        self.screen.blit(text, ((self.size - text_rect) / 2).get_tuple())
        self.is_game_over = True


if __name__ == "__main__":
    game = Game()
