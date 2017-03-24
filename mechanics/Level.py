from tools.VecMath import Vec2D
from tools.utils import Drawable


class Block(Drawable):
    COLOR = (0, 128, 0)

    def __init__(self, pos=None, size=None):
        Drawable.__init__(self, pos, size)
        self.enemy = None

    def collide(self, other):
        from pygame.rect import Rect
        if isinstance(other, Drawable):
            return other.get_rect().colliderect(self.get_rect())
        if isinstance(other, Rect):
            return other.colliderect(self.get_rect())
        if isinstance(other, Vec2D):
            return self.get_rect().collidepoint(other.get_tuple())
        else:
            return None

    def move(self):
        self.enemy.move()

    def add_enemy(self, enemy_type):
        from mechanics.Enemy import Enemy
        if enemy_type == 0:
            return
        self.enemy = Enemy(self.size)
        self.enemy.stand_on(self.get_rect())

    def draw(self, screen):
        import pygame
        pygame.draw.rect(screen, Block.COLOR, self.get_rect())
        if self.enemy is not None:
            self.enemy.draw(screen)


class Level:
    def __init__(self):
        from tools.levelLoader import load
        blocks = load('data/level1.lvl')
        self.blocks = []
        for b in blocks:
            block = Block(b['pos'], b['size'])
            block.add_enemy(b['enemy'])
            self.blocks.append(block)

    def move(self, move=None):
        for block in self.blocks:
            if block.enemy is None: continue
            block.move()
        if Vec2D.is_vec(move):
            for block in self.blocks:
                block.pos += move
            return True
        else:
            return False

    def collide(self, other):
        has_collided = False
        for block in self.blocks:
            has_collided |= block.collide(other)
        return has_collided

    def draw(self, screen):
        for block in self.blocks:
            block.draw(screen)

    def enemies(self, player):
        collision = False
        for block in self.blocks:
            if block.enemy is None: continue
            collision |= block.enemy.collide(player)
        return collision

    def get_ememies(self):
        enemies= [        ]
        for block in self.blocks:
            if block.enemy is None: continue
            enemies.append(block.enemy)
        return enemies
