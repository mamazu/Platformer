from tools.utils import Drawable


class Healthbar(Drawable):
    BACKGROUND_COLOR = (153, 153, 153)

    def __init__(self, pos, size, max_value=100, health=1.0):
        Drawable.__init__(self, pos, size)
        self.max_health = max_value
        self.set_health(health)
        self.set_col(Healthbar.BACKGROUND_COLOR)

    def set_health(self, value):
        if isinstance(value, float):
            self.health = value
        elif isinstance(value, int):
            self.health = float(value) / self.max_health
        return None

    def draw(self, surf):
        from pygame.draw import rect
        from tools.utils import Pane
        from tools.VecMath import Vec2D
        Drawable.draw(self, surf)
        rect(surf, (153, 0, 0), Pane(self.pos, self.size * Vec2D(self.health, 1)).get_rect())


class GUI(Drawable):

    def __init__(self):
        Drawable.__init__(self)
        self.elements = []

    def add(self, param):
        if isinstance(param, Drawable):
            self.elements.append(param)

    def draw(self, surf):
        for gui_element in self.elements:
            gui_element.draw(surf)