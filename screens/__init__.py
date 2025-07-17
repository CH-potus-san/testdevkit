# Import widgets used in this library to add necessary background properties and setters
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle, RoundedRectangle


class TDKBoxLayout(BoxLayout):
    def __init__(self, src=None, bg_color=(1, 1, 1, 1), rounded=False, **kwargs):
        super().__init__(**kwargs)

        self._bg_color = bg_color
        self._bg_src = src

        with self.canvas.before:
            self.bg_color_before = Color(*self._bg_color)
            self.bg_rect = (
                Rectangle(source=self._bg_src, pos=self.pos, size=self.size)
                if not rounded
                else RoundedRectangle(source=self._bg_src, pos=self.pos, size=self.size)
            )

        self.bind(pos=self._update_bg, size=self._update_bg)

    @property
    def bg_color(self):
        return self._bg_color

    @bg_color.setter
    def bg_color(self, value):
        self._bg_color = value
        self.bg_color_before.rgba = value

    @property
    def bg_src(self):
        return self._bg_src

    @bg_src.setter
    def bg_src(self, src):
        self._bg_src = src
        self.bg_rect.source = src

    def _update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size


class TDKButton(Button):
    def __init__(self, src='', bg_color=(1, 1, 1, 1), **kwargs):
        super().__init__(**kwargs)
        self.background_normal = src
        self.background_color = bg_color