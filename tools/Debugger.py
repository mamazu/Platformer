import pygame

from tools.utils import Drawable

pygame.font.init()
font = pygame.font.SysFont('monospace', 16)
is_debugging = False


class Debug(Drawable):
    def __init__(self):
        Drawable.__init__(self)
        self.hud_elements = {
            'fpsCounter': FPSCounter()
        }
        self.draw_call = 1

    def get_debugging(self):
        return is_debugging

    def toggle_debug(self):
        global is_debugging
        is_debugging = not is_debugging

    def set_draw_call(self, time):
        self.hud_elements['fpsCounter'].draw_call = time

    def draw(self, surf):
        if not is_debugging:
            return
        for hud_name, hud_element in self.hud_elements.items():
            hud_element.draw(surf)


class FPSCounter(Drawable):
    def __init__(self):
        Drawable.__init__(self)
        self.draw_call = 1

    def show_fps(self):
        fps = int(1 / self.draw_call)
        return font.render('%i fps' % fps, 1, (0, 0, 0))

    def draw(self, surf):
        surf.blit(self.show_fps(), self.pos.get_tuple())
