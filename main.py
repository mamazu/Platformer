import pygame
from mechanics.Level import Level
from mechanics.Player import Player

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

class Game:
    level = Level()
    player = Player()

    def __init__(self, size=None):
        from tools.VecMath import Vec2D
        if isinstance(size, Vec2D):
            self.size = size
        else:
            self.size = Vec2D(900, 800)
        self.screen = pygame.display.set_mode(self.size.getTuple())
        self.running = True
        self.isGameover = False
        self.run()

    def setup(self):
        self.player = Player()
        self.level = Level()

    def run(self):
        while self.running:
            # Event loop
            for event in pygame.event.get():
                self.handle_event(event)
            # Movement
            self.player.move()
            if self.level.enemies(self.player):
                self.player.damage()
            if not self.player.check_bounds(self.screen.get_rect()):
                self.gameover()
            self.level.move()
            self.draw()
            clock.tick(60)

    def draw(self):
        # Drawing
        if not self.isGameover:
            self.screen.fill((142, 193, 231))
            self.player.draw(self.screen)
            self.level.draw(self.screen)
        # Updating
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
            if self.isGameover and key == pygame.K_r:
                self.setup()
                self.isGameover = False

    def gameover(self):
        font = pygame.font.SysFont("monospace", 80)
        text = font.render("Game over", 1, (0, 0, 0))
        self.screen.blit(text, (self.size / 2).getTuple())
        self.isGameover = True

if __name__ == "__main__":
    game = Game()
