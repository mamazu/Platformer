from tools.VecMath import Vec2D
from tools.utils import Drawable


class Entity(Drawable):
    DEFAULTGRAVITY = 0.09

    def __init__(self):
        Drawable.__init__(self)
        self.movement = Vec2D(0, 0)

    def move(self):
        from main import Game
        level = Game.level
        collision = []
        temppos = Vec2D(vec=self.pos)
        # Checking x direction
        size = self.size.x if self.movement.x > 0 else 0
        temppos.x += size + self.movement.x - 1
        collision.append(level.collide(temppos))
        if not collision[0]:
            self.pos.x += self.movement.x
        else:
            self.movement.x = 0
        temppos.x = self.pos.x

        # Checking y direction
        size = self.size.y if self.movement.y > 0 else 0
        temppos.y += size + self.movement.y - 1
        collision.append(level.collide(temppos))
        if not collision[1]:
            self.pos.y += self.movement.y
            self.movement.y += Entity.DEFAULTGRAVITY
        else:
            self.movement.y = 0
        return collision
