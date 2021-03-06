from tools.VecMath import Vec2D, Pane
from tools.utils import Drawable


class Entity(Drawable):
    DEFAULT_GRAVITY = 0.09

    def __init__(self):
        Drawable.__init__(self)
        self.movement = Vec2D(0, 0)

    def collide(self, other):
        from pygame import Rect
        if isinstance(other, Rect):
            return self.get_rect().colliderect(other)
        if isinstance(other, Pane):
            return self.get_rect().colliderect(other.get_rect())
        return False

    def debug(self, surf):
        from pygame.draw import line
        start = self.pos + self.size / 2
        end = self.pos + self.size / 2 + self.movement * 5
        line(surf, (255, 255, 0), start.get_tuple(), end.get_tuple(), 5)

    def turn_around(self):
        from pygame.transform import flip
        self.movement.x *= -1
        self.image = flip(self.image, True, False)

    def move(self):
        from main import Game
        level = Game.level
        collision = []
        # Checking x direction
        xrect = self.get_rect().move(self.movement.x, -1)
        collision.append(level.collide(xrect))
        if not collision[0]:
            self.pos.x += self.movement.x
        else:
            self.movement.x = 0

        # Checking y direction
        yrect = self.get_rect().move(0, self.movement.y)
        collision.append(level.collide(yrect))
        if not collision[1]:
            self.pos.y += self.movement.y
            self.movement.y += Entity.DEFAULT_GRAVITY
        else:
            self.movement.y = 0
        return collision

    def draw(self, surf):
        from main import Game
        Drawable.draw(self, surf)
        if Game.debugger.get_debugging():
            self.debug(surf)
