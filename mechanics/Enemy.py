from mechanics.Entity import Entity
from tools.utils import Drawable


class Enemy(Entity):

    def __init__(self, obj):
        from tools.VecMath import Vec2D
        Drawable.__init__(self, size=Vec2D(30, 30))
        self.width = obj.x
        self.rel_pos = 1
        self.movement = Vec2D(1, 0)

    def stand_on(self, rect):
        from pygame import Rect
        from tools.VecMath import Vec2D
        x, y = 0, 0
        if isinstance(rect, Rect):
            x, y = rect.topleft
        elif isinstance(rect, Vec2D):
            x, y = rect.getTuple()
        self.pos = Vec2D(x, y - self.size.y)

    def move(self):
        print(self.rel_pos)
        if self.rel_pos == 0 or self.rel_pos == self.width - self.size.x:
            self.movement.x *= -1
        self.rel_pos += self.movement.x
        Entity.move(self)

    def draw(self, surf):
        from pygame.draw import rect
        rect(surf, (255, 0, 0), self.getRect())