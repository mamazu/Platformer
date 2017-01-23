from tools.VecMath import Vec2D
from tools.utils import Drawable


class Player(Drawable):
    DEFAULTGRAVITY = 0.09
    DEFAULTSPEED = 2

    def __init__(self, pos=None, size=None):
        if not isinstance(pos, Vec2D):
            pos = Vec2D(10, 700)
        if not isinstance(size, int):
            size = Vec2D(30, 30)
        else:
            size = Vec2D(abs(size), abs(size))
        Drawable.__init__(self, pos, size)
        self.jumping = 0
        self.movement = Vec2D(Player.DEFAULTSPEED, Player.DEFAULTGRAVITY)

    def control(self, x):
        self.movement.x = 0 if x == 0 else x / abs(x) * Player.DEFAULTSPEED

    def move(self, level):
        temppos = Vec2D(vec=self.pos)
        # Checking x direction
        size = self.size.x if self.movement.x > 0 else 0
        temppos.x += size + self.movement.x - 1
        if not level.collide(temppos):
            self.pos.x += self.movement.x
        else:
            self.movement.x = 0
        temppos.x = self.pos.x

        # Checking y direction
        size = self.size.y if self.movement.y > 0 else 0
        temppos.y += size + self.movement.y - 1
        if not level.collide(temppos):
            self.pos.y += self.movement.y
            self.movement.y += Player.DEFAULTGRAVITY
        else:
            self.movement.y = 0
            self.jumping = 0

    def jump(self):
        if self.jumping > 1:
            return
        self.movement.y = -4
        self.jumping += 1

    def check_bounds(self, bounds):
        return bounds.contains(self.getRect())

    def draw(self, screen):
        from pygame.draw import rect
        rect(screen, (0, 0, 0), self.getRect())