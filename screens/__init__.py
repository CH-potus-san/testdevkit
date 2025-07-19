# Import widgets used in this library to add necessary background properties and setters
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, RoundedRectangle, BoxShadow


class TDKBoxLayout(BoxLayout):
    def __init__(
        self,
        sh_color=None,
        bg_src="./screens/source/empty.png",
        bg_color=(1, 1, 1, 1),
        fg_src="./screens/source/empty.png",
        fg_color=(1, 1, 1, 0),
        fg_scale=(1.015, 1.015),
        rounded=False,
        **kwargs
    ):
        super().__init__(**kwargs)

        if not sh_color:
            br, bg, bb, ba = bg_color
            fr, fg, fb, fa = fg_color
            sh_color = (round(1-br*fr, 2), round(1-bg*fg, 2), round(1-bb*fb, 2), round(1-ba*fa))

        self.fg_scale = fg_scale

        self._sh_color = sh_color
        self._bg_color = bg_color
        self._bg_src = bg_src
        self._fg_color = fg_color
        self._fg_src = fg_src

        with self.canvas.before:
            self.sh_color_instruction = Color(*self.sh_color)
            self.shadow = BoxShadow(
                pos=self.pos,
                size=self.size,
                offset=(0, -10),
                spread_radius=(-20, -20),
                blur_radius=75,
            )
            self.bg_color_instruction = Color(*self.bg_color)
            self.bg_rect = (
                Rectangle(source=self.bg_src, pos=self.pos, size=self.size)
                if not rounded
                else RoundedRectangle(source=self.bg_src, pos=self.pos, size=self.size)
            )

        with self.canvas.after:
            fg_width = self.size[0] * self.fg_scale[0]
            fg_height = self.size[1] * self.fg_scale[1]
            self.fg_color_instruction = Color(*self.fg_color)
            self.fg_rect = (
                Rectangle(
                    source=self.fg_src,
                    pos=(
                        (self.x - fg_width - self.width) / 2,
                        (self.y - fg_height - self.height) / 2,
                    ),
                    size=(fg_width, fg_height),
                )
                if not rounded
                else RoundedRectangle(
                    source=self._fg_src,
                    pos=(
                        (self.x - fg_width - self.width) / 2,
                        (self.y - fg_height - self.height) / 2,
                    ),
                    size=(fg_width, fg_height),
                )
            )

        self.bind(pos=self._update_bg, size=self._update_bg)

    def _update_bg(self, *args):
        self.shadow.pos = self.pos
        self.shadow.size = self.size
        fg_width = self.size[0] * self.fg_scale[0]
        fg_height = self.size[1] * self.fg_scale[1]
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size
        self.fg_rect.pos = (
            self.x - (fg_width - self.width) / 2,
            self.y - (fg_height - self.height) / 2,
        )
        self.fg_rect.size = (fg_width, fg_height)

    @property
    def sh_color(self):
        return self._sh_color

    @sh_color.setter
    def sh_color(self, value):
        self._sh_color = value
        self.sh_color_instruction.rgba = value

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


class TDKButton(Button):
    def __init__(
        self,
        sh_color=None,
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

        if not sh_color:
            br, bg, bb, ba = bg_color
            fr, fg, fb, fa = fg_color
            sh_color = (round(1-br*fr, 2), round(1-bg*fg, 2), round(1-bb*fb, 2), round(1-ba*fa))

        self._sh_color = sh_color
        self._bg_color = bg_color
        self._bg_color_down = bg_color_down
        self._bg_src = bg_src
        self._fg_color = fg_color
        self._fg_color_down = fg_color_down
        self._fg_src = fg_src

        self.background_normal = ""
        self.background_color = (1, 1, 1, 0)

        with self.canvas.before:
            self.sh_color_instruction = Color(*self.sh_color)
            self.shadow = BoxShadow(
                pos=self.pos,
                size=self.size,
                offset=(0, -10),
                spread_radius=(-20, -20),
                blur_radius=75,
            )
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
        self.shadow.pos = self.pos
        self.shadow.size = self.size
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
    def sh_color(self):
        return self._sh_color

    @sh_color.setter
    def sh_color(self, value):
        self._sh_color = value
        self.sh_color_instruction.rgba = value

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


class TDKLabel(Label):
    def __init__(
        self,
        sh_color=None,
        bg_src=None,
        bg_color=(1, 1, 1, 1),
        fg_src="./screens/source/empty.png",
        fg_color=(1, 1, 1, 1),
        fg_scale=(1.015, 1.015),
        rect_padding=(20, 10),
        rounded=False,
        **kwargs
    ):
        super().__init__(**kwargs)

        if not sh_color:
            br, bg, bb, ba = bg_color
            fr, fg, fb, fa = fg_color
            sh_color = (round(1-br*fr, 2), round(1-bg*fg, 2), round(1-bb*fb, 2), round(1-ba*fa))

        self.fg_scale = fg_scale
        self.rect_padding = rect_padding

        self._sh_color = sh_color
        self._bg_color = bg_color
        self._bg_src = bg_src
        self._fg_color = fg_color
        self._fg_src = fg_src

        with self.canvas.before:
            self.sh_color_instruction = Color(*self.sh_color)
            self.shadow = BoxShadow(
                pos=self.pos,
                size=self.size,
                offset=(0, -10),
                spread_radius=(-20, -20),
                blur_radius=75,
            )
            self.bg_color_instruction = Color(*self.bg_color)
            self.bg_rect = (
                Rectangle(source=self.bg_src, pos=self.pos, size=self.size)
                if not rounded
                else RoundedRectangle(source=self._bg_src, pos=self.pos, size=self.size)
            )

        with self.canvas.after:
            fg_width = self.size[0] * self.fg_scale[0]
            fg_height = self.size[1] * self.fg_scale[1]
            self.fg_color_instruction = Color(*self.fg_color)
            self.fg_rect = (
                Rectangle(
                    source=self.fg_src,
                    pos=(
                        (self.x - fg_width - self.width) / 2,
                        (self.y - fg_height - self.height) / 2,
                    ),
                    size=(fg_width, fg_height),
                )
                if not rounded
                else RoundedRectangle(
                    source=self.fg_src,
                    pos=(
                        (self.x - fg_width - self.width) / 2,
                        (self.y - fg_height - self.height) / 2,
                    ),
                    size=(fg_width, fg_height),
                )
            )

        self.bind(pos=self._update_bg, size=self._update_bg)

    def _update_bg(self, *args):
        text_width, text_height = self.texture_size
        pad_x, pad_y = self.rect_padding

        rect_x = self.center_x - text_width / 2 - pad_x
        rect_y = self.center_y - text_height / 2 - pad_y
        rect_w = text_width + pad_x * 2
        rect_h = text_height + pad_y * 2

        fg_width = rect_w * self.fg_scale[0]
        fg_height = rect_h * self.fg_scale[1]

        self.shadow.pos = (rect_x, rect_y)
        self.shadow.size = (rect_w, rect_h)
        self.bg_rect.pos = (rect_x, rect_y)
        self.bg_rect.size = (rect_w, rect_h)

        self.fg_rect.pos = (
            self.x - (fg_width - self.width) / 2,
            self.y - (fg_height - self.height) / 2,
        )
        self.fg_rect.size = (fg_width, fg_height)

    @property
    def sh_color(self):
        return self._sh_color

    @sh_color.setter
    def sh_color(self, value):
        self._sh_color = value
        self.sh_color_instruction.rgba = value

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
