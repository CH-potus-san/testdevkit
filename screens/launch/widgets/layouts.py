#Defaults for element parameters will be set here and instance calls will pass their
#settings through these templates to the Kivy widgets with added customization functionality.
from screens import TDKBoxLayout


class TDKLaunchLayout(TDKBoxLayout):
    #Set relevant parameter defaults here
    def __init__(
        self,
        orientation="vertical",
        bg_src=None, #"./screens/source/launch.png",
        bg_color=(.6, .6, .6, 1),
        rounded=True,
        spacing=15,
        padding=10,
        size_hint_min=(1.0, 0.3),
        **kwargs
    ):
        #Pass relevant parameters above to the parent class like a baton with unexpected changes
        super().__init__(
            orientation=orientation,
            bg_src=bg_src,
            bg_color=bg_color,
            rounded=rounded,
            spacing=spacing,
            padding=padding,
            size_hint_min=size_hint_min,
            **kwargs,
        )


class TDKLaunchButtonsRegionLayout(TDKBoxLayout):
    def __init__(
        self,
        bg_color=(0.2, 0.2, 0.2, 0.0),
        size_hint=(1, 0.66),
        orientation="horizontal",
        **kwargs
    ):
        super().__init__(
            **kwargs,
            bg_color=bg_color,
            size_hint=size_hint,
            orientation=orientation,
        )


class TDKLaunchButtonsZoneLayout(TDKBoxLayout):
    def __init__(
        self,
        rounded=True,
        bg_color=(0.2, 0.2, 0.2, 0.6),
        orientation="vertical",
        **kwargs
    ):
        super().__init__(
            **kwargs,
            rounded=rounded,
            bg_color=bg_color,
            orientation=orientation,
        )
