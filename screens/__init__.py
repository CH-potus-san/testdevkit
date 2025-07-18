# Import widgets used in this library to add necessary background properties and setters
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle, RoundedRectangle, BoxShadow


class TDKBoxLayout(BoxLayout):
    def __init__(
        self,
        bg_src=None,
        bg_color=(1, 1, 1, 1),
        fg_src="",
        fg_color=(1, 1, 1, 1),
        rounded=False,
        **kwargs
    ):
        super().__init__(**kwargs)

        self._bg_color = bg_color
        self._bg_src = bg_src
        self._fg_color = fg_color
        self._fg_src = fg_src

        with self.canvas.before:
            self.bg_color_instruction = Color(*self._bg_color)
            self.bg_rect = (
                Rectangle(source=self._bg_src, pos=self.pos, size=self.size)
                if not rounded
                else RoundedRectangle(source=self._bg_src, pos=self.pos, size=self.size)
            )
        
        with self.canvas.after:
            self.fg_color_instruction = Color(*self._fg_color)
            self.fg_rect = (
                Rectangle(source=self._fg_src, pos=self.pos, size=self.size)
                if not rounded
                else RoundedRectangle(source=self._fg_src, pos=self.pos, size=self.size)
            )


        self.bind(pos=self._update_bg, size=self._update_bg)

    @property
    def bg_color(self):
        return self._bg_color

    @bg_color.setter
    def bg_color(self, value):
        self._bg_color = value
        self.bg_color_instruction.rgba = value

    @property
    def bg_src(self):
        return self._bg_src

    @bg_src.setter
    def bg_src(self, src):
        self._bg_src = src
        self.bg_rect.source = src

    @property
    def fg_color(self):
        return self._fg_color

    @fg_color.setter
    def fg_color(self, value):
        self._fg_color = value
        self.fg_color_instruction.rgba = value

    @property
    def fg_src(self):
        return self._fg_src

    @fg_src.setter
    def fg_src(self, src):
        self._fg_src = src
        self.fg_rect.source = src

    def _update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size
        self.fg_rect.pos = self.pos
        self.fg_rect.size = self.size


class TDKButton(Button):
    def __init__(
        self,
        bg_color=(1, 1, 1, 1),
        bg_color_down=(0.7, 0.7, 1, 1),
        bg_src="",
        fg_color=(1, 1, 1, 1),
        fg_color_down=(0.6, 0.6, 0.6, 1),
        fg_src="",
        rounded=False,
        **kwargs
    ):
        super().__init__(**kwargs)

        self._bg_color = bg_color
        self._bg_color_down = bg_color_down
        self._bg_src = bg_src
        self._fg_color = fg_color
        self._fg_color_down = fg_color_down
        self._fg_src = fg_src

        self.background_normal = ""
        self.background_color = (1, 1, 1, 0)

        with self.canvas.before:
            self.bg_color_instruction = Color(*self._bg_color)
            self.bg_rect = (
                Rectangle(source=self._bg_src, pos=self.pos, size=self.size)
                if not rounded
                else RoundedRectangle(source=self._bg_src, pos=self.pos, size=self.size)
            )

        with self.canvas.after:
            self.fg_color_instruction = Color(*self._fg_color)
            self.fg_rect = (
                Rectangle(source=self._fg_src, pos=self.pos, size=self.size)
                if not rounded
                else RoundedRectangle(source=self._fg_src, pos=self.pos, size=self.size)
            )

        self.bind(pos=self._update_butt, size=self._update_butt)
        self.bind(state=self._on_state)

    def _update_butt(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size
        self.fg_rect.pos = self.pos
        self.fg_rect.size = self.size
        self.font_size = self.width ** (1 / 1.75)

    def _on_state(self, *args):
        self.bg_color_instruction.rgba = (
            self._bg_color_down if self.state == "down" else self._bg_color
        )
        self.fg_color_instruction.rgba = (
            self._fg_color_down if self.state == "down" else self._fg_color
        )

    @property
    def bg_color(self):
        return self._bg_color

    @bg_color.setter
    def bg_color(self, value):
        self._bg_color = value
        self.bg_color_instruction.rgba = value

    @property
    def bg_color_down(self):
        return self._bg_color_down

    @bg_color_down.setter
    def bg_color_down(self, value):
        self._bg_color_down = value

    @property
    def bg_src(self):
        return self._bg_src

    @bg_src.setter
    def bg_src(self, src):
        self._bg_src = src
        self.bg_rect.source = src

    @property
    def fg_color(self):
        return self._fg_color

    @fg_color.setter
    def fg_color(self, value):
        self._fg_color = value
        self.fg_color_instruction.rgba = value

    @property
    def fg_color_down(self):
        return self._fg_color_down

    @fg_color_down.setter
    def fg_color_down(self, value):
        self._fg_color_down = value

    @property
    def fg_src(self):
        return self._fg_src

    @fg_src.setter
    def fg_src(self, src):
        self._fg_src = src
        self.fg_rect.source = src
