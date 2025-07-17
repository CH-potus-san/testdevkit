from screens import TDKBoxLayout

class TDKLaunchLayout(TDKBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(
            **kwargs,
            orientation="vertical",
            src="./screens/source/launch.png",
            bg_color=(1, 1, 1, .25),
            rounded=True,
            spacing=15,
            padding=10,
            size_hint_min=(1.0, 0.3)
        )


class TDKLaunchButtonsRegionLayout(TDKBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(
            **kwargs,
            bg_color=(0.2, 0.2, 0.2, 0.0),
            size_hint=(1, 0.66),
            orientation="horizontal"
        )

class TDKLaunchButtonsZoneLayout(TDKBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(
            **kwargs,
            rounded=True,
            bg_color=(0.2, 0.2, 0.2, 0.6),
            orientation="vertical"
        )
