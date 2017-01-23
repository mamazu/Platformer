from tools.VecMath import Vec2D
from tools.utils import Drawable


class Block(Drawable):
    def __init__(self, pos=None, size=None):
        Drawable.__init__(self, pos, size)

    def collide(self, other):
        from pygame.rect import Rect
        if isinstance(other, Drawable):
            return other.getRect().colliderect(self.getRect())
        if isinstance(other, Rect):
            return other.colliderect(self.getRect())
        if isinstance(other, Vec2D):
            return self.getRect().collidepoint(other.getTuple())
        else:
            return None

    def draw(self, screen):
        import pygame
        pygame.draw.rect(screen, (255, 0, 0), self.getRect())


class Level:
    def __init__(self):
        from tools.levelLoader import load
        blocks = load('data/level1.lvl')
        self.blocks = [Block(b[0], b[1]) for b in blocks]

    def move(self, move=None):
        if Vec2D.isVec(move):
            for block in self.blocks:
                block.pos += move
            return True
        else:
            return False

    def collide(self, other):
        has_collided = False
        for block in self.blocks:
            has_collided |= block.collide(other)
        if has_collided:
            print("you hit something")
        return has_collided

    def draw(self, screen):
        for block in self.blocks:
            block.draw(screen)
