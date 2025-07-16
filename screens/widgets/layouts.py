from screens.widgets import ColoredBoxLayout, TexturedBoxLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color, ClearColor


class TDKLaunchLayout(TexturedBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(
            **kwargs,
            orientation="vertical",
            spacing=15,
            padding=10,
            size_hint_min=(1.0, 0.3)
        )


class TDKLaunchButtonsRegionLayout(ColoredBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(
            **kwargs,
            bg_color=(0.2, 0.2, 0.2, 0.0),
            size_hint=(1, 0.66),
            orientation="horizontal"
        )

class TDKLaunchButtonsZoneLayout(ColoredBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(
            **kwargs,
            rounded=True,
            bg_color=(0.2, 0.2, 0.2, 0.6),
            spacing=25,
            orientation="vertical"
        )
