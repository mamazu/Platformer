from tools.VecMath import Pane


class Drawable(Pane):
    DEFAULTCOLOR = (0, 0, 0)

    def __init__(self, pos=None, size=None):
        Pane.__init__(self, pos, size)
        self.color = Drawable.DEFAULTCOLOR
        self.image = None

    def set(self, pane):
        if isinstance(pane, Pane):
            self.pos = pane.pos
            self.size = pane.size
            return True
        else:
            return False

    def set_col(self, col):
        if col is None:
            self.color = Drawable.DEFAULTCOLOR
            return
        if len(col) == 3:
            self.color = col

    def set_image(self, path):
        if path is None:
            self.image = None

        from os.path import isfile
        import pygame.image
        if isfile(path):
            self.image = pygame.image.load(path)
            self.image = pygame.transform.scale(self.image, self.size.getTuple())
        else:
            print("Invalid file")

    def __mul__(self, other):
        Pane.__mul__(self, other)

    def draw(self, surf):
        if self.image is None:
            from pygame.draw import rect
            rect(surf, self.color, self.getRect())
            return
        surf.blit(self.image, self.pos.getTuple())
