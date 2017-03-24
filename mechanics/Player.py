from mechanics.Entity import Entity
from tools.VecMath import Vec2D


class Player(Entity):
    DEFAULT_SPEED = 2

    def __init__(self, pos=None, size=None):
        Entity.__init__(self)
        self.pos = Vec2D(10, 700) if not isinstance(pos, Vec2D) else pos
        self.size = Vec2D(30, 30) if not isinstance(size, int) else Vec2D(abs(size), abs(size))
        self.set_image('res/player.png')
        self.movement = Vec2D(Player.DEFAULT_SPEED, Player.DEFAULT_GRAVITY)
        self.health = 100
        self.jumping = 0

    def control(self, x):
        self.movement.x = 0 if x == 0 else x / abs(x) * Player.DEFAULT_SPEED

    def move(self):
        x_move, y_move = Entity.move(self)
        if not y_move:
            self.jumping = False

    def jump(self):
        if self.jumping > 1:
            return
        self.movement.y = -4
        self.jumping += 1

    def check_bounds(self, bounds):
        return bounds.contains(self.get_rect())

    def damage(self):
        from random import randint
        self.health -= randint(0, 20)
        if self.health < 0:
            self.health = 0

    def draw(self, screen):
        Entity.draw(self, screen)

