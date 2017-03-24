from mechanics.Entity import Entity
from tools.VecMath import Vec2D


class Player(Entity):
    DEFAULT_SPEED = 2

    def __init__(self, pos=None, size=None):
        Entity.__init__(self)
        self.pos = Vec2D(10, 700) if not isinstance(pos, Vec2D) else pos
        self.size = Vec2D(30, 30) if not isinstance(size, int) else Vec2D(abs(size), abs(size))
        self.set_image('res/doodle.png')
        self.movement = Vec2D(Player.DEFAULT_SPEED, Player.DEFAULT_GRAVITY)
        self.control(1)
        self.health = 100
        self.jumping = 0

    def control(self, x):
        if x == 0:
            self.movement.x = 0
            return
        direction = x / abs(x)
        # Flipping the image of the player if he turns around
        if direction != self.movement / Player.DEFAULT_SPEED:
            from pygame.transform import flip
            self.image = flip(self.image, True, False)
        self.movement.x = direction * Player.DEFAULT_SPEED

    def move(self):
        Entity.move(self)

        if self.movement.y == 0:
            self.jumping = 0

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

