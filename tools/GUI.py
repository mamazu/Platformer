from pygame import font

from tools.utils import Drawable

font.init()
gui_font = font.SysFont("monospace", 20)


class Healthbar(Drawable):
    BACKGROUND_COLOR = (153, 153, 153)
    MODE = {
        "absolute": 1,
        "relative": 2
    }

    def __init__(self, pos, size, max_value=100, health=1.0):
        Drawable.__init__(self, pos, size)
        self.max_health = max_value
        self.display_mode = Healthbar.MODE["absolute"]
        self.set_health(health)
        self.set_col(Healthbar.BACKGROUND_COLOR)

    def set_health(self, value):
        if isinstance(value, float):
            self.health = value
        elif isinstance(value, int):
            self.health = float(value) / self.max_health
        self.hud_text = self.get_text()
        return None

    def set_mode(self, mode_name):
        if mode_name not in Healthbar.MODE:
            return
        self.display_mode = Healthbar.MODE[mode_name]
        self.hud_text = self.get_text()

    def get_health(self, string=False):
        print(self.display_mode)
        if self.display_mode == Healthbar.MODE["relative"]:
            return self.health if not string else str(self.health * 100) + "%"
        elif self.display_mode == Healthbar.MODE["absolute"]:
            value = self.health * self.max_health
            return value if not string else str(int(value)) + " HP"

    def get_text(self):
        content = self.get_health(string=True)
        text = gui_font.render(content, 1, (255, 255, 255))
        return text

    def draw(self, surf):
        from pygame.draw import rect
        from tools.utils import Pane
        from tools.VecMath import Vec2D
        Drawable.draw(self, surf)
        rect(surf, (153, 0, 0), Pane(self.pos, self.size * Vec2D(self.health, 1)).get_rect())
        surf.blit(self.hud_text, self.pos.get_tuple())


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
