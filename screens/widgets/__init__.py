#Import widgets used in this library to add necessary background properties and setters
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle, RoundedRectangle

class TexturedBoxLayout(BoxLayout):
    def __init__(self, src="./mindmap/launch.png", **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            self.bg_rect = Rectangle(source=src, pos=self.pos, size=self.size)
        self.bind(pos=self._update_bg, size=self._update_bg)

    def _update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size


class ColoredBoxLayout(BoxLayout):
    def __init__(self, bg_color=(1, 1, 1, 1), rounded=False, **kwargs):
        super().__init__(**kwargs)
        self._bg_color=bg_color
        with self.canvas.before:
            self.bg_color_before = Color(*self._bg_color)
            self.bg_rect = Rectangle(pos=self.pos, size=self.size) if not rounded else RoundedRectangle(pos=self.pos, size=self.size)
        self.bind(pos=self._update_bg, size=self._update_bg)

    @property
    def bg_color(self):
        return self._bg_color
    
    @bg_color.setter
    def bg_color(self, value):
        self._bg_color = value
        self.bg_color_before.rgba = value

    def _update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size

class ColoredButton(Button):
    def __init__(self, bg_color=(1, 1, 1, 1), **kwargs):
        super().__init__(**kwargs)
        self._bg_color=bg_color
        with self.canvas.before:
            self.bg_color_before=Color(*self._bg_color)
            self.bg_rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self._update_bg, size=self._update_bg)

    @property
    def bg_color(self):
        return self._bg_color
    
    @bg_color.setter
    def bg_color(self, value):
        self._bg_color = value
        self.bg_color_before.rgba = value

    def _update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size
        